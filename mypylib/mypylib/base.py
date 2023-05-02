import inspect
import os

import mypylib
from mypylib.mypylib.auxiliars import strip_line_with_content, file_contains_function, remove_function_from_file
from mypylib.mypylib.collections import create_new_collection

def remove_function(function_name, collection="", module_name="main"):
    base_path = mypylib.__path__[0]
        
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

def add_function(function_name, source_code, module, collection="", overwrite=False, base_path = mypylib.__path__[0]):    
    collection_folder = base_path
    words = collection.split('.')
    for word in words:
        collection_folder = os.path.join(collection_folder, word)
    
    
    if collection != "":
        create_new_collection(collection, base_path, package_name="mypylib")
        pass
    
    module_path = os.path.join(collection_folder,  module + ".py")


    if file_contains_function(module_path, function_name):
        if not overwrite:
            raise Exception(f"The function {function_name} already exists in the {collection} {module}. If you want to overwrite it, set overwrite=True.")
        else:
            remove_function_from_file(module_path, function_name)

    with open(module_path, "a") as file:
        file.write("\n" + source_code + "\n")
        
    init_file_path = os.path.join(collection_folder, "__init__.py")
    update_init_file(init_file_path, module, function_name)

## DECORATOR
def add(collection="", module="main", overwrite=False):
    package_name = "mypylib"
    base_path = mypylib.__path__[0]

    def decorator(func):
        source_code = inspect.getsource(func)
        source_code = strip_line_with_content(source_code, "@mypylib.add")
        add_function(func.__name__, source_code, module, collection, overwrite, base_path)
        
        return func
    return decorator