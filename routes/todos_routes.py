from fastapi import APIRouter
from models.todos_models import Todo

from config.database import collection_name
from schemas.todos_schema import todo_serializer, todos_serializer
from bson import ObjectId


todo_api_router = APIRouter()

# retriever
@todo_api_router.get("/todos")
async def get_todos():
    todos = todos_serializer(collection_name.find())
    return {"status": "ok", "data": todos}

# get single todos from
@todo_api_router.get("/todos/{id}")
async def get_todos(id: str):
    todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": todo}

# Post to db
@todo_api_router.post("/todos")
async def post_todo(todo: Todo):
    _id = collection_name.insert_one(dict(todo))
    todo = todos_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": todo}

# update todo
@todo_api_router.put("/todos/{id}")
async def update_todo( id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": todo}


# delete todo
@todo_api_router.delete("/todos/{id}")
async def delete_todo( id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": []}