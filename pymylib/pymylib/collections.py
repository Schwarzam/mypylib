import os

import pymylib
from pymylib.pymylib.auxiliars import get_last_folder_name, extract_folder_hierarchy, extract_subfolder_path2mod, remove_folder

def init_folder(folder, base_path, package_name="pymylib"):
    """Initializes a folder with an empty __init__.py file and adds an import statement to its parent folder's __init__.py file.

    Parameters
    ----------
    folder : str
        The path to the folder to initialize.
    base_path : str
        The base path of the pymylib package.
    package_name : str, optional
        The name of the package (default is "pymylib").

    """
    init_path = os.path.join(folder, "__init__.py")
    if not os.path.exists(init_path):
        open(init_path, "w")
    else:
        #Folder already has __init__.py
        return
    
    outside_folder = extract_folder_hierarchy(folder)[-2]
    outside_folder_init = os.path.join(outside_folder, "__init__.py")
    with open(outside_folder_init, 'r') as init_file:
        lines = init_file.readlines()
    
    # Check if the module is already imported
    mod_name = extract_subfolder_path2mod(folder, base_path)
    import_line = f"import {package_name}.{mod_name}"
    import_found = False

    for line in lines:
        if import_line in line:
            import_found = True
            break
    
    if not import_found:
        with open(outside_folder_init, 'a') as init_file:
            init_file.write(f"{import_line}\n")


def create_new_collection(collection_name, base_path, package_name="pymylib"):
    """Creates a new collection in the pymylib package.

    Parameters
    ----------
    collection_name : str
        The name of the collection to create.
    base_path : str
        The base path of the pymylib package.
    package_name : str, optional
        The name of the package (default is "pymylib").

    Raises
    ------
    ValueError
        If the collection name is equal to the package name.

    """
    # Split the collection name into individual words
    words = collection_name.split('.')
    for word in words:
        if word == package_name:
            raise ValueError(f"Collection name cannot be {package_name}")
    
    # Create the root folder for the collection
    root_folder = os.path.join(base_path, words[0])
    os.makedirs(root_folder, exist_ok=True)
    init_folder(root_folder, base_path, package_name)
    
    # Create subfolders for each word after the first
    current_folder = root_folder
    for word in words[1:]:
        current_folder = os.path.join(current_folder, word)
        os.makedirs(current_folder, exist_ok=True)
        init_folder(current_folder, base_path, package_name)

def remove_collection(collection_name, base_path=pymylib.__path__[0], package_name="pymylib"):
    """Removes a collection from the pymylib package.

    Parameters
    ----------
    collection_name : str
        The name of the collection to remove.
    base_path : str, optional
        The base path of the pymylib package (default is pymylib.__path__[0]).
    package_name : str, optional
        The name of the package (default is "pymylib").

    """
    if collection_name.strip() == "":
        raise ValueError("Collection name cannot be empty")
    
    words = collection_name.split('.')

    folder = base_path
    for word in words:
        folder = os.path.join(folder, word)

    outside_folder = extract_folder_hierarchy(folder)[-2]
    outside_folder_init = os.path.join(outside_folder, "__init__.py")
    with open(outside_folder_init, 'r') as init_file:
        lines = init_file.readlines()

    # Check if the module is already imported
    mod_name = extract_subfolder_path2mod(folder, base_path)
    import_line = f"import {package_name}.{mod_name}"
    import_found = False

    new_lines = []
    for line in lines:
        if not import_line in line:
            new_lines.append(line)

    with open(outside_folder_init, 'w') as init_file:
        init_file.writelines(new_lines)

    remove_folder(folder)
