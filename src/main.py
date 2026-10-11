
from pathlib import Path
import argparse
import json
import logging

from file_organizer import organize_files


def setup_logging(log_folder: Path) -> None:
    """Configure a log file for the application."""
    log_folder.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_folder / "organizer.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )


def save_report(results: dict, report_folder: Path) -> Path:
    """Save the operation results as a JSON report."""
    report_folder.mkdir(parents=True, exist_ok=True)

    report_path = report_folder / "organization_report.json"
    report_path.write_text(
        json.dumps(results, indent=4),
        encoding="utf-8",
    )

    return report_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Safely organize files into categories."
    )
    parser.add_argument(
        "--folder",
        type=Path,
        required=True,
        help="Folder whose files you want to organize.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files. Without this option, preview only.",
    )

    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    setup_logging(project_root / "logs")

    try:
        results = organize_files(
            args.folder,
            dry_run=not args.apply,
        )
        logging.info(
            "Run completed: mode=%s folder=%s scanned=%s organized=%s errors=%s",
            "apply" if args.apply else "preview",
            args.folder.resolve(),
            results["scanned"],
            results["organized"],
            len(results["errors"]),
        )

        print("\n=== SWYNEX SMART FILE ORGANIZER ===")
        print(f"Mode: {'ORGANIZE' if args.apply else 'PREVIEW'}")
        print(f"Files scanned: {results['scanned']}")

        for action in results["actions"]:
            print(
                f"[{action['status'].upper()}] "
                f"{Path(action['source']).name} -> "
                f"{action['category']}"
            )

        if args.apply:
            print(f"Files organized: {results['organized']}")

        if results["errors"]:
            print(f"Errors: {len(results['errors'])}")
            for error in results["errors"]:
                print(f"- {error['file']}: {error['error']}")

        report_path = save_report(
            results,
            project_root / "reports",
        )
        print(f"\nReport saved to: {report_path}")

    except (OSError, ValueError) as error:
        logging.exception("The organizer could not complete the operation.")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
