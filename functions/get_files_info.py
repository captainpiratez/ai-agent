import os

def get_files_info(working_directory, directory=None):
    # abs = os.path.abspath(os.path.join(working_directory,directory))
    # print(abs)
    if directory not in os.listdir(working_directory) or directory.startswith(".."):
        if directory != ".":
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory "{working_directory}"'
    if os.path.isfile(directory):
        return f'Error: "{directory}" is not a directory'
    
    result = []
    dir = os.path.join(working_directory,directory)
    for name in os.listdir(dir):
        file = os.path.join(dir,name)
        file_size = os.path.getsize(file)
        is_dir = os.path.isdir(file)
        result.append(f"- {name}: file_size={file_size} bytes, is_dir={is_dir}")
    return "\n".join(result)
    
    