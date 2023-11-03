import os
import subprocess
import sys

from setuptools import find_packages, setup

pip_packages: list[str] = ["setuptools", "types-setuptools", "mypy"]


class PackageSetup:
    """Setup package"""

    def __init__(self) -> None:
        """Setup package"""
        self.setup_package()

    @staticmethod
    def read_file(filename: str) -> str:
        """Read file"""
        with open(filename) as f:
            return f.read()

    def setup_package(self) -> None:
        """Setup package"""
        long_description: str = self.read_file("README.md")
        project_license: str = self.read_file("LICENSE.md")

        setup(
            name="StenLib",
            version="0.0.53",
            long_description=long_description,
            long_description_content_type="text/markdown",
            license=project_license,
            url="https://github.com/Structura-Engineering/StenLib",
            project_urls={
                "Bug Tracker": "https://github.com/Structura-Engineering/StenLib/issues"
            },
            install_requires=pip_packages,
            packages=find_packages(),
            python_requires=">=3.12.0",
            package_data={
                "*": ["*.py", "data/*.json", "*.pyi"],
            },
            zip_safe=False,
        )


class VENVSetup:
    """Setup virtual environment and install pip packages"""

    def __init__(self) -> None:
        """Setup virtual environment and install pip packages"""
        self.setup_venv()

    @staticmethod
    def setup_venv() -> None:
        """Setup virtual environment and install pip packages"""
        venv_dir = os.path.join(os.getcwd(), ".venv")
        python_executable = os.path.join(venv_dir, "Scripts", "python")
        pip_executable = os.path.join(venv_dir, "Scripts", "pip")

        subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
        subprocess.check_call(
            [python_executable, "-m", "pip", "install", "--upgrade"] + pip_packages
        )
        subprocess.check_call([pip_executable, "install", "--upgrade", "pip"])


if __name__ == "__main__":
    PackageSetup()
