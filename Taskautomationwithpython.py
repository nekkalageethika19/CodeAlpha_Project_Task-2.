import os
import shutil

# Define the directory you want to organize
source_dir = "C:/path/to/your/folder"

# Define target folders for different file types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Others": []
}

# Function to create folders if they don't exist
def create_folders():
    for folder in file_types.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to organize files by their types
def organize_files():
    for filename in os.listdir(source_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        # Check each file type and move accordingly
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, folder, filename))
                moved = True
                break

        # Move to "Others" if no matching extension is found
        if not moved and file_ext:
            shutil.move(os.path.join(source_dir, filename), os.path.join(source_dir, "Others", filename))

# Main function
if __name__ == "__main__":
    create_folders()
    organize_files()
    print(f"Files in '{source_dir}' have been organized by type.")