## Installation:

1. `python -m venv .venv` (creates environment for packages).
2. select the correct interpreter (`.venv`).
3. activate the environment. `./.venv/Scripts/activate` (Windows) or source `./.venv/bin/activate` (Linux).
4. `pip install -e .`.

## Upload to PyPi:

1. Update version in setup.py
2. Run `python setup.py sdist`
3. Run `twine upload dist/*` or `twine upload -r testpypi dist/*` for test upload
