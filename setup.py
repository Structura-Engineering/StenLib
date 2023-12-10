from setuptools import find_packages, setup

setup(
    name="StenLib",
    version="0.2.1",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license=open("LICENSE.md").read(),
    url="https://github.com/Structura-Engineering/StenLib",
    project_urls={
        "Bug Tracker": "https://github.com/Structura-Engineering/StenLib/issues"
    },
    install_requires=open("requirements.txt").read().splitlines(),
    packages=find_packages(),
    python_requires=">=3.12.0",
    package_data={
        "*": ["*.py", "data/*.json", "*.pyi"],
    },
    zip_safe=False,
)
