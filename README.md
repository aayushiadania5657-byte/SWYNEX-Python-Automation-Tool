
# SWYNEX Smart File Organizer

A Python-based file organization automation tool developed as part of the SWYNEX Python Internship.

## Overview

The Smart File Organizer scans a selected folder and categorizes files by their extensions. It supports preview mode, duplicate filename protection, JSON reports, application logging, and automated tests.

## Features

- Automatically categorizes files into folders.
- Supports images, documents, videos, audio, archives, code, and other files.
- Preview mode lets users review planned changes before moving files.
- Prevents overwriting files when duplicate names exist.
- Generates a JSON report of each run.
- Records run summaries and application errors in a log file.
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
├── demo_input/
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

Preview the planned changes without moving files:

```bash
python src/main.py --folder demo_input
```

### 2. Apply file organization

After reviewing the preview, organize the files:

```bash
python src/main.py --folder demo_input --apply
```

**Demo note:** The `demo_input` folder contains example files for testing. The file named `project_report.pdf` is a text placeholder used to demonstrate extension-based categorization, not a valid PDF document. Preview mode does not move files; `--apply` moves them into category folders.

**Safety warning:** Test with sample files first and keep backups before organizing a folder containing important personal data.

### 3. Run automated tests

```bash
python -m unittest discover -s tests -v
```

## Reports and Logs

- `reports/organization_report.json` stores the latest run's results.
- `logs/organizer.log` records run summaries and application errors.

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
