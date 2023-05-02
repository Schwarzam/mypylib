import inspect
import os

import pymylib
from pymylib.pymylib.auxiliars import strip_line_with_content, file_contains_function, remove_function_from_file
from pymylib.pymylib.collections import create_new_collection

def remove_function(function_name, collection="", module_name="main"):
    """Removes a function from a Python module and its corresponding import statement from a collection's __init__.py file.

    Parameters
    ----------
    function_name : str
        The name of the function to remove.
    collection : str, optional
        The name of the collection that contains the module to modify (default is "").
    module_name : str, optional
        The name of the module to modify (default is "main").

    """
    base_path = pymylib.__path__[0]
        
    collection_folder = base_path
    words = collection.split('.')
    for word in words:
        collection_folder = os.path.join(collection_folder, word)

    import_line = f"from .{module_name} import {function_name}"
    
    init_filepath = os.path.join(collection_folder, "__init__.py")
    with open(init_filepath, 'r') as init_file:
        lines = init_file.readlines()

    new_lines = []
    for line in lines:
        if not import_line in line:
            new_lines.append(line)

    with open(init_filepath, 'w') as init_file:
        init_file.writelines(new_lines)
    
    module_filepath = os.path.join(collection_folder, module_name + ".py")
    remove_function_from_file(module_filepath, function_name)


def update_init_file(init_file_path, module_name, function_name):
    """Updates a collection's __init__.py file with an import statement for a given function.

    Parameters
    ----------
    init_file_path : str
        The path to the __init__.py file to modify.
    module_name : str
        The name of the module to import the function from.
    function_name : str
        The name of the function to import.

    """
    # Read the contents of the __init__.py file
    with open(init_file_path, 'r') as init_file:
        lines = init_file.readlines()

    # Check if the function is already imported
    import_line = f"from .{module_name} import {function_name}"
    import_found = False

    for line in lines:
        if import_line in line:
            import_found = True
            break

    # If not, append the import statement to the file
    if not import_found:
        with open(init_file_path, 'a') as init_file:
            init_file.write(f"{import_line}\n")

def add_function(function_name, source_code, module, collection="", overwrite=False, base_path=pymylib.__path__[0]):
    """Adds a function to a Python module and updates its corresponding import statement in a collection's __init__.py file.

    Parameters
    ----------
    function_name : str
        The name of the function to add.
    source_code : str
        The source code of the function to add.
    module : str
        The name of the module to add the function to.
    collection : str, optional
        The name of the collection to add the module to (default is "").
    overwrite : bool, optional
        Whether to overwrite an existing function with the same name (default is False).
    base_path : str, optional
        The base path of the pymylib package (default is pymylib.__path__[0]).

    Raises
    ------
    Exception
        If the function already exists in the specified module and overwrite is False.

    """
    collection_folder = base_path
    words = collection.split('.')
    for word in words:
        collection_folder = os.path.join(collection_folder, word)
    
    if collection != "":
        create_new_collection(collection, base_path, package_name="pymylib")
    
    module_path = os.path.join(collection_folder, module + ".py")

    try:
        if file_contains_function(module_path, function_name):
            if not overwrite:
                raise Exception(f"The function {function_name} already exists in the {collection} {module}. If you want to overwrite it, set overwrite=True.")
            else:
                remove_function_from_file(module_path, function_name)
    except:
        pass

    with open(module_path, "a") as file:
        file.write("\n" + source_code + "\n")
        
    init_file_path = os.path.join(collection_folder, "__init__.py")
    update_init_file(init_file_path, module, function_name)


## DECORATOR
def add(collection="", module="main", overwrite=False):
    """Decorator that adds a function to a module and its corresponding import statement to a collection's __init__.py file.

    Parameters
    ----------
    collection : str, optional
        The name of the collection to add the module and function to (default is "").
    module : str, optional
        The name of the module to add the function to (default is "main").
    overwrite : bool, optional
        Whether to overwrite an existing function with the same name (default is False).

    Returns
    -------
    function
        The decorated function.

    """
    package_name = "pymylib"
    base_path = pymylib.__path__[0]

    def decorator(func):
        source_code = inspect.getsource(func)
        source_code = strip_line_with_content(source_code, "@pymylib.add")
        add_function(func.__name__, source_code, module, collection, overwrite, base_path)
        
        return func
    return decorator
