FROM golang:1.16-alpine

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip && \
    pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip/*
