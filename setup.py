from setuptools import setup

setup(
    name="QeLib",
    version="0.0.1",
    description="Qerimi Engineering Library",
    author="Illyrius",
    license="LICENSE.md",
    packages=["src"],
    python_requires=">=3.11.5",
    install_requires=["numpy", "pyside6", "pyqtdarktheme", "ezdxf"],
)
