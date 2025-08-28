# File Organizer - Python Project

## Overview
This Python script automatically organizes files in a specified folder into categorized subfolders based on their file types. It is designed to help users keep their directories neat and structured, especially when dealing with large numbers of files.

---

## Features
- Automatically creates main folders if they don't exist:
  - `Documents`
  - `Images`
  - `Matlab`
  - `Programming`
- Creates subfolders inside `Documents` for specific file types:
  - `PDF` (.pdf)
  - `Word` (.doc, .docx)
  - `Excel` (.xlsx, .csv)
  - `PowerPoint` (.pptx)
- Moves files to the appropriate folder/subfolder based on their extension.
- Ignores folders, only processes files.
- Can be easily extended to include new file types and categories.

---

## Supported File Types
| Extension | Destination Folder |
|-----------|------------------|
| .pdf      | Documents/PDF     |
| .docx, .doc | Documents/Word  |
| .xlsx, .csv | Documents/Excel |
| .pptx     | Documents/PowerPoint |
| .jpg, .png | Images           |
| .mlx, .slx, .m | Matlab       |
| .cpp, .py | Programming      |

---

## How to Use
1. Set the path of the folder you want to organize in the `folder` variable:
```python
folder = r"C:\Path\To\Your\Folder"
