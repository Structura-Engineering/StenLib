import subprocess

from setuptools import find_packages, setup


class PackageSetup:
    def __init__(self):
        self.pip_packages = ["setuptools", "types-setuptools"]

    def install_and_upgrade_packages(self):
        for package in self.pip_packages:
            if package == "StenLib":
                subprocess.check_call(
                    [
                        "python",
                        "-m",
                        "pip",
                        "install",
                        "--upgrade",
                        "-i",
                        "https://test.pypi.org/simple/",
                        package,
                    ]
                )
            else:
                subprocess.check_call(
                    ["python", "-m", "pip", "install", "--upgrade", package]
                )

    def read_file(self, filename):
        with open(filename) as f:
            return f.read()

    def setup_package(self):
        long_description = self.read_file("README.md")
        license = self.read_file("LICENSE.md")

        setup(
            name="StenLib",
            version="0.0.46",
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
