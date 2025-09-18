import os
import shutil
from datetime import datetime
import schedule
import time

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        # Define what files go where
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.docx', '.doc', '.txt'],
            'PDFs': ['.pdf'],
            'Others': []
        }
    
    def get_file_category(self, file_extension):
        """Figure out where this file should go"""
        file_extension = file_extension.lower()
        
        for category, extensions in self.file_types.items():
            if file_extension in extensions:
                return category
        return 'Others'
    
    def create_folders(self, date_folder, file_category):
        """Make the folders we need: Date/FileType/"""
        full_path = os.path.join(self.folder_path, date_folder, file_category)
        
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"✅ Created: {date_folder}/{file_category}/")
        
        return full_path
    
    def should_ignore_file(self, filename):
        """Skip files we don't want to move"""
        ignore_list = ['.', 'Thumbs.db', 'file_organizer.py', 'requirements.txt']
        return any(filename.startswith(ignore) for ignore in ignore_list)
    
    def organize_files(self):
        """The main work - organize all files"""
        print(f"🔍 Looking in: {self.folder_path}")
        
        try:
            # Get today's date for folder name
            today = datetime.now().strftime("%Y-%m-%d")
            
            # Find all files in the main folder only
            all_items = os.listdir(self.folder_path)
            files = [f for f in all_items if os.path.isfile(os.path.join(self.folder_path, f))]
            
            if not files:
                print("📂 No files found")
                return
            
            moved_count = 0
            
            for filename in files:
                # Skip files we don't want to touch
                if self.should_ignore_file(filename):
                    continue
                
                # Get file info
                file_path = os.path.join(self.folder_path, filename)
                _, extension = os.path.splitext(filename)
                category = self.get_file_category(extension)
                
                # Create destination folder
                destination_folder = self.create_folders(today, category)
                new_location = os.path.join(destination_folder, filename)
                
                # Move the file
                try:
                    shutil.move(file_path, new_location)
                    print(f"📁 {filename} → {today}/{category}/")
                    moved_count += 1
                except Exception as e:
                    print(f"❌ Couldn't move {filename}: {e}")
            
            print(f"✅ Moved {moved_count} files!")
                
        except Exception as e:
            print(f"❌ Error: {e}")

# Main program starts here
if __name__ == "__main__":
    # Your folder path
    FOLDER_PATH = "E:\\FileOrganizer"
    
    # Create organizer
    organizer = FileOrganizer(FOLDER_PATH)
    
    print("🚀 File Organizer Starting...")
    
    # Run once right now
    organizer.organize_files()
    
    # Set up to run every minute
    schedule.every(1).minutes.do(organizer.organize_files)
    
    print("⏰ Now checking every minute. Press Ctrl+C to stop.")
    
    # Keep running
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopped!")