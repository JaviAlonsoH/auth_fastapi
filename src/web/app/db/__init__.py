import os
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://user1:1234@cluster0.sxfpn0k.mongodb.net/?retryWrites=true&w=majority")

db = client.auth_fastapi_db

properties_col = db.get_collection("properties")
