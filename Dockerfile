FROM python:slim-buster

WORKDIR /app

RUN mkdir "templates"

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT export FLASK_APP=app.py && flask run --host 0.0.0.0
