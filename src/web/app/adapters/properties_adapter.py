from typing import Type, TypeVar

from django.db import models
from fastapi import HTTPException, Path

from app.db import properties_col

from app.models.property_models import PropertyModel, UpdatePropertyModel, ResponseModel, ErrorResponseModel


async def get_properties_data():
    properties = []
    async for item in properties_col.find():
        properties.append(property_helper(item))
    return properties


async def get_property_data(id: str):
    item = await properties_col.find_one({"_id": ObjectId(id)})
    if item:
        return property_helper(item)
    return "Resource not found"


async def add_property_data(item_data: dict) -> dict:
    item = await properties_col.insert_one(item_data)
    new_item = await properties_col.find_one({"_id": item.inserted_id})
    return item


async def update_property_data(id: str, data: dict):
    if len(data) < 1:
        return False
    item = await properties_col.find_one({"_id": ObjectId(id)})
    if item:
        updated_item = await properties_col.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_item:
            return True
        return False


async def delete_property_data(id: str):
    item = await properties_col.find_one({"_id": ObjectId(id)})
    if item:
        await properties_col.delete_one({"_id": ObjectId(id)})
        return True
# helpers


def property_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "build_status": str(item["build_status"]),
        "is_active": item["is_active"],
        "start_month": item["start_month"],
        "construction_type": str(item["construction_type"]),
        "date_diff": str(item["date_diff"]),
        "description": item["description"],
        "date_in": item["date_in"],
        "property_type": item["property_type"],
        "end_week": str(item["end_week"]),
        "typology_type": str(item["typology_type"]),
        "id": str(item["id"]),
        "coordinates": item["coordinates"],
        "boundary_id": str(item["boundary_id"]),
        "id_uda": item["id_uda"],
        "title": item["title"],
        "listing_type": str(item["listing_type"]),
        "date": item["date"]
    }
