import re


def get_version():
    with open("setup.py", "r") as f:
        setup_file = f.read()
    version_match = re.search(r"^VERSION\s*=\s*'\"['\"]", setup_file, re.MULTILINE)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")
