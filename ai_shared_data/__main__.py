import sys

from ai_shared_data.registry import ASSETS
from ai_shared_data.fetch import ensure_asset, get_asset_path


def list_datasets():
    for name, ds in ASSETS.items():
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

def check_all_assets():
    from ai_shared_data.registry import ASSETS
    from ai_shared_data.fetch import asset_exists, get_asset_path

    missing = []

    for name in sorted(ASSETS):
        path = get_asset_path(name)
        if path.exists():
            print(f"OK   {name:20} {path}")
        else:
            print(f"MISS {name:20} {path}")
            missing.append(name)

    if missing:
        print(f"\nMissing {len(missing)} asset(s).")
        return 1

    print("\nAll assets present.")
    return 0


def main():
    if len(sys.argv) < 2:
        print("Commands:")
        print("  list")
        print("  check-all")
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
    elif cmd == "check-all":
        sys.exit(check_all_assets())
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
