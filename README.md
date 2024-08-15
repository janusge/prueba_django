## Deploy Steps
``` bash
$ cd prueba_django/docker
$ docker compose run web python manage.py migrate
$ docker compose run web python manage.py loaddata /code/seeds.json
$ docker-compose up -d
$ En el navegador ir a http://localhost:8000/api/v1/students/
```