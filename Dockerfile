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
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 - --version 1.2.0 && \
    poetry install && \
    poe download_torch

ENTRYPOINT ["/bin/bash"]