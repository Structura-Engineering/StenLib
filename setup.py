from setuptools import find_packages, setup

setup(
    name="QeLib",
    version="0.0.30",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=open("LICENSE.md").read(),
    url="https://github.com/Illyrius666/QeLib",
    project_urls={"Bug Tracker": "https://github.com/Illyrius666/QeLib/issues"},
    packages=find_packages(),
    python_requires=">=3.11.5",
    package_data={
        "*": ["data/*.json", "py.typed", "*.pyi"],
    },
)
