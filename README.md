## Virtual Environment Setup:

1. `python -m venv .venv` (creates environment for packages).
2. select the correct interpreter (`.venv`).
3. activate the environment. `./.venv/Scripts/activate` (Windows) or source `./.venv/bin/activate` (Linux).
4. `pip install -e .`.

## Build package, Release on Github & Upload to TestPyPi:

1. In the push message use the keyword `.deploy`.

# TODO: UPDATE README.md