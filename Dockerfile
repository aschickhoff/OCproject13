FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DSNkey $SENTRY_DSN
ENV SECRET_KEY $SECRET_KEY

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py 

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
