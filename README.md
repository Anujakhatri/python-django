# Auto File Organizer

A simple Python package to organize files into folders based on file type.

## Features
- Organizes files into categories (Images, Documents, Videos, etc.)
- Handles duplicate file names automatically
- Easy to use

## Installation
pip install pyinstaller
pip install setuptools wheel twine
python setup.py sdist bdist_wheel

## Usuage
from automation import FileOrganizer


Step 7: Usage Example
from automation.organizer import FileOrganizer

organizer = FileOrganizer()
result = organizer.organize(r"C:\Users\anujakhatri\Downloads")
print(result)