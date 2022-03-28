from typing import Optional
from pydantic import ValidationError
from fastapi import APIRouter, HTTPException
from models.user_models import User

from config.database import collection_name_user
from schemas.users_schema import user_serializer, users_serializer
from bson import ObjectId


user_api_router = APIRouter()

# all users should
# retriever
@user_api_router.get("/users")
async def get_users():
    try:
        users = users_serializer(collection_name_user.find())
        if not users:
            raise HTTPException(status_code=404, detail="User not found")
        return {"status": "ok", "data": users}
    except ValidationError as e:
        print(e.json())


# Create a user
@user_api_router.post("/user")
async def post_todo(user: User):
    try:
        _id = collection_name_user.insert_one(dict(user))
        user = users_serializer(collection_name_user.find({"_id": _id.inserted_id}))
        return {"status": "ok", "data": user}
    except ValidationError as e:
        print(e.json())
