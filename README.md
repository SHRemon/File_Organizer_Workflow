# 📁 Automated File Organizer

**A smart Python script that automatically organizes files by date and type with continuous monitoring.**

## 📋 Overview

This project automatically:
- Detects file types (.jpg, .docx, .pdf, .txt, .png, etc.)
- Creates an organized folder structure by date and file type
- Monitors the folder every minute for new files
- Safely ignores system files and hidden files
- Provides real-time console feedback

## ✨ Features

- **🔍 Smart Detection**: Automatically identifies file types and categories  
- **📁 Auto Organization**: Creates `/YYYY-MM-DD/FileType/` structure  
- **⏰ Live Monitoring**: Checks for new files every minute  
- **🛡️ Safe Operation**: Never touches system files or the script itself  
- **📊 Clean Output**: Professional console messages with progress tracking  
- **⚙️ Easy Customization**: Simple configuration for new file types  

## 🛠️ Installation

### Prerequisites
- Python 3.11.9 (Recommended)  
- Works on Windows, Mac, and Linux  

### Step 1: Clone the Repository
```bash
git clone https://github.com/SHRemon/File-Organizer.git
cd File-Organizer
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Organizer
```bash
python file_organizer.py
```

## 📂 Project Structure

```
FileOrganizer/
│
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── file_organizer.py         # Main organizer script
└── YYYY-MM-DD/              # Generated organized folders
    ├── Images/
    ├── Documents/
    ├── PDFs/
    └── Others/
```

## 🚀 Quick Start

### Method 1: Default Run (Recommended)
```bash
python file_organizer.py
```
This will organize existing files and start continuous monitoring.

### Method 2: Test with Sample Files
1. Create test files: `photo.jpg`, `document.docx`, `file.pdf`  
2. Run the script  
3. Watch files get organized automatically!  

## 📊 Output Structure

Example folder layout:
```
FileOrganizer/
├── 2025-09-18/
│   ├── Images/
│   │   ├── vacation.jpg
│   │   └── screenshot.png
│   ├── Documents/
│   │   ├── report.docx
│   │   └── notes.txt
│   ├── PDFs/
│   │   └── manual.pdf
│   └── Others/
│       └── unknown.xyz
└── file_organizer.py
```

### Console Output Example
```
🚀 File Organizer Starting...
🔍 Looking in: E:\FileOrganizer
✅ Created: 2025-09-18/Images/
📁 photo.jpg → 2025-09-18/Images/
📁 document.docx → 2025-09-18/Documents/
✅ Moved 2 files!
⏰ Now checking every minute. Press Ctrl+C to stop.
```

## ⚙️ Configuration

### Supported File Types
| Category   | Extensions |
|------------|------------|
| **Images** | .jpg, .jpeg, .png, .gif, .bmp |
| **Documents** | .docx, .doc, .txt |
| **PDFs**   | .pdf |
| **Others** | All unrecognized file types |

### Customization Options
- **Add New File Categories**: Edit the `file_types` dictionary in `file_organizer.py`
```python
self.file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.docx', '.doc', '.txt'],
    'Videos': ['.mp4', '.avi', '.mov'],  # New category
    'PDFs': ['.pdf'],
    'Others': []
}
```

- **Change Monitoring Frequency**: Adjust the schedule interval
```python
schedule.every(5).minutes.do(organizer.organize_files)  # Every 5 minutes
```

## 🔧 Troubleshooting

### Common Issues
- **Files not moving** → Ensure they aren’t open in other programs  
- **Permission denied** → Run as admin (Windows) or use `sudo` (Mac/Linux)  
- **Script stops unexpectedly** → Check if folder path exists and is accessible  

### Debug Tips
- Hidden/system files are ignored automatically  
- The script file itself is never moved  

## 🧪 Testing

Quick test steps:
1. Place files: `test.jpg`, `document.docx`, `file.pdf`  
2. Run:  
   ```bash
   python file_organizer.py
   ```
3. Expected: Files organized into `/Date/FileType/`  
4. Add a new file while running → auto-organized within 1 minute  

## 📦 Dependencies

Core libraries used:
- `schedule` – Task scheduling  
- Built-in: `os`, `shutil`, `datetime`  

## 📞 Support
- 📧 Email: remonshahariar@gmail.com  
- 📖 Documentation: This README file  

## 👨‍💻 Created By
**Shahariar Hossain Remon**  
📧 Email: remonshahariar@gmail.com  

## 🙏 Acknowledgments
- Python `schedule` library  
- Built-in Python modules for file operations  
- Night Shift AI/Automation Engineers Team – Assignment 2  

---

**⭐ Star this repository if you find it useful!**  
**Made with ❤️ for automated file organization**
