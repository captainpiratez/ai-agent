import os
import subprocess
import sys


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            [sys.executable, abs_file_path],
            cwd=abs_working_dir,
            timeout=30,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        output_parts = []
        if result.stdout.strip():
            output_parts.append(f"STDOUT:{result.stdout.strip()}")
        if result.stderr.strip():
            output_parts.append(f"STDERR:{result.stderr.strip()}")

        if output_parts:
            return "\n".join(output_parts)
        else:
            return "STDOUT: (no output)"

    except subprocess.TimeoutExpired as e:
        return f"Error: Execution timed out. {e}"
    except Exception as e:
        return f"Error: executing Python file: {e}"