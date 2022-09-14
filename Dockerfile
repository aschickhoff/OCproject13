FROM python:3.10

WORKDIR /app

ARG SECRET_KEY
ARG DEBUG
ARG DSNkey

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG
ENV DSNkey=$DSNkey


COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py 

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
