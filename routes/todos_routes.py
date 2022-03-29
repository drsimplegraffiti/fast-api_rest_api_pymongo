from typing import Optional
from pydantic import ValidationError
from fastapi import APIRouter, HTTPException
from models.todos_models import Todo

from config.database import collection_name
from schemas.todos_schema import todo_serializer, todos_serializer
from bson import ObjectId


todo_api_router = APIRouter()

# root
@todo_api_router.get("/", tags=["Root"])
async def root():
    return {"message": "Hello World"}


## path parameter  route

# @todo_api_router.get("/todos/{q}")
# async def get_todos(q: str):
#      return {"item_id": q}

# retriever
@todo_api_router.get("/todos")
async def get_todos():
    try:
        todos = todos_serializer(collection_name.find())
        if not todos:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"status": "ok", "data": todos}
    except ValidationError as e:
        print(e.json())


# get single todos from
@todo_api_router.get("/todos/{id}")
async def get_todos(id: str, q: Optional[str] = None):
    try:
        todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
        if not todo:
            raise HTTPException(status_code=404, detail=f"{id} does not exist")
        return {"status": "ok", "data": todo}
    except ValidationError as e:
        print(e.json())


# Post to db
@todo_api_router.post("/todos")
async def post_todo(todo: Todo):
    try:
        _id = collection_name.insert_one(dict(todo))
        todo = todos_serializer(collection_name.find({"_id": _id.inserted_id}))
        return {"status": "ok", "data": todo}
    except ValidationError as e:
        print(e.json())


# update todo
@todo_api_router.put("/todos/{id}")
async def update_todo(id: str, todo: Todo):
    try:
        collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
        todo = todos_serializer(collection_name.find({"_id": ObjectId(id)}))
        return {"status": "ok", "data": todo}
    except ValidationError as e:
        print(e.json())


# delete todo
@todo_api_router.delete("/todos/{id}")
async def delete_todo(id: str):
    try:
        collection_name.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "ok", "data": []}
    except ValidationError as e:
        print(e.json())
