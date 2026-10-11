
# SWYNEX Smart File Organizer

A Python-based file organization automation tool developed as part of the SWYNEX Python Internship.

## Overview

The Smart File Organizer scans a selected folder and categorizes files by their extensions. It supports preview mode, duplicate filename protection, JSON reports, and application logging.

## Features

- Automatically categorizes files into folders.
- Supports images, documents, videos, audio, archives, code, and other files.
- Preview mode lets users review planned changes before moving files.
- Prevents overwriting files when duplicate names exist.
- Generates a JSON report of each run.
- Records application errors in a log file.
- Includes automated unit tests.
- Uses Python's standard library; no paid APIs or external packages are required.

## Project Structure

```text
SWYNEX-Python-Automation-Tool/
├── src/
│   ├── main.py
│   └── file_organizer.py
├── tests/
│   └── test_file_organizer.py
├── sample_files/
├── reports/
├── logs/
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- Windows, macOS, or Linux

## Setup

Clone or download this repository, then open a terminal in the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No additional packages are required.

## Usage

### 1. Preview file organization

Preview the changes without moving files:

```bash
python src/main.py --folder sample_files
```

### 2. Apply file organization

After reviewing the preview, run:

```bash
python src/main.py --folder sample_files --apply
```

**Warning:** Apply mode moves files into category folders inside the selected directory. Test with sample files before using a folder containing important personal data.

### 3. Run automated tests

```bash
python -m unittest discover -s tests -v
```

## Reports and Logs

- `reports/organization_report.json` stores the latest run's results.
- `logs/organizer.log` records application errors.

These generated files are excluded from Git by `.gitignore`.

## Technologies

- Python
- pathlib
- argparse
- shutil
- logging
- JSON
- unittest
- Git and GitHub

## Learning Outcomes

This project demonstrates file handling, command-line interfaces, exception handling, safe file operations, logging, report generation, and automated testing.

## Internship Context

Developed as a practical automation project for the SWYNEX Python Internship.

## Disclaimer

Use preview mode first and keep backups of important files before applying file organization.
