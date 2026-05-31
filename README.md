markdown
# Онлайн Кинотеатр с идентификацией, аутентификацией, авторизацией, с помощью (Flask, JWT, SQLAlchemy)

"Кинопоиск" с фильмами, жанрам, режиссерами и пользователями.  
- (Необязательно) Если хотите увидеть ссылки и картинки (названия и отображение фильмов) то подключите ВПН или прокси для ютуба

## 🚀 Стек технологий

* **Backend**: Python 3.10, Flask, Marshmallow, SQLAlchemy, REST, CRUD, JWT, sqlite
* **Database & Logging**: PostgreSQL, Psycopg2, RotatingFileHandler
* **DevOps**: Docker, Docker Compose

## 🛠 Пошаговый запуск проекта

### 1. Клонирование репозитория 
Откройте терминал и скачайте проект на свой компьютер:
```bash
git clone https://github.com/Alex-Power-programmer/coursework_3_source.git
cd coursework_3_source 
```

## Описание проекта
### 2. Локальная установка зависимостей и инициализация БД

```bash
# Создаем и активируем виртуальное окружение (рекомендуется)
python -m venv .venv
source .venv/bin/activate  # Для Linux/macOS
.venv\Scripts\activate     # Для Windows
```

- Установка зависимостей
```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

- Создание моделей (очистит БД и создаст все модели, указанные в импорте)
```shell
python create_tables.py
```

- Загрузка данных в базу
```shell
python load_fixtures.py
```
Скрпит читает файл fixtures.json и загружает данные в базу. Если данные уже загружены - выводит соответсвующее сообщение. 


## 3.0 Запуск проекта (Windows) 
```shell
python run.py
```

### 3.1 Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run
```

### 3.2 CMD (Windows) если не запустился, то выполните шаг3.0
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### 3.3 PowerShell (Windows), если не запустился, то выполните шаг3.0
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run
```

### Интерактивная документация (Swagger UI)
Перейдите по ссылке для отправки тестовых запросов через браузер:
* **[http://127.0.0.1:25000/docs](http://127.0.0.1:25000/docs)** — интерактивная панель Swagger UI
- **POST** /auth/register — передавая  email и пароль, создаем пользователя в системе.
- **POST** /auth/login — передаем email и пароль и, если пользователь прошел аутентификацию, возвращаем пользователю ответ в виде:
- {
   "access_token": "qwesfsdfa",
   "refresh_token": "kjhgfgjakda",
} 
- **PUT** /auth/login — принимаем пару токенов и, если они валидны, создаем пару новых.
- 


## Запуск тестов
```shell
pytest .
```

