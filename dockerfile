ARG IMAGE=python
ARG VARIANT=3.12-bullseye

FROM ${IMAGE}:${VARIANT} AS build

WORKDIR /workspace

COPY . /workspace

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get purge -y imagemagick imagemagick-6-common && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --disable-pip-version-check --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip/*

FROM ${IMAGE}:${VARIANT}

WORKDIR /workspace

COPY --from=build /workspace /workspace

CMD ["/bin/bash", "-c", "source venv/bin/activate && exec /bin/bash"]