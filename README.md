# API Yatube

REST API для проекта социальной сети YaTube для размещения постов и подписок на авторов.

## Установка

Как развернуть проект на локальной машине.

1. Склонируйте репозиторий

```
$ git clone https://github.com/aaaaaaaalesha/api_final_yatube.git
$ cd api_final_yatube
```

2. Создайте и активируйте рекламное окружение

```
$ python3 -m venv venv
$ venv/bin/activate
```

3. Установите зависимости

```
$ pip install -r requirements.txt
```

4. Выполните миграции

```
$ cd yatube_api
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ cd ..
```

4. Запуск сервера

```
$ python3 .\yatube_api\manage.py runserver
```

## Примеры

Некоторые примеры запросов к API.

### 1. Создание JWT-токена

`[POST] /api/v1/jwt/create/`

```json
{
  "username": "aaaaaaaalesha",
  "password": "ok_give_me_your_password"
}
```

Примеры ответов:

- `Status Code: 200`

```json
{
  "refresh": "******",
  "access": "******"
}
```

- `Status Code: 400`

```json
{
  "username": [
    "Обязательное поле."
  ],
  "password": [
    "Обязательное поле."
  ]
}
```

- `Status Code: 401`

```json
{
  "detail": "No active account found with the given credentials"
}
```

### 2. Получение публикаций

`[GET] /api/v1/posts/`

Пример ответа:

- `Status Code: 200`

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### 3. Частичное обновление комментария

`[PATCH] /api/v1/posts/{post_id}/comments/{id}/`

```json
{
  "text": "string"
}
```

Примеры ответа:

- `Status Code: 200`

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

- `Status Code: 401`

```json
{
  "detail": "Учетные данные не были предоставлены."
}
```

- `Status Code: 403`

```json
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

- `Status Code: 403`

```json
{
  "detail": "Страница не найдена."
}
```