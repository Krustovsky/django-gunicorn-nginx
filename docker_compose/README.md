# Запуск: Docker-compose

**Состав:**
- python 3.10
- django 4.0.4
- gunicorn 20.1.0
- postgesql 14
- nginx 1.23.1

**Запуск проекта:**

- Из директории ./empty_project
- создаем image с django `docker-compose build`
- стартуем проект `docker-compose up -d`
- Проверяем что по пути `localhost/admin` подгрузилась статика
