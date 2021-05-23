FROM python:3.9

ENV pythonunbuffered=1

RUN mkdir /app

COPY ./app /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
