FROM python:3.12-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip && \
    pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt
