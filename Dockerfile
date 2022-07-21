# syntax=docker/dockerfile:1.4
FROM python:3.7

ENV HOME /updater/

WORKDIR ${HOME}

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    python -m pip install -r requirements.txt

COPY . .

# additional directories to look for modules 
# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:${HOME}"

# run from current workdir
CMD python app/main.py