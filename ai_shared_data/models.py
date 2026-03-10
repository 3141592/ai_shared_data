from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def get_models_root(data_root: Path) -> Path:
    path = data_root / "models"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_metadata(meta_path: Path, metadata: dict[str, Any]) -> None:
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, sort_keys=True)


def _build_metadata(
    *,
    name: str,
    framework: str,
    artifact_type: str,
    script: str | None = None,
    dataset: str | None = None,
    notes: str | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "name": name,
        "framework": framework,
        "artifact_type": artifact_type,
        "created": _utc_now_iso(),
    }
    if script:
        metadata["script"] = script
    if dataset:
        metadata["dataset"] = dataset
    if notes:
        metadata["notes"] = notes
    if extra:
        metadata["extra"] = extra
    return metadata


def save_keras_model(
    model: Any,
    *,
    data_root: Path,
    name: str,
    script: str | None = None,
    dataset: str | None = None,
    notes: str | None = None,
    extra: dict[str, Any] | None = None,
) -> Path:
    model_dir = get_models_root(data_root) / "keras"
    model_dir.mkdir(parents=True, exist_ok=True)

    model_path = model_dir / f"{name}.keras"
    model.save(model_path)

    metadata = _build_metadata(
        name=name,
        framework="keras",
        artifact_type="model",
        script=script,
        dataset=dataset,
        notes=notes,
        extra=extra,
    )
    _write_metadata(model_path.with_suffix(".meta.json"), metadata)
    return model_path


def save_torch_checkpoint(
    checkpoint: dict[str, Any],
    *,
    data_root: Path,
    name: str,
    script: str | None = None,
    dataset: str | None = None,
    notes: str | None = None,
    extra: dict[str, Any] | None = None,
) -> Path:
    import torch

    model_dir = get_models_root(data_root) / "torch"
    model_dir.mkdir(parents=True, exist_ok=True)

    ckpt_path = model_dir / f"{name}.pt"
    torch.save(checkpoint, ckpt_path)

    metadata = _build_metadata(
        name=name,
        framework="torch",
        artifact_type="checkpoint",
        script=script,
        dataset=dataset,
        notes=notes,
        extra=extra,
    )
    _write_metadata(ckpt_path.with_suffix(".meta.json"), metadata)
    return ckpt_path
