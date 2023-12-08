FROM python:3.12-bullseye AS build

WORKDIR /workspace

COPY . /workspace

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --disable-pip-version-check --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip/*

FROM python:3.12-bullseye

WORKDIR /workspace

COPY --from=build /workspace /workspace

RUN useradd -m wsusr

USER wsusr

CMD ["/bin/bash", "-c", "source venv/bin/activate && exec /bin/bash"]