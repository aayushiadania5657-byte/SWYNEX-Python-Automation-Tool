
import tempfile
import unittest
from pathlib import Path

from src.file_organizer import get_category, get_unique_path, organize_files


class TestFileOrganizer(unittest.TestCase):

    def test_file_category(self):
        self.assertEqual(get_category(Path("photo.JPG")), "Images")
        self.assertEqual(get_category(Path("notes.txt")), "Documents")
        self.assertEqual(get_category(Path("song.mp3")), "Audio")
        self.assertEqual(get_category(Path("unknown.xyz")), "Others")

    def test_duplicate_filename(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            folder = Path(temporary_folder)
            existing_file = folder / "photo.jpg"
            existing_file.touch()

            unique_path = get_unique_path(existing_file)

            self.assertEqual(unique_path.name, "photo_1.jpg")
            self.assertTrue(existing_file.exists())

    def test_preview_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            folder = Path(temporary_folder)
            sample_file = folder / "notes.txt"
            sample_file.write_text("Test content", encoding="utf-8")

            results = organize_files(folder, dry_run=True)

            self.assertEqual(results["scanned"], 1)
            self.assertEqual(results["organized"], 0)
            self.assertTrue(sample_file.exists())
            self.assertEqual(results["actions"][0]["status"], "preview")

    def test_missing_folder_raises_error(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            missing_folder = Path(temporary_folder) / "does_not_exist"

            with self.assertRaises(FileNotFoundError):
                organize_files(missing_folder)


if __name__ == "__main__":
    unittest.main()
