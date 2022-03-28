from fastapi import FastAPI
from routes.todos_routes import todo_api_router

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = FastAPI()

app.include_router(todo_api_router)