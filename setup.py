import os
import shutil

from setuptools import Command, find_packages, setup


class CleanCmd(Command):
    """
    Custom clean command to remove previous versions in the dist directory.

    Usage:
        >>> `python setup.py clean`
    """

    description = "Remove previous versions in the dist directory"
    user_options = []

    def initialize_options(self) -> None:
        """Override method"""

    def finalize_options(self) -> None:
        """Override method"""

    def run(self) -> None:
        """Override method"""
        for entry in os.listdir("."):
            if os.path.isdir(entry) and (".egg-info" in entry or entry == "dist"):
                shutil.rmtree(entry, ignore_errors=True)
                print(f"Removed '{entry}' directory.")


setup(
    name="QeLib",
    version="0.0.22",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=open("LICENSE.md").read(),
    url="https://github.com/Illyrius666/QeLib",
    project_urls={"Bug Tracker": "https://github.com/Illyrius666/QeLib/issues"},
    install_requires=[
        "twine",
        "wheel",
        "pyside6",
        "shiboken6",
    ],
    packages=find_packages(),
    python_requires=">=3.11.5",
    package_data={
        "*": ["data/*.json", "py_typed", "*.pyi"],
    },
    cmdclass={"clean": CleanCmd},
)
