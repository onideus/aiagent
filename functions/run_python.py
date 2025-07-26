import os
import subprocess
from subprocess import TimeoutExpired


def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File "{file_path}" not found.'

    if not target_file.lower().endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = ['python', target_file] + args
        result = subprocess.run(command,
                                cwd=working_directory,
                                capture_output=True,
                                text=True,
                                check=True,
                                timeout=30)
        if not result.stdout.strip():
            return "No output produced."
        return f"STDOUT:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        output = []
        if e.stdout:
            output.append(f"STDOUT:\n{e.stdout}")
        if e.stderr:
            output.append(f"STDERR:\n{e.stderr}")
        output.append(f"Process exited with code {e.returncode}")
        return "\n".join(output)
    except TimeoutExpired:
        return f'Error: Execution timed out after 30 seconds'
    except Exception as e:
        return f"Error: executing Python file: {e}"
