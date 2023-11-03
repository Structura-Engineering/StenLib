import subprocess

from setuptools import find_packages, setup

pip_packages: list[str] = ["setuptools", "types-setuptools", "mypy"]


class PackageSetup:
    """Setup package"""

    def __init__(self) -> None:
        """Setup package"""
        self.setup_package()

    def read_file(self, filename: str) -> str:
        """Read file"""
        with open(filename) as f:
            return f.read()

    def setup_package(self) -> None:
        """Setup package"""
        long_description: str = self.read_file("README.md")
        license: str = self.read_file("LICENSE.md")

        setup(
            name="StenLib",
            version="0.0.51",
            long_description=long_description,
            long_description_content_type="text/markdown",
            license=license,
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

    def setup_venv(self) -> None:
        """Setup virtual environment and install pip packages"""
        subprocess.check_call(["python", "-m", "venv", ".venv"])
        subprocess.check_call(
            [".venv\\Scripts\\python", "-m", "pip", "install", "--upgrade"]
            + pip_packages
        )
        subprocess.check_call(
            [".venv\\Scripts\\python", "-m", "pip", "install", "--upgrade", "pip"]
        )


if __name__ == "__main__":
    PackageSetup()
