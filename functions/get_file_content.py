import os
from functions.config import char_limit


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file, "r") as f:
            content = f.read()
            if len(content) > char_limit:
                return content[:char_limit]
            return content
    except Exception as e:
        return f'Error: Failed to read file: "{file_path}" - {str(e)}'