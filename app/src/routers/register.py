
from fastapi import APIRouter, HTTPException
from models.item import Item

router = APIRouter()

database = {}

@router.post("/register")
async def register(item: Item):
    if item.id in database:
        raise HTTPException(status_code=400, detail="Item already registered")
    database[item.id] = item
    return {"message": "Item registered successfully"}
