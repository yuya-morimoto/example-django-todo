########### Base
ARG PYTHON_IMAGE_TAG
FROM python:$PYTHON_IMAGE_TAG AS base

ARG POETRY_VERSION

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/


########### Generate SECRET_KEY and .env file
FROM base AS setup

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


########### Local runner
FROM base AS local_runner

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi