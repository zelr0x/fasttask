FROM python:3.10-slim

WORKDIR /fasttask

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -y --no-install-recommends install gcc

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .
