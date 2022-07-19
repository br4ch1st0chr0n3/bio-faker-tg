FROM python:3.7

WORKDIR .

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/bio-faker-tg"

CMD python app/main.py
