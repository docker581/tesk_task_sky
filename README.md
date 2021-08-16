# test_task_sky

## Описание проекта
API для медицинских данных

## Стек технологий
- Python 3.8.3
- Django 3.0.5
- Django Rest Framework (DRF) 3.12.4
- Docker-compose 3.3
- Postgres 12.4
- Nginx 1.19.3
- Gunicorn 20.0.4

## Установка docker
https://docs.docker.com/engine/install/

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/test_task_sky
```

### Пример файла .env
```bash
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres
DB_HOST=db 
DB_PORT=5432
```

### Запуск приложения
```bash
docker-compose up -d
```

### Создание суперпользователя
```bash
docker-compose exec web python manage.py makemigrations
```
```bash
docker-compose exec web python manage.py migrate --noinput
```
```bash
docker-compose exec web python manage.py createsuperuser
```

## Документация по API
```bash
http://127.0.0.1:8000/swagger - Swagger
```
```bash
http://127.0.0.1:8000/redoc - Redoc
```

## Логирование результатов API-запросов - DRF API Logger
```bash
http://127.0.0.1/admin/drf_api_logger/apilogsmodel/
```