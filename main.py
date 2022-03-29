from ensurepip import version
from fastapi import FastAPI
from routes.todos_routes import todo_api_router
from routes.user_routes import user_api_router

app = FastAPI(
    title="CRUD API using FastAPI and pymongo",
    description="A simple rest api",
    version="1.0.1",
    openapi_url="/openapi.json",
)

app.include_router(todo_api_router, prefix="/api/v1", tags=["todos"])
app.include_router(user_api_router, prefix="/api/v1", tags=["users"])

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="debug")
