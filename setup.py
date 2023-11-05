from setuptools import find_packages, setup

from StenLib.StenUtils import Utils

setup(
    name="StenLib",
    version="0.1.0",
    long_description=Utils.read_file("README.md"),
    long_description_content_type="text/markdown",
    license=Utils.read_file("LICENSE.md"),
    url="https://github.com/Structura-Engineering/StenLib",
    project_urls={
        "Bug Tracker": "https://github.com/Structura-Engineering/StenLib/issues"
    },
    install_requires=Utils.read_file("requirements.txt").splitlines(),
    packages=find_packages(),
    python_requires=">=3.12.0",
    package_data={
        "*": ["*.py", "data/*.json", "*.pyi"],
    },
    zip_safe=False,
)
