FROM python:3.10

WORKDIR /app

ENV PORT 8000

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
