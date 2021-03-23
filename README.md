[![test_task workflow](https://github.com/AndIsaev/test_task/actions/workflows/main.yml/badge.svg)](https://github.com/AndIsaev/test_task/actions/workflows/main.yml)

<p><a href="https://www.python.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/938bc97e6c0351babffcd724243f78c6654833e451efc6ce3f5d66a635727a9c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d507974686f6e" alt="Python" data-canonical-src="https://img.shields.io/badge/-Python-464646??style=flat-square&amp;logo=Python" style="max-width:100%;"></a>
<a href="https://www.djangoproject.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/99e48bebd1b4c03828d16f8625f34439aa7d298ea573dd4e209ea593a769bd06/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446a616e676f2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d446a616e676f" alt="Django" data-canonical-src="https://img.shields.io/badge/-Django-464646??style=flat-square&amp;logo=Django" style="max-width:100%;"></a>
<a href="https://www.docker.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/038c45c7c5f0059723bba28b5b77bd9ac7994c8da774814c8fcb620f4bc61b35/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d646f636b65722d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d646f636b6572" alt="docker" data-canonical-src="https://img.shields.io/badge/-docker-464646??style=flat-square&amp;logo=docker" style="max-width:100%;"></a>
<a href="https://www.postgresql.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/18b5ef277b89701f948c212d45d3460070037bda9712fe5f1e64315811356ea2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d506f737467726553514c2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d506f737467726553514c" alt="PostgreSQL" data-canonical-src="https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&amp;logo=PostgreSQL" style="max-width:100%;"></a>
<a href="https://www.sqlite.org/index.html" rel="nofollow"><img src="https://camo.githubusercontent.com/2c46c2b57530e634094dcb5ca341adbd8cc101300fd0968991b2a2700f1ac318/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d53514c6974652d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d53514c697465" alt="SQLite" data-canonical-src="https://img.shields.io/badge/-SQLite-464646??style=flat-square&amp;logo=SQLite" style="max-width:100%;"></a>

# Тестовое задание от компании "Некидаем"

Задача:
-  «+» Имеется база стандартных пользователей Django (добавляются через админку, регистрацию делать не надо). 
- «+» У каждого пользователя есть персональный блог. Новые создавать он не может.
- «+» Пост в блоге — элементарная запись с заголовком, текстом и временем создания.
- «+» Пользователь может подписываться (отписываться) на блоги других пользователей (любое количество).
- «+» У пользователя есть персональная лента новостей, в которой в обратном хронологическом порядке выводятся посты из блогов, на которые он подписан.
- «+» Пользователь может помечать посты в ленте прочитанными.
- «+» При добавлении/удалении подписки содержание ленты меняется (при удалении подписки пометки о "прочитанности" сохранять не нужно).
- «-» При добавлении поста в ленту — подписчики получают почтовое уведомление со ссылкой на новый пост.
- «-» Изменение содержания лент подписчиков (и рассылка уведомлений) должно происходить как при стандартной публикации поста пользователем через интерфейс сайта, так при добавлении/удалении поста через админку.
Проект реализован с помощью Class-based views.


## Стек

```sh
Python
Django
Bootstrap
Sqlite
PostgreSQL
```

## Установка


Клонируем проект: 
```
git clone git@github.com:AndIsaev/test_task.git
```
В домашней директории проекта Создать папку .env:


Пример добавляемых настроек в папку .env:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
```

Выполнить команду:

```
docker-compose up
```

Отобразить список работающих контейнеров:

```
docker container ls
```

В списке контейнеров копировать CONTAINER ID контейнера username/yamdb_final_web:latest (username - имя пользователя на DockerHub):

```
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                NAMES
9338873f6a9e   nginx:1.19.6           "/docker-entrypoint.…"   45 seconds ago   Up 43 seconds   0.0.0.0:80->80/tcp   foodgram-project_nginx_1
d415a082597e   andisaev/foodgram:v1   "/bin/sh -c 'gunicor…"   47 seconds ago   Up 45 seconds                        foodgram-project_web_1
d8cb992faa64   postgres:12.4          "docker-entrypoint.s…"   4 minutes ago    Up 46 seconds   5432/tcp             foodgram-project_postgres_1
```

Выполнить вход в контейнер:

```
docker exec -it d415a082597e bash
```

Внутри контейнера выполнить миграции:

```
python manage.py migrate
```


Также можно наполнить базу данных начальными тестовыми данными:

```
python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
python manage.py loaddata dump.json
```
или

Для создания нового суперпользователя можно выполнить команду:

```
$ python manage.py createsuperuser
```

Для остановки и удаления контейнеров и образов на сервере:

```
sudo docker stop $(sudo docker ps -a -q) && sudo docker rm $(sudo docker ps -a -q) && sudo docker rmi $(sudo docker images -q)
```

