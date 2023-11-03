import subprocess

from setuptools import find_packages, setup


class VENVSetup:
    def __init__(self):
        self.venv_packages = ["setuptools", "wheel", "twine", "types-setuptools"]

    def install_and_upgrade_packages(self):
        for package in self.venv_packages:
            subprocess.check_call(
                ["python", "-m", "pip", "install", "--upgrade", package]
            )

    def setup_package(self):
        self.install_and_upgrade_packages()


class PackageSetup:
    def __init__(self):
        self.pip_packages = ["setuptools", "types-setuptools"]
        self.setup_package()

    def read_file(self, filename):
        with open(filename) as f:
            return f.read()

    def setup_package(self):
        long_description = self.read_file("README.md")
        license = self.read_file("LICENSE.md")

        setup(
            name="StenLib",
            version="0.0.47",
            long_description=long_description,
            long_description_content_type="text/markdown",
            license=license,
            url="https://github.com/Structura-Engineering/StenLib",
            project_urls={
                "Bug Tracker": "https://github.com/Structura-Engineering/StenLib/issues"
            },
            install_requires=self.pip_packages,
            packages=find_packages(),
            python_requires=">=3.12.0",
            package_data={
                "*": ["*.py", "data/*.json", "*.pyi"],
            },
            zip_safe=False,
        )


if __name__ == "__main__":
    PackageSetup()
