import os

def change_filename():
    old_name = input("Enter current filename: ")
    new_name = input("Enter new filename: ")

    try:
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
    except FileNotFoundError:
        print("File not found!")
