import sys

from ai_shared_data.registry import DATASETS
from ai_shared_data.fetch import ensure_asset, get_asset_path


def list_datasets():
    for name, ds in DATASETS.items():
        desc = ds.description or ""
        print(f"{name:20} {ds.relative_path:40} {desc}")


def show_path(name):
    path = get_asset_path(name)
    print(path)

def check_dataset(name):
    try:
        path = ensure_asset(name)
        print(f"OK: {name}")
        print(path)
    except KeyError:
        print(f"Unknown dataset: {name}")
        sys.exit(1)
    except FileNotFoundError as exc:
        print(str(exc))
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Commands:")
        print("  list")
        print("  path <dataset>")
        return

    cmd = sys.argv[1]

    if cmd == "list":
        list_datasets()
    elif cmd == "path":
        if len(sys.argv) < 3:
            print("Usage: python -m ai_shared_data path <dataset>")
            return
        show_path(sys.argv[2])
    elif cmd == "check":
        if len(sys.argv) < 3:
            print("Usage: ai-data check <dataset>")
            return
        check_dataset(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
