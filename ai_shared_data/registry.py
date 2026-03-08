from dataclasses import dataclass
from typing import Optional, Callable
from ai_shared_data.builders import build_asv_raw, build_jena_climate, build_asv_clean_nt

@dataclass
class Asset:
    name: str
    kind: str
    relative_path: str
    description: Optional[str] = None
    builder: Optional[Callable[[], None]] = None


ASSETS = {
    "asv_raw": Asset(
        name="asv_raw",
        kind="datasets",
        relative_path="interpretability/asv.txt",
        description="American Standard Version Bible",
        builder=build_asv_raw
    ),

    "asv_clean_nt": Asset(
        name="asv_clean_nt",
        kind="datasets",
        relative_path="interpretability/asv_clean_nt.txt",
        description="Cleaned New Testament used for language modeling",
        builder=build_asv_clean_nt
    ),

    "the_verdict": Asset(
        name="the_verdict",
        kind="datasets",
        relative_path="interpretability/the_verdict.txt",
        description="Short text used in LLM-from-scratch examples",
        builder=build_asv_clean_nt
    ),

    "jena_climate": Asset(
        name="jena_climate",
        kind="datasets",
        relative_path="jena_climate_2009_2016.csv",
        description="Temperature forecasting dataset",
        builder=build_jena_climate
    ),
}

# ---- registry validation ----

for key, asset in ASSETS.items():
    if key != asset.name:
        raise ValueError(
            f"Registry mismatch: key '{key}' does not match asset.name '{asset.name}'"
        )
