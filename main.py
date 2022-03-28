from ensurepip import version
from fastapi import FastAPI
from routes.todos_routes import todo_api_router
from routes.user_routes import user_api_router

app = FastAPI(
    title="CRUD API using FastAPI and pymongo",
    description="A simple rest api",
    version="1.0.1",
)

app.include_router(todo_api_router)
app.include_router(user_api_router)
