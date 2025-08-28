import os
import shutil

# Main folder
folder = r"C:\Users\kubap\OneDrive\Pulpit\Studia"

# Main folders
main_folders = ["Documents", "Images", "Matlab", "Programming"]

# Create main folders if they don't exist
for name in main_folders:
    path = os.path.join(folder, name)
    if not os.path.exists(path):
        os.makedirs(path)

# Subfolders inside Documents
documents_subfolders = ["PDF", "Word", "Excel", "PowerPoint"]
for sub in documents_subfolders:
    path = os.path.join(folder, "Documents", sub)
    if not os.path.exists(path):
        os.makedirs(path)

# Dictionary mapping extensions to (main folder, subfolder)
file_types = {
    ".pdf": ("Documents", "PDF"),
    ".docx": ("Documents", "Word"),
    ".doc": ("Documents", "Word"),
    ".xlsx": ("Documents", "Excel"),
    ".csv": ("Documents", "Excel"),
    ".pptx": ("Documents", "PowerPoint"),
    ".jpg": ("Images", ""),
    ".png": ("Images", ""),
    ".mlx": ("Matlab", ""),
    ".slx": ("Matlab", ""),
    ".m": ("Matlab", ""),
    ".cpp": ("Programming", ""),
    ".py": ("Programming", ""),
}

# List only files (ignore folders)
list_of_docs = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

# Move files to correct folder/subfolder
for doc in list_of_docs:
    full_path = os.path.join(folder, doc)
    name, extension = os.path.splitext(doc)
    
    if extension in file_types:
        main_folder, sub_folder = file_types[extension]
        
        # Build destination path
        if sub_folder:
            destination_folder = os.path.join(folder, main_folder, sub_folder)
        else:
            destination_folder = os.path.join(folder, main_folder)
        
        # Create destination folder if it doesn't exist (just in case)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Move the file
        shutil.move(full_path, os.path.join(destination_folder, doc))
        
