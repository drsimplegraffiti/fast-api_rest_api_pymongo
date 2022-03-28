from dotenv import load_dotenv
from pymongo import MongoClient
import os


load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.todo_app

collection_name = db["todos_app"]
collection_name_user = db["users_app"]
