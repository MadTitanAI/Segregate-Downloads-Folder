import os
import shutil
import pystray
from PIL import Image

def move_file(file_path, destination_folder):
    try:
        shutil.move(file_path, destination_folder)
        print(f"Moved {os.path.basename(file_path)} to {destination_folder}")
    except Exception as e:
        print(f"Error moving {os.path.basename(file_path)}: {e}")

def create_category_folders(downloads_folder):
    categories = ['Images', 'Documents', 'Videos', 'Music', 'Compressed', 'Others']
    for category in categories:
        folder_path = os.path.join(downloads_folder, category)
        os.makedirs(folder_path, exist_ok=True)

def segregate_downloads(icon, downloads_folder):
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            if file_extension in ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'):
                move_file(file_path, os.path.join(downloads_folder, "Images"))
            elif file_extension in ('.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'):
                move_file(file_path, os.path.join(downloads_folder, "Documents"))
            elif file_extension in ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'):
                move_file(file_path, os.path.join(downloads_folder, "Videos"))
            elif file_extension in ('.mp3', '.wav', '.flac', '.aac'):
                move_file(file_path, os.path.join(downloads_folder, "Music"))
            elif file_extension in ('.zip', '.rar', '.7z', '.tar', '.gz'):
                move_file(file_path, os.path.join(downloads_folder, "Compressed"))
            else:
                move_file(file_path, os.path.join(downloads_folder, "Others"))

def on_quit(icon, item):
    icon.stop()

def setup_system_tray(icon, downloads_folder):
    menu = (pystray.MenuItem("Segregate Downloads", lambda _: segregate_downloads(icon, downloads_folder)),
            pystray.MenuItem("Quit", on_quit))
    icon.menu = pystray.Menu(*menu)
    icon.run()

if __name__ == "__main__":
    downloads_folder = r"C:\Users\Jerush Vijay\Downloads"
    create_category_folders(downloads_folder)
    image = Image.open("C:\\Users\\Jerush Vijay\\Desktop\\Python Programs\\MyPrograms\\Projects\\FileManagement\\icons8-download-64.png")  # Replace with the path to your icon image
    icon = pystray.Icon("Segregate Downloads", image, "Segregate Downloads", menu=pystray.Menu())
    setup_system_tray(icon, downloads_folder)
