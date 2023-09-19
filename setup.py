import setuptools as st

with open("README.md", "r") as fh:
    """Readme file for the project"""
    long_description = fh.read()

st.setup(
    name="QeLib",
    version="0.0.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Illyrius",
    license="LICENSE.md",
    packages=st.find_packages(),
    python_requires=">=3.11.5",
    install_requires=["setuptools", "string", "random"],
)
