# api_final

### API_Yatube
Проект предназначен для взаимодействия с базой данных Yatube с помощью API запросов.

GET, POST, PUT, PATCH, DELETE, HEAD

Для получения токена доступа передать параметры:
```
{
    "username":"name_example",
    "password":"pass_example"
}
В запрос:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```


адреса API запросов:

```
http://127.0.0.1:8000/api/v1/posts/
http://127.0.0.1:8000/api/v1/groups/
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
http://127.0.0.1:8000/api/v1/follow/
```
### EXAMPLE REQUESTS

Получить список всех постов
GET - http://127.0.0.1:8000/api/v1/posts/
```
[
    {
        "id": 1,
        "author": "vitsman",
        "text": "text1",
        "pub_date": "2024-11-03T11:28:22.796327Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "vitsman",
        "text": "text3",
        "pub_date": "2024-11-04T14:28:03.031403Z",
        "image": null,
        "group": null
    }
]
```

Создать комментарий к посту. Требуется передать поле "text"
POST - http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

```
{
    "text":"text_example"
}
```
Ответ:
```
{
    "id": 2,
    "text": "text_example",
    "post": 1,
    "author": "vitsman",
    "created": "2024-11-04T15:08:23.749590Z"
}
```
PUT запрос к определенному посту.
PUT - http://127.0.0.1:8000/api/v1/posts/{post_id}/

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VitsVi/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции в папке файла manage.py:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```