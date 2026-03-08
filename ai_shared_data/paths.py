from __future__ import annotations

import os
from pathlib import Path


# Default root for shared assets
DEFAULT_DATA_HOME = Path("~/src/data").expanduser()


def get_data_home() -> Path:
    """
    Root directory containing shared data assets.

    Priority:
    1. AI_DATA_HOME environment variable
    2. default: ~/src/data
    """
    env_value = os.environ.get("AI_DATA_HOME")
    if env_value:
        return Path(env_value).expanduser().resolve()

    return DEFAULT_DATA_HOME.resolve()


def get_asset_home(kind: str | None = None) -> Path:
    """
    Return the root directory for a given asset type.

    Allows overrides like:

        AI_DATA_HOME=~/src/data
        AI_MODELS_HOME=/mnt/models
        AI_EMBEDDINGS_HOME=/mnt/embeddings
    """

    base = get_data_home()

    if kind is None:
        return base

    env_name = f"AI_{kind.upper()}_HOME"
    override = os.environ.get(env_name)

    if override:
        return Path(override).expanduser().resolve()

    return base / kind


def ensure_asset_dir(kind: str) -> Path:
    """
    Ensure the directory for a given asset type exists.
    """
    path = get_asset_home(kind)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_path(*parts: str, kind: str | None = None) -> Path:
    """
    Return a path under the appropriate asset root.

    Example:
        get_path("interpretability", "asv_clean_nt.txt", kind="datasets")
    """

    root = get_asset_home(kind)
    return root.joinpath(*parts)
