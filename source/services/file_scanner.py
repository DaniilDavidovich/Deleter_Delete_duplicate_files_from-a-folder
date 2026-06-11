# source/services/file_scanner.py
import os

def find_files(folder_path: str, file_names: list[str]) -> list[str]:
    found = []
    names_set = set(file_names)
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file in names_set:
                found.append(os.path.join(root, file))
    return found