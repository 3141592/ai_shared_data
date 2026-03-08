from dataclasses import dataclass
from typing import Optional


@dataclass
class Asset:
    name: str
    kind: str
    relative_path: str
    description: Optional[str] = None


ASSETS = {
    "asv_raw": Asset(
        name="asv_raw",
        kind="datasets",
        relative_path="interpretability/asv.txt",
        description="American Standard Version Bible"
    ),

    "asv_clean_nt": Asset(
        name="asv_clean_nt",
        kind="datasets",
        relative_path="interpretability/asv_clean_nt.txt",
        description="Cleaned New Testament used for language modeling"
    ),

    "the_verdict": Asset(
        name="the_verdict",
        kind="datasets",
        relative_path="interpretability/the_verdict.txt",
        description="Short text used in LLM-from-scratch examples"
    ),
}
