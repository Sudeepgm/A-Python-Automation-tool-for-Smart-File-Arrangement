import os
import shutil

# Change this to your target folder (e.g., Downloads)
TARGET_FOLDER = "/path/to/your/Downloads"

# Define file type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Documents/PDFs': ['.pdf'],
    'Documents/Word': ['.docx', '.doc'],
    'Archives': ['.zip', '.rar'],
    'Scripts': ['.py', '.js', '.sh']
}

def organize_folder():
    for file in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    dest_folder = os.path.join(TARGET_FOLDER, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break

            if not moved:
                misc_folder = os.path.join(TARGET_FOLDER, 'Misc')
                os.makedirs(misc_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(misc_folder, file))

if __name__ == "__main__":
    organize_folder()
