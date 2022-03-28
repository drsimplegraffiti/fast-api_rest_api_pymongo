## Setup

> pipenv install fastapi "uvicorn[standard]" pymongo pymongo[srv]

## Gitignore

> npx gitignore python

## Env

> pipenv install python-dotenv

##### docs

[openapi](http://127.0.0.1:8000/openapi.json)
[swagger docs](http://127.0.0.1:8000/docs)
[swagger redoc](http://127.0.0.1:8000/redoc)

##### Deploy to deta --> windows command (install deta)

> iwr https://get.deta.dev/cli.ps1 -useb | iex

##### Confirm if deta is installed

> deta --help --

#### login to deta [cmd]

> deta login

##### Create a new micro application

> deta new --python

##### Result

```
{
        "name": "fastapi_pymongo",
        "id": "6b4eef64-9716-4978-be47-a6ed3c6756f8",
        "project": "a0ei39ht",
        "runtime": "python3.9",
        "endpoint": "https://phvegm.deta.dev",
        "region": "eu-central-1",
        "visor": "enabled",
        "http_auth": "disabled"
}

```

[deployed link](https://phvegm.deta.dev/)

##### Update .env to deta production

> deta update -e .env
