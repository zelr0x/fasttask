# FastTask

FastTask is a toy task tracker app written in FastAPI


## Run

```shell
uvicorn main:app --reload
```


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
pip install fastapi
pip install "uvicorn[standard]"
pip install tortoise-orm[sqlite]
```

#### Use requirements.txt

```shell
pip install -r requirements.txt
```

### Freeze dependencies

```shell
pip freeze > requirements.txt
```
