import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://localhost:27017")

db = client.auth_fastapi_db

properties_col = db.get_collection("properties")
