FROM python:3.9-slim

# Avoid requirement to set country code, etc.
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    curl \
    software-properties-common \
    && \
    apt-get clean

WORKDIR /home

# Install poetry 1.2.0
COPY pyproject.toml poetry.lock /home/
RUN curl -sSL https://install.python-poetry.org | python - --preview && \
    export PATH="/root/.local/bin:$PATH" && \
    pip3 install poethepoet && \
    poetry install && \
    poe download_torch

ENTRYPOINT ["/bin/bash"]