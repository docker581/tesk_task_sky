FROM python:3.8.5

WORKDIR /code

COPY requirements.txt .

RUN pip install -r /code/requirements.txt

COPY . .

CMD gunicorn test_task_sky.wsgi:application --bind 0.0.0.0:8000