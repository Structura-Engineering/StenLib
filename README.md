# Welcome to:

## StenLib

<p align="center">
  <a href="https://app.deepsource.com/gh/illyrius666/QeLib/">
    <img src="https://app.deepsource.com/gh/illyrius666/StenLib.svg/?label=active+issues&show_trend=true&token=-tDSaXL3J9rCy_eVfjq65unj" alt="DeepSource">
    <img src="https://app.deepsource.com/gh/illyrius666/StenLib.svg/?label=resolved+issues&show_trend=true&token=-tDSaXL3J9rCy_eVfjq65unj" alt="DeepSource">
  </a>
</p>

## Setup the environment:

1. `.\setup.bat` (Windows) or `./setup.sh` (Linux)
2. SET interpreter to `.venv\Scripts\python.exe` (Windows) or `.venv/bin/python` (Linux)

3. TO UPDATE: deactivate venv and revert interpreter back to local python installation, then follow steps 1 & 2 again.

## Build package, Release on Github & Upload to (Test)PyPi:

1. FOR `TestPyPi`: In the push message use the keyword `.test .tag[x]`.
2. FOR `PyPi`: In the push message use the keyword `.deploy .tag[x]`.
