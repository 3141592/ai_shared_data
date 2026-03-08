from __future__ import annotations

import os
from pathlib import Path


DEFAULT_DATA_HOME = Path("~/src/data").expanduser()


def get_data_home() -> Path:
    """
    Return the root directory where shared datasets are stored.

    Priority:
    1. AI_DATA_HOME environment variable
    2. default: ~/src/data
    """
    env_value = os.environ.get("AI_DATA_HOME")
    if env_value:
        return Path(env_value).expanduser().resolve()
    return DEFAULT_DATA_HOME.resolve()


def ensure_data_home() -> Path:
    """
    Ensure the shared data root exists and return it.
    """
    data_home = get_data_home()
    data_home.mkdir(parents=True, exist_ok=True)
    return data_home


def get_path(*parts: str) -> Path:
    """
    Return a path under the shared data root.

    Example:
        get_path("interpretability", "asv.txt")
    """
    return get_data_home().joinpath(*parts)


def ensure_dir(*parts: str) -> Path:
    """
    Ensure a directory under the shared data root exists and return it.

    Example:
        ensure_dir("interpretability")
    """
    path = get_data_home().joinpath(*parts)
    path.mkdir(parents=True, exist_ok=True)
    return path
