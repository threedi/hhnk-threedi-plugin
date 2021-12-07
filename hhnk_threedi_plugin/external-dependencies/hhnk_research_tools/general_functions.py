from pathlib import Path


def ensure_file_path(filepath):
    """
    Functions makes sure all folders in a given file path exist. Creates them if they don't.
    """
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise e from None
