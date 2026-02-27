import os
import shutil

def organize_folder(folder_path):
    # This dictionary maps the target folder names to the file extensions they should hold
    extensions_map = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        "Videos": ['.mp4', '.mkv', '.avi', '.mov'],
        "Audio": ['.mp3', '.wav', '.aac'],
        "Archives": ['.zip', '.rar', '.tar.gz'],
        "Installers": ['.exe', '.msi']
    }

    # Verify the provided folder path actually exists
    if not os.path.exists(folder_path):
        print(f"Error: The path '{folder_path}' does not exist.")
        return

    print(f"Organizing files in: {folder_path}...\n")

    # Loop through every single item in the target folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # We only want to move files, not folders that are already there
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            # Check our dictionary to see where this file belongs
            for folder_name, extensions in extensions_map.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    
                    # Create the category folder if it doesn't exist yet
                    os.makedirs(target_folder, exist_ok=True)

                    # Move the file and print a status update
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} -> {folder_name}/")
                    moved = True
                    break

            # If the file extension isn't in our list, drop it in an 'Others' folder
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved: {filename} -> Others/")

    print("\nOrganization complete! Ready for GitHub. ⭐")

if __name__ == "__main__":
    # IMPORTANT: Change this path to a messy folder on your computer to test it out!
    # Example: "C:/Users/YourName/Downloads" (Use forward slashes)
    target_directory = "C:/Users/J SAM JUDSON/Desktop/Messy_Test" 
    organize_folder(target_directory)