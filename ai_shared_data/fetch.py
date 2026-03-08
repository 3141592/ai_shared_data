from pathlib import Path

from ai_shared_data.paths import get_asset_home
from ai_shared_data.registry import ASSETS


def asset_exists(name: str) -> bool:
    try:
        path = get_asset_path(name)
    except KeyError:
        return False
    return path.exists()


def get_asset_path(name: str) -> Path:
    """
    Return the full filesystem path for an asset.

    Raises KeyError if the asset name is not registered.
    """
    asset = ASSETS[name]
    return get_asset_home(asset.kind) / asset.relative_path


def ensure_asset(name: str) -> Path:
    """
    Ensure the asset exists locally.

    Returns the asset path if found.
    Raises FileNotFoundError if the asset is missing.
    """
    path = get_asset_path(name)

    if not path.exists():
        raise FileNotFoundError(
            f"Asset '{name}' not found at {path}\n"
            f"Expected location: {path}\n"
            f"Check that the asset has been downloaded or created."
        )

    return path
