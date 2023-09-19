import setuptools as st

with open('README.md', 'r') as fh:
    long_description = fh.read()

st.setup(
    name='QeLib',
    version='0.0.3',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author='Illyrius',
    license='LICENSE.md',
    packages=st.find_packages(),
    python_requires='>=3.11.5',
    install_requires=['setuptools>=68','wheel','numpy','pyside6','pyqtdarktheme','ezdxf'],
)