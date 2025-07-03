# 📂 Automated File Organizer

A Python automation tool that organizes files in a folder (like Downloads) into subfolders based on their file type.

## 🔧 Technologies Used
- Python
- os
- shutil

## 🧠 How It Works
1. Set the target folder path.
2. The script checks each file's extension.
3. Files are moved into folders based on type (Images, PDFs, Word Docs, Videos, Archives, etc.)
4. Unmatched files go into a "Misc" folder.

## ▶️ How to Run
1. Update the TARGET_FOLDER path in `main.py`.
2. Run the script:
```bash
python main.py
```

## 📁 Example Folder Structure
```
Downloads/
├── Images/
├── Documents/
│   ├── PDFs/
│   └── Word/
├── Videos/
├── Archives/
└── Misc/
```

Customize file types and folders by editing the `FILE_TYPES` dictionary in `main.py`.
