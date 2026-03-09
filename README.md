# ai_shared_data

Shared dataset utilities for machine learning and mechanistic interpretability projects.

This repository provides:

- A **single shared dataset location**
- Utilities for **downloading and preparing assets**
- A consistent way for multiple repositories to **locate datasets**

The goal is to **avoid duplicating dataset download and preprocessing code** across projects.

---

# Design

Datasets and other large assets are stored **outside project repositories** in a shared directory.

Default location:

    ~/src/data

This location can be overridden:

    export AI_DATA_HOME=/path/to/data

Projects import `ai_shared_data` to:

- locate assets
- download assets if missing
- build derived datasets

---

# Repository Layout

    ai_shared_data/
        ai_shared_data/
            paths.py
            fetch.py
            registry.py
            builders/
                bible.py
                glove.py
                text_datasets.py
                vision_datasets.py
        README.md

Example installed data directory:

    ~/src/data/
        datasets/
            aclImdb/
            annotations/
            celeba_gan/
            dogs-vs-cats/
            images/  
            interpretability/
            jena_climate_2009_2016.csv
            __MACOSX/
            spa-eng/
        embeddings/ 
            fasttext/
            glove.6B/

Large files remain **outside Git repositories**.

---

# Installing

Clone the repository and install in editable mode:

    git clone https://github.com/<user>/ai_shared_data.git
    cd ai_shared_data
    pip install -e .

Editable installation allows updates without reinstalling.

---

# Using From Another Repository

Example usage:

    from ai_shared_data.fetch import ensure_asset
    from ai_shared_data.paths import get_asset_path

    ensure_asset("asv_nt_clean")

    path = get_asset_path("asv_nt_clean")

Behavior:

1. If the asset already exists → return path  
2. If missing → run the registered builder  
3. Builder downloads or generates the dataset

---

# Asset Registry

Assets are defined in:

    ai_shared_data/registry.py

Each asset describes:

- name
- type (text, embeddings, vision, etc.)
- relative path
- builder function

Example:

    Asset(
        name="glove.6B",
        kind="embeddings",
        relative_path="glove.6B.100d.txt",
        description="GloVe 6B 100-dimensional word embeddings",
        builder=build_glove_6B
    )

---

# Available Assets

Example assets currently supported:

| asset | description |
|------|-------------|
| `the_verdict` | short text used in *Build an LLM from Scratch* |
| `asv_raw` | American Standard Version Bible |
| `asv_nt_clean` | cleaned New Testament text for language modeling |
| `glove.6B` | Stanford GloVe word embeddings |
| `celeba` | CelebA face dataset used for GAN experiments |

---

# Asset Naming Conventions

To keep asset names consistent across repositories:

- Asset names use **lowercase with underscores**: `tinyshakespeare`, `asv_nt_clean`
- Model or dataset families may retain **canonical names**: `glove.6B`
- Asset names should be **stable identifiers**, not file names
- Asset *kind* determines storage location (`text`, `embeddings`, `vision`, etc.)
- `relative_path` specifies the actual file used by code
- Derived datasets should indicate lineage (example: `asv_raw → asv_nt_clean`)

---

# Adding a New Asset

### 1. Write a builder

Example:

    def build_my_dataset():
        root = get_asset_home("text") / "my_dataset"
        ...

Builders handle:

- downloads
- extraction
- preprocessing
- file placement

---

### 2. Register the asset

Add an entry to `registry.py`:

    "my_dataset": Asset(
        name="my_dataset",
        kind="text",
        relative_path="my_dataset/data.txt",
        description="Example dataset",
        builder=build_my_dataset
    )

---

### 3. Use it

    ensure_asset("my_dataset")

---

# Typical Workflow

Clone your ML project:

    git clone ai_project
    cd ai_project

Install shared dataset utilities:

    pip install -e ../ai_shared_data

Run your code:

    python train_model.py

Missing assets download automatically on first use.

---

# Kaggle Assets

Some datasets require Kaggle authentication.

Place credentials in:

    ~/.kaggle/kaggle.json

or set environment variables:

    export KAGGLE_USERNAME=...
    export KAGGLE_KEY=...

You may also need to **accept dataset terms on the Kaggle website** before downloads will work.

---

# Notes

This repository intentionally **does not store datasets in Git**.

It only contains:

- download logic
- preprocessing scripts
- asset definitions

Datasets remain in the shared local directory.