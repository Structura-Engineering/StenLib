# Welcome to:

## StenLib

<p align="center">
  <a href="https://app.deepsource.com/gh/Structura-Engineering/StenLib/">
    <img src="https://app.deepsource.com/gh/Structura-Engineering/StenLib.svg/?label=active+issues&show_trend=true&token=aVu9lik1r9ykXWLQZSGz3ItB" alt="DeepSource">
    <img src="https://app.deepsource.com/gh/Structura-Engineering/StenLib.svg/?label=resolved+issues&show_trend=true&token=aVu9lik1r9ykXWLQZSGz3ItB" alt="DeepSource">
  </a>
</p>
<p align="center">
  <a>
    <img src="https://img.shields.io/badge/Unittest-${{ job.status }}-brightgreen" alt="Unittest">
    <img src="https://img.shields.io/badge/Build-${{ job.status }}-brightgreen" alt="Build">
    <img src="https://img.shields.io/badge/Release-${{ job.status }}-brightgreen" alt="Release">
    <img src="https://img.shields.io/badge/PyPI-${{ job.status }}-brightgreen" alt="PyPI">
    <img src="https://img.shields.io/badge/Docs-${{ job.status }}-brightgreen" alt="Docs">
  </a>
</p>

## Setup the project:

1. Install `Docker Desktop`.
2. Click on the `blue remote button` on the bottom left of vsc.
3. Click on `Clone Repository in Container Volume...`.
4. Follow the steps one by one, Wait a bit, Done.

## Build package, Release on Github & Upload to (Test)PyPi:

1. FOR `TestPyPi`: In the push message use the keyword `.test .tag[x]`.
2. FOR `PyPi`: In the push message use the keyword `.deploy .tag[x]`.
