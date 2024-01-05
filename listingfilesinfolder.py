import os

def list_files_in_folder(folder):
    for root, directories, files in os.walk(folder):
        print(f"Folder: {root}")
        if files:
            print("Files:")
            for file in files:
                print(f"\t- {file}")
        else:
            print("This folder doesn't contain any files.")
        print("\n")

# there you write the folder 
folder_path = "Path\\to\\folder"

list_files_in_folder(folder_path)