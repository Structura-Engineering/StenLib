## Virtual Environment Setup:

1. `python -m venv .venv` (creates environment for packages).
2. select the correct interpreter (`.venv`).
3. activate the environment. `./.venv/Scripts/activate` (Windows) or source `./.venv/bin/activate` (Linux).
4. `python -m pip install -e .`.

## Build package, Release on Github & Upload to (Test)PyPi:

1. FOR `TestPyPi`: In the push message use the keyword `.test`.
2. FOR `PyPi`: In the push message use the keyword `.deploy`.

# TODO: UPDATE README.md
