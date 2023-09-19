import os
import random
import string


def complex_id_generator(char_len=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(abs(char_len)))


def apply_pyi_docstring():
    pyi_files = [f for f in os.listdir(".") if f.endswith(".pyi")]

    for pyi_file in pyi_files:
        py_file = pyi_file[:-1]
        if os.path.isfile(py_file):
            with open(pyi_file, "r") as pyi_file_obj:
                pyi_contents = pyi_file_obj.read()

            docstring_start = pyi_contents.find('"""')
            docstring_end = pyi_contents.rfind('"""')

            if docstring_start != -1 and docstring_end != -1:
                docstring = pyi_contents[docstring_start : docstring_end + 3]

                with open(py_file, "r") as py_file_obj:
                    py_contents = py_file_obj.read()

                docstring_start_py = py_contents.find('"""')
                docstring_end_py = py_contents.rfind('"""')

                if docstring_start_py != -1 and docstring_end_py != -1:
                    updated_py_contents = (
                        py_contents[:docstring_start_py]
                        + docstring
                        + py_contents[docstring_end_py + 3 :]
                    )

                    with open(py_file, "w") as py_file_obj:
                        py_file_obj.write(updated_py_contents)


apply_pyi_docstring()
