


![logo-teal](https://user-images.githubusercontent.com/70065792/160499099-29d33c02-d07a-4576-814e-5bb5739a2163.png)

##### Setup
> pipenv install fastapi "uvicorn[standard]" pymongo pymongo[srv]

##### Gitignore

> npx gitignore python

##### Env

> pipenv install python-dotenv

![pip](https://user-images.githubusercontent.com/70065792/160499463-01a1771e-feca-41c6-a610-ef9cae67d802.PNG)


##### docs

[openapi](http://127.0.0.1:8000/openapi.json)

[swagger docs](http://127.0.0.1:8000/docs)

[swagger redoc](http://127.0.0.1:8000/redoc)


---

##### Project structure
![structure](https://user-images.githubusercontent.com/70065792/160499278-fe103104-de55-4d72-9f3e-c94dc9b9e30a.PNG)


##### Models

![model](https://user-images.githubusercontent.com/70065792/160501552-1915f001-89d7-4a47-990d-7db1705604cd.PNG)


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
