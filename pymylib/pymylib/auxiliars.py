import os
import shutil
import ast

def remove_function_from_file(file_path, function_name):
    """Removes a function definition from a Python file by name.

    Parameters
    ----------
    file_path : str
        The file path of the Python file.
    function_name : str
        The name of the function to remove.

    Raises
    ------
    ValueError
        If the function is not found in the file.

    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the line numbers corresponding to the function definition
    function_start = None
    function_end = None
    for i, line in enumerate(lines):
        if line.startswith('def ' + function_name):
            function_start = i
            continue
        if function_start is not None and line.startswith('def '):
            function_end = i
            break
    if function_start is None:
        raise ValueError('Function not found in file')
    
    # Remove the lines corresponding to the function definition
    del lines[function_start:function_end]

    # Write the modified file contents back to disk
    with open(file_path, 'w') as file:
        file.write(''.join(lines))

def file_contains_function(file_path, function_name):
    """Checks if a Python file contains a function with the specified name.

    Parameters
    ----------
    file_path : str
        The file path of the Python file.
    function_name : str
        The name of the function to check.

    Returns
    -------
    bool
        True if the file contains the function, False otherwise.

    """
    with open(file_path, 'r') as file:
        source = file.read()
        tree = ast.parse(source)

        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == function_name:
                return True

        return False
    
def remove_folder(folder_path):
    """Removes a folder and all its contents.

    Parameters
    ----------
    folder_path : str
        The file path of the folder to remove.

    """
    shutil.rmtree(folder_path)

def get_last_folder_name(folder_path):
    """Gets the name of the last folder in the given path.

    Parameters
    ----------
    folder_path : str
        The file path of the folder.

    Returns
    -------
    str
        The name of the last folder in the given path.

    """
    return os.path.basename(os.path.normpath(folder_path))

def extract_folder_hierarchy(folder_path):
    """Extracts the folder hierarchy from the given folder path.

    Parameters
    ----------
    folder_path : str
        The file path of the folder.

    Returns
    -------
    list of str
        A list of folder paths for each level of the hierarchy.

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
    """Extracts the path of a subfolder from a full path, relative to a base path.

    Parameters
    ----------
    full_path : str
        The full file path of the subfolder.
    base_path : str
        The file path of the base folder.

    Returns
    -------
    str
        The path of the subfolder as a module path.

    """
    rel_path = os.path.relpath(full_path, base_path)
    return '.'.join(rel_path.split(os.path.sep))

def strip_line_with_content(string, content):
    """Strips lines in a string that contain the specified content.

    Parameters
    ----------
    string : str
        The string to strip.
    content : str
        The content to search for in each line.

    Returns
    -------
    str
        The stripped string.

    """
    lines = string.splitlines()
    stripped_lines = [line for line in lines if content not in line]
    return '\n'.join(stripped_lines)
