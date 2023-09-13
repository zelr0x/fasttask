# FastTask

FastTask is a toy task tracker app written in FastAPI with Tortoise ORM


## Run

### With docker-compose
To simply run the app, this should be enough:
```shell
docker compose up
```

If major change happened (e.g. dependency added), append `--build` flag.


### Manually

For running using .env, while at `fasttask/` run:
```shell
python -m app.main
```

For running with uvicorn directly, while at `fasttask/` run:

```shell
uvicorn app.main:app --host localhost --port 8080
```

For hot-reloading mode specify `--reload`.

Tip: absolute imports won't work if we start at the directory that is root package or some directory within it. We must run it at root package's parent.

## Develop

### Virtual environment

Create:

```shell
python -m venv venv
```

Activate (Windows):
```shell
.\venv\Scripts\activate.bat
```

Activate (*nix)
```shell
source ./venv/bin/activate
```

### Install dependencies

#### Manually with pip

```shell
pip install debugpy fastapi pydantic-settings "uvicorn[standard]" "tortoise-orm[asyncpg]"
```

#### Use requirements.txt

```shell
pip install -r requirements.txt
```

### Freeze dependencies

```shell
pip freeze > requirements.txt
```
