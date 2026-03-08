from dataclasses import dataclass
from typing import Optional, Callable
from ai_shared_data.builders import build_acl_imdb, build_asv_raw
from ai_shared_data.builders import build_jena_climate, build_asv_clean_nt
from ai_shared_data.builders import build_dogs_vs_cats, build_oxford_pets
from ai_shared_data.builders import build_glove_6B

@dataclass
class Asset:
    name: str
    kind: str
    relative_path: str
    description: Optional[str] = None
    builder: Optional[Callable[[], None]] = None
    depends_on: Optional[list[str]] = None    


DATASETS = {
    "dogs_vs_cats": Asset(
        name="dogs_vs_cats",
        kind="datasets",
        relative_path="dogs-vs-cats",
        description="Kaggle Dogs vs Cats image classification dataset",
        builder=build_dogs_vs_cats
    ),

    "oxford_pets": Asset(
        name="oxford_pets",
        kind="datasets",
        relative_path="images",
        description="Oxford-IIIT Pet dataset (images and segmentation annotations)",
        builder=build_oxford_pets,
    ),

    "aclImdb": Asset(
        name="aclImdb",
        kind="datasets",
        relative_path="aclImdb",
        description="Large Movie Review Dataset for binary sentiment classification",
        builder=build_acl_imdb
    ),

    "glove.6B.50d": Asset(
        name="glove.6B.50d",
        kind="embeddings",
        relative_path="glove.6B",
        description="GloVe 6B 50-dimensional word embeddings",
        builder=build_glove_6B
    ),
    "glove.6B.100d": Asset(
        name="glove.6B.100d",
        kind="embeddings",
        relative_path="glove.6B",
        description="GloVe 6B 100-dimensional word embeddings",
        builder=build_glove_6B
    ),  
    "glove.6B.200d": Asset(
        name="glove.6B.200d",
        kind="embeddings",
        relative_path="glove.6B",
        description="GloVe 6B 200-dimensional word embeddings",
        builder=build_glove_6B  
    ),
    "glove.6B.300d": Asset(
        name="glove.6B.300d",
        kind="embeddings",
        relative_path="glove.6B",
        description="GloVe 6B 300-dimensional word embeddings",
        builder=build_glove_6B
    ),

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
        builder=build_asv_clean_nt,
        depends_on=["asv_raw"]
    ),

    "the_verdict": Asset(
        name="the_verdict",
        kind="datasets",
        relative_path="interpretability/the_verdict.txt",
        description="Short text used in LLM-from-scratch examples",
    ),

    "jena_climate": Asset(
        name="jena_climate",
        kind="datasets",
        relative_path="jena_climate_2009_2016.csv",
        description="Temperature forecasting dataset",
        builder=build_jena_climate
    ),
}

EMBEDDINGS = {
    # "glove_6B": Asset(...),
    # "fasttext_wiki_news": Asset(...),
}

MODELS = {
    # future model checkpoints
}

ARCHIVES = {
    # optional raw archives if you want to track them explicitly
}

ASSETS = {}
ASSETS.update(DATASETS)
ASSETS.update(EMBEDDINGS)
ASSETS.update(MODELS)
ASSETS.update(ARCHIVES)


# ---- registry validation ----

for key, asset in ASSETS.items():
    if key != asset.name:
        raise ValueError(
            f"Registry mismatch: key '{key}' does not match asset.name '{asset.name}'"
        )
