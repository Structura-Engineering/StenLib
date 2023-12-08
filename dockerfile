FROM python:3.12-bullseye AS build

WORKDIR /app

COPY . /app

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --disable-pip-version-check --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip/*

FROM python:3.12-bullseye

WORKDIR /app

COPY --from=build /app /app

RUN useradd -m appusr

USER appusr

CMD ["/bin/bash", "-c", "source venv/bin/activate && exec /bin/bash"]
