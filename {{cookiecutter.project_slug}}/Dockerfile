FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
COPY requirements/ requirements/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
