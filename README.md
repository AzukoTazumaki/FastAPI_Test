

<div id="header" align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDFxdjIwZDcwa3JpdDFmOGYxcHFwbmI0bnV3bXg0OXdmaWhiZHZ0bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oV7m7OaPe86aJzZwRC/giphy.gif" width="500"/>
</div>

# Azuko: FastAPI + Vue 3 + Vite + Postgres (beta v1.0)

`Azuko` – это статический сайт для прослушивания музыки, где Вы (в будущем) сможете
заказать продукты от битов до написания текста.

## Клонируйте репозиторий

### Откройте терминал:

Перейдите в директорию, где будет располагаться сайт `Azuko`

```bash
cd <name_of_your_directory>
```

Клонируйте репозиторий

```bash
git clone https://github.com/AzukoTazumaki/FastAPI_Test.git
```

Перейдите в `Azuko`

```bash
cd Azuko/
```

## Создайте окружение и установите зависимости для `backend`

### `Pip`:

```bash
cd backend/ && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

### `Pipenv`:

```bash
cd backend/ && python -m pipenv shell && pipenv install
```

## Создайте окружение и установите зависимости для `frontend`

В терминале:

```bash
cd frontend/ && npm install
```

Если Вы хотите внести изменения в `.css` файлы, 
выполните команду ниже, находясь в текущей директории:

```bash
npm run gulp
```This 

You must see:

```bash
<???>:static ???$ npm run gulp

> static@1.0.0 gulp
> gulp js_css

[??:??:??] Using gulpfile ~/<your_path_to_project>/Azuko/static/gulpfile.js
[??:??:??] Starting 'js_css'...
```

Это означает, что `Gulp` теперь просматривает все `css` файлы, так что когда 
Вы измените что-либо в стилях и сохраните файл, `Gulp` автоматически скомпилирует 
новый файл (`bundle.min.css`). Когда Вы клонируете данный репозиторий, запускать `Gulp`
не нужно, так как скомпилированный файл уже находится в папке `frontend/src/public`

## Создайте `.env` файл по примеру `.dev.env` (файлы окружения находятся в папке `environment`)

```python
# CREATE YOUR OWN .env FILE & SET THE PREFERENCES

DB_DRIVER='db_driver'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='host'
DB_PORT='port'
DB_NAME='db_name'
```

## Базы данных (только `Postgres` на данный момент)

Создайте базу данных с именем `db_name` из вашего `.env` файла. 
Затем в терминале выполните следующую команду:

```bash
cd backend/ && python create_db.py
```

Вы должны увидеть сообщение:

```bash
INFO: Database successfully created (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
```

Затем запустите команду ниже, находясь в текущей директории и запустите 
`backend` сервер [`Uvicorn` и `Fastapi`]

```bash
python project.py
```

Если все хорошо, Вы увидите следующее сообщение:

```bash
(Azuko) <???>@<???> Azuko % python3 project.py 
INFO:     Will watch for changes in these directories: ['/<your_path_to_project>/Azuko']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [?????] using WatchFiles
INFO:     Started server process [?????]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Остался последний шаг: запустить `frontend` сервер. Выполните следующую команду:

```bash
cd frontend/ && npm run dev
```

В терминале появится следующее сообщение и Вас автоматически перебросит на сервер:

```bash
???@??? frontend % npm run dev

> frontend@1.0.0 dev
> vite

# Вы увидите это, если порт 3000 занят на Вашем локальном компьютере
Port 3000 is in use, trying another one...

  VITE v4.5.0  ready in ???? ms

  ➜  Local:   http://localhost:3001/
  ➜  Network: http://???.???.?.???:3001/
  ➜  press h to show help

```

## Обновления
Когда вернусь с армии :)
