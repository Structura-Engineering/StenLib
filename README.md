# Welcome to:

## QeLib
<p align="center">
  <a href="https://app.deepsource.com/gh/illyrius666/QeLib/">
    <img src="https://app.deepsource.com/gh/illyrius666/QeLib.svg/?label=active+issues&show_trend=true&token=-tDSaXL3J9rCy_eVfjq65unj" alt="DeepSource">
    <img src="https://app.deepsource.com/gh/illyrius666/QeLib.svg/?label=resolved+issues&show_trend=true&token=-tDSaXL3J9rCy_eVfjq65unj" alt="DeepSource">
  </a>
</p>

## Virtual Environment Setup:

1. `python -m venv .venv` (creates environment for packages).
2. select the correct interpreter (`.venv`).
3. activate the environment. `./.venv/Scripts/activate` (Windows) or source `./.venv/bin/activate` (Linux).
4. `python -m pip install -e .`.

## Build package, Release on Github & Upload to (Test)PyPi:

1. FOR `TestPyPi`: In the push message use the keyword `.test`.
2. FOR `PyPi`: In the push message use the keyword `.deploy`.
