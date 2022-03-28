from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://drsimplegraffiti:admin1234@fastapi.wc9es.mongodb.net/todo?retryWrites=true&w=majority")
db = client.todo_app

collection_name = db["todos_app"]
