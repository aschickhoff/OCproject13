FROM python:3.10

WORKDIR /app

ENV PORT 8000

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN python manage.py 

CMD python manage.py runserver 0.0.0.0:$PORT
