# TODO: choose a small Python base image, set WORKDIR, copy requirements first,
# install dependencies, copy source, and run the CLI with safe default arguments.
FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY orderly/ orderly/

# Intentional incomplete image: app dependencies and files are not copied.
CMD ["python", "-m", "orderly.cli"]
