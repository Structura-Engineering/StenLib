import re

with open("setup.py") as f:
    version_match = re.search(r"version=\"(.+?)\"", f.read())

if version_match:
    version = version_match.group(1)
    print(version)
else:
    print("Version not found")
