import json
import tempfile
import os
import traceback
import pysimplicityhl

def create_temp_file(suffix="", directory=None, delete=True):
    """
    Create a temporary file with a user-defined suffix and directory.

    Parameters:
        suffix (str): File extension, e.g. ".txt" or ".csv".
        directory (str): Directory where the file should be created.
                         If None, the system temp directory is used.
        delete (bool): If True, the file will be deleted automatically
                       when the file object is closed.

    Returns:
        (filename, file_object): The absolute path and the file handle.
    """
    # Create the temporary file
    if not suffix.startswith("."):
        suffix = f".{suffix}"
    tmp = tempfile.NamedTemporaryFile(
        suffix=suffix,
        dir=directory,
        delete=delete
    )

    # Return the full path and the file object
    return tmp.name, tmp

def write_text_to_temp_file(text, suffix="", directory=None):
    """
    Create a temporary file, write text into it, and return the filename only.

    Parameters:
        text (str): The text content to write into the file.
        suffix (str): File extension, e.g. ".txt".
        directory (str): Directory where the file will be created.

    Returns:
        str: The full path of the created temporary file.
    """
    # Create the temporary file using the previously defined function
    filename, f = create_temp_file(suffix=suffix, directory=directory, delete=False)

    # Write the text into the file (convert to bytes)
    f.write(text.encode("utf-8"))
    f.flush()

    # Close the file handle (file remains on disk because delete=False)
    f.close()

    # Return only the filename
    return filename

import os
import platform

import os
import platform


import os
import platform
import traceback

def compile(code, witness=None, folder=None, delete_temp_files=True):
    """
    Compile using temporary files. Temporary files can optionally be deleted.
    On Windows, file paths are wrapped in extra quotes.
    The return value is always a dictionary.
    """

    # Result dictionary
    res = {}

    # Determine working folder
    _temp_folder = "."
    if folder is not None:
        if not os.path.exists(folder):
            # Folder does not exist -> warn and keep default
            res["warning"] = "Error: folder does not exist. - using default folder '.'"
        else:
            _temp_folder = folder

    # Create temp files
    cfile_given = False
    if code is not None and os.path.isfile(code):
        simf_file = code
        cfile_given = True
    elif code is None:
        res["warning"] = "Error: file doese not exist or code is empty.'"
        res["error"] = True
        res["status"] = "error"
        return res
    else:
        simf_file = write_text_to_temp_file(code, suffix=".simf", directory=_temp_folder)

    wit_file = None
    wfile_given = False
    if witness is not None and os.path.isfile(witness):
        wfile_given = True
        wit_file = witness
    elif witness is None:
        pass
    else:
        wit_file = write_text_to_temp_file(witness, suffix=".wit", directory=_temp_folder)

    # Detect Windows
    is_windows = platform.system().lower().startswith("win")

    # Build parameter list
    parameter = ["--debug"]
    parameter.append(f"'{simf_file}'" if is_windows else simf_file)
    if witness is not None:
        parameter.append(f"'{wit_file}'" if is_windows else wit_file)
    # if is_windows:
    #     parameter = ["--debug", f"'{simf_file}'", f"'{wit_file}'"]
    # else:
    #     parameter = ["--debug", simf_file, wit_file]

    # Convert list to string
    parameter_txt = " ".join(parameter)

    try:
        # Run compilation
        # NOTE: this assumes pysimplicityhl.run_from_python returns a dict
        ddd = json.loads(pysimplicityhl.run_from_python(parameter_txt))
        res.update(ddd)

    except Exception:
        traceback_str = traceback.format_exc()
        res["error"] = True
        res["traceback"] = traceback_str
        res["code_file"] = simf_file
        res["witness_file"] = wit_file
        res["deleted"] = False
        return res

    # Handle deletion of temp files
    if delete_temp_files:
        try:
            if os.path.isfile(simf_file) and not cfile_given:
                os.remove(simf_file)
            if wit_file and os.path.isfile(wit_file) and not wfile_given:
                os.remove(wit_file)
        except Exception:
            traceback_str = traceback.format_exc()
            res["warning"] = f"Warning: failed to delete temporary files:\n{traceback_str}"
            res["code_file"] = simf_file
            res["witness_file"] = wit_file
            res["deleted"] = False
        return res

    # If not deleting, return filenames
    res["code_file"] = simf_file
    res["witness_file"] = wit_file
    res["deleted"] = False
    return res


def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)  # delete file


def pretty_print_code(code, indent_step=2):
    """
    Pretty-print a heavily nested expression string.
    Rules:
      - Increase indent after '('
      - Decrease indent after ')'
      - Break lines at ';' only
      - Klammern do NOT create new lines
    """
    indent = 0
    i = 0
    n = len(code)
    result = ""
    while i < n:
        c = code[i]
        if c == '(':
            result += '('
            indent += indent_step
            i += 1
        elif c == ')':
            indent -= indent_step
            result += ')'
            i += 1
        elif c == ';':
            result += ';\n' + ' ' * indent
            i += 1
        else:
            result += c
            i += 1

    # Remove trailing spaces on each line
    return '\n'.join(line.rstrip() for line in result.split('\n'))


def envelope_with_quote(filename):
    """
    Envelopse the full path in 'filename' with single quotes
    """
    return f"'{filename}'"