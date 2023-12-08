FROM docker/dev-environments-default:stable-1

WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip && \
    pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip/*
