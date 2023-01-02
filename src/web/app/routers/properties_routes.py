from typing import List

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..models.property_models import (
    PropertyModel,
    UpdatePropertyModel,
    ErrorResponseModel,
    ResponseModel
)

from app.adapters.properties_adapter import *


router = APIRouter()


@router.post("/properties", response_description="Property data added to database")
async def add_property_data(item: PropertyModel = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_property(item)
    return ResponseModel(new_item, 201, "Property added")


@router.get("/properties", response_description="Properties retrieved")
async def get_properties():
    items = await get_properties_data()
    if items:
        return ResponseModel(items, "Data received succesfully")
    return ResponseModel(items, "Empty list")


@router.get("/properties/{id}", response_description="Property data retrieved")
async def get_property(id):
    item = await get_property_data(id)
    if item:
        return ResponseModel(item, "Data received succesfully")
    return ResponseModel("An error ocurred", 404, "The property does not exist")


@router.put("/properties/{id}")
async def update_property(id: str, req: UpdatePropertyModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_item = await update_property_data(id, req)
    if updated_item:
        return ResponseModel("Data updated of property with the id: {}".format(id), "Property correctly updated!")
    return ErrorResponseModel("An error ocurred", 404, "There was an error updating the property...")


@router.delete("/properties/{id}", response_description="Property data succesfully deleted")
async def delete_property(id: str):
    deleted_item = await delete_property_data(id)
    if deleted_item:
        return ResponseModel("Property with id: {} deleted".format(id), "Property succesfully deleted.")
    return ErrorResponseModel("An error ocurred", 404, "The property does not exist")
