from dataclasses import dataclass
from typing import Optional


@dataclass
class Dataset:
    name: str
    relative_path: str
    description: Optional[str] = None


DATASETS = {
    "asv_raw": Dataset(
        name="asv_raw",
        relative_path="interpretability/asv.txt",
        description="American Standard Version Bible"
    ),

    "asv_clean_nt": Dataset(
        name="asv_clean_nt",
        relative_path="interpretability/asv_clean_nt.txt",
        description="Cleaned New Testament used for language modeling"
    ),

    "the_verdict": Dataset(
        name="the_verdict",
        relative_path="interpretability/the_verdict.txt",
        description="Short text used in LLM-from-scratch examples"
    ),
}
