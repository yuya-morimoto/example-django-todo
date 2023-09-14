# Base
ARG PYTHON_IMAGE_TAG
FROM python:$PYTHON_IMAGE_TAG AS base

ARG POETRY_VERSION

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Generate SECRET_KEY and .env file
FROM base AS setup

# Local runner
FROM base AS local_runner

EXPOSE 8000

CMD ["poetry", "run", "task", "generate_env"]