import inspect
import os

import mypylib
from mypylib.mypylib.auxiliars import strip_line_with_content
from mypylib.mypylib.collections import create_new_collection

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

def add_function(function_name, source_code, module, collection=""):
    base_path = mypylib.__path__[0]
        
    collection_folder = base_path
    words = collection.split('.')
    for word in words:
        collection_folder = os.path.join(collection_folder, word)
    
    if collection != "":
        create_new_collection(collection, base_path, package_name="mypylib")
        pass
    
    module_path = os.path.join(collection_folder,  module + ".py")
    with open(module_path, "a") as file:
        file.write("\n\n" + source_code + "\n\n")
        
    init_file_path = os.path.join(collection_folder, "__init__.py")
    update_init_file(init_file_path, module, function_name)

## DECORATOR
def add(collection="", module="main", package_name = "mypylib"):
    def decorator(func):
        source_code = inspect.getsource(func)
        source_code = strip_line_with_content(source_code, "@mypylib.add")
        add_function(func.__name__, source_code, module, collection)
        
        return func
    return decorator