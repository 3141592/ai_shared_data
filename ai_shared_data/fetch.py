from pathlib import Path

from ai_shared_data.paths import get_data_home
from ai_shared_data.registry import DATASETS

def dataset_exists(name: str) -> bool:
    try:
        path = get_dataset_path(name)
    except KeyError:
        return False
    return path.exists()


def get_dataset_path(name: str) -> Path:
    """
    Return the full filesystem path for a dataset.

    Raises KeyError if the dataset name is not registered.
    """
    dataset = DATASETS[name]
    return get_data_home() / dataset.relative_path


def ensure_dataset(name: str) -> Path:
    """
    Ensure the dataset exists locally.

    Returns the dataset path if found.
    Raises FileNotFoundError if the dataset is missing.
    """
    path = get_dataset_path(name)

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset '{name}' not found at {path}\n"
            f"Expected location: {path}\n"
            f"Check that the dataset has been downloaded or created."
        )

    return path
