# Тестовое задание
Тестовое задание FastAPI REST

---
Подразумевается, что на компьютере установлены Docker, docker-compose, Git.
Версии при разработке:
- Docker - 24.0.6
- Docker-compose - 1.29.2
- Git - 2.34.1
---

# Инструкция по сборке проекта

Склонируйте репозиторий к себе:
```
git clone https://github.com/Yashenkov22/test_victorina_rest.git
```
Перейдите в папку проекта:
```
cd test_victorina_rest/
```
Создайте файл .env:
```
touch .env
```
Откройте файл .env:
```
nano .env
```
---
Добавьте в файл .env следующее содержимое:

POSTGRES_USER=postgres

POSTGRES_PASSWORD=12345

POSTGRES_PORT=5432

POSTGRES_NAME=postgres

---
Выйдите и сохраните файл .env:
- нажмите Ctrl + X
- подтвердите изменения нажав Y
- нажмите Enter

**Перед сборкой убедитесь, что service Docker активен!**

Соберите docker-compose:
```
docker-compose build
```
Запустите сборку:
```
docker-compose up -d
```
Откройте браузер и перейдите по адресу: http://0.0.0.0:8000/docs

**Пример POST запроса** на адрес http://0.0.0.0:8000/get_questions/

Request Body:
```
  {
    "questions_num": 1
  }
```
Ответом будет либо пустой объект {}, либо последняя добавленная запись формата:
```
  {
    "id": int,
    "question": "string",
    "answer": "string",
    "created_at": datetime
  }
```
