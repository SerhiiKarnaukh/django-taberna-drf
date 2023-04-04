# WIP:Django-Taberna-DRF

## For local development

1. Build the image and make migrations

```
docker-compose build
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

3. Run container

```
docker-compose up
```

4. Go to admin panel and add test content

```
http://127.0.0.1:8000/admin
```

### For debugging

```
1.See .vscode/launch.json
2.docker-compose -f docker-compose.yml -f docker-compose-debug.yml up --build + F5
```

### Tests

1. Create report

```
docker-compose run --rm app sh -c "coverage run manage.py test"
docker-compose run --rm app sh -c "coverage report"
docker-compose run --rm app sh -c "coverage html"
```

2. Run Tests

```
docker-compose up
docker exec -it taberna-drf coverage run manage.py test
```

### Create your own project with this Dockerfile

```
1.Create your dependency file 'requirements.txt' (Django + psycopg2)
2.Create .dockerignore
3.Commands:
docker-compose build
docker-compose run --rm app sh -c "django-admin startproject projects_name"
4.Change the 'settings.py' file to take into account the database connection constants
5.Next commands:
docker-compose run --rm app sh -c "python manage.py startapp apps_name"
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
