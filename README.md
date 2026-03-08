# ai_shared_data

Shared dataset utilities for my machine learning and mechanistic interpretability projects.

This repository provides:

- A **common location for datasets**
- Utilities for **downloading and preparing data**
- A consistent way for other repositories to **locate datasets**

The goal is to avoid duplicating dataset scripts across multiple repositories.

---

# Design

Datasets are stored in a single shared directory on the local machine.

Default location:

```
~/src/data
```

This location can be overridden using an environment variable:

```
export AI_DATA_HOME=/path/to/data
```

All projects import this repository to:

- locate datasets
- download datasets if missing
- generate derived datasets

---

# Directory Layout

Example structure after datasets are installed:

```
~/src/
    ai_shared_data/
        ai_shared_data/
            paths.py
            fetch.py
            registry.py
        README.md

    data/
        
```

This keeps **large files outside project repositories**.

---

# Installing

Clone the repository and install it in editable mode:

```
git clone https://github.com/<user>/ai_shared_data.git
cd ai_shared_data
pip install -e .
```

Editable installation allows updates without reinstalling.

---

# Using From Another Repository

Example usage inside another project:

```python
from ai_shared_data.fetch import ensure_dataset
from ai_shared_data.paths import get_data_path

ensure_dataset("asv_nt_clean")

ASV_PATH = get_data_path("asv_nt_clean")
```

`ensure_dataset()` will download or generate the dataset if it does not exist.

---

# Available Datasets

Example registry:

| dataset | description |
|--------|-------------|
| `the_verdict` | short text used in "LLM from Scratch" examples |
| `asv_raw` | American Standard Version Bible |
| `asv_nt_clean` | cleaned New Testament version used for language modeling |
| `tinyshakespeare` | common small dataset used for character models |

Datasets are defined in:

```
ai_shared_data/registry.py
```

---

# Adding a Dataset

1. Add a dataset definition in `registry.py`

Example:

```python
ASSETS["asv_raw"] = {
    "url": "...",
    "target": "asv/asv.txt"
}
```

2. Add a builder function if preprocessing is required.

Example:

```
asv_raw  ->  asv_nt_clean
```

3. Update documentation if useful.

---

# Why This Exists

Originally, each repository contained:

- duplicated data pull scripts
- duplicated `DATA_PATH` utilities

This created maintenance problems.

This repository centralizes dataset logic so that:

- fixes happen in one place
- datasets are stored once
- repositories remain lightweight

---

# Typical Workflow

```
git clone ai_project
pip install -e ../ai_shared_data
python script.py
```

Datasets will automatically download on first use.

---

# Notes

This repository intentionally **does not store large datasets in Git**.  
It only contains **code describing how to obtain them**.
