
from pathlib import Path
import shutil
import logging

# File extensions mapped to their categories
FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".xlsx", ".csv", ".pptx"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".cpp", ".json"},
}


def get_category(file_path: Path) -> str:
    """Return the category for a file based on its extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination: Path) -> Path:
    """Find a destination name that will not overwrite an existing file."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1


def organize_files(folder: Path, dry_run: bool = True) -> dict:
    """
    Preview or organize files in a folder.

    dry_run=True previews changes without moving files.
    dry_run=False performs the moves.
    """
    folder = Path(folder).resolve()

    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")

    results = {
        "scanned": 0,
        "organized": 0,
        "skipped": 0,
        "errors": [],
        "actions": [],
    }

    for file_path in folder.iterdir():
        # Process only files directly inside the selected folder.
        if not file_path.is_file():
            continue

        results["scanned"] += 1
        category = get_category(file_path)
        destination_folder = folder / category
        destination = get_unique_path(destination_folder / file_path.name)

        if dry_run:
            results["actions"].append({
                "source": str(file_path),
                "destination": str(destination),
                "category": category,
                "status": "preview",
            })
            continue

        try:
            destination_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(destination))

            results["organized"] += 1
            results["actions"].append({
                "source": str(file_path),
                "destination": str(destination),
                "category": category,
                "status": "organized",
            })

        except OSError as error:
            results["errors"].append({
                "file": str(file_path),
                "error": str(error),
            })
            logging.exception("Failed to organize %s", file_path)

    return results
