ARG PYTHON_IMAGE_TAG
FROM python:$PYTHON_IMAGE_TAG

ARG POETRY_VERSION

ENV PYTHONUNBUFFERED 1

WORKDIR /app

EXPOSE 8000

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi