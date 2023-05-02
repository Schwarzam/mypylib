import os
import shutil

def remove_folder(folder_path):
    """
    Removes a folder and all its contents.
    """
    shutil.rmtree(folder_path)

def get_last_folder_name(folder_path):
    """
    Gets the name of the last folder in the given path.
    """
    return os.path.basename(os.path.normpath(folder_path))

def extract_folder_hierarchy(folder_path):
    """
    Extracts the folder hierarchy from the given folder path.
    """
    # Split the folder path into individual folder names
    folder_names = folder_path.split(os.path.sep)

    # Remove empty folder names
    folder_names = [name for name in folder_names if name]

    # Create a list of folder paths for each level of the hierarchy
    folder_paths = []
    current_path = '/'
    for folder_name in folder_names:
        current_path = os.path.join(current_path, folder_name)
        folder_paths.append(current_path)

    return folder_paths

def extract_subfolder_path2mod(full_path, base_path):
    """
    Extracts the path of a subfolder from a full path, relative to a base path.
    """
    rel_path = os.path.relpath(full_path, base_path)
    return '.'.join(rel_path.split(os.path.sep))

def strip_line_with_content(string, content):
    """
    Strips the lines in a string that contain the specified content.
    """
    lines = string.splitlines()
    stripped_lines = [line for line in lines if content not in line]
    return '\n'.join(stripped_lines)