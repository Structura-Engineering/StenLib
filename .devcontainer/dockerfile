FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
