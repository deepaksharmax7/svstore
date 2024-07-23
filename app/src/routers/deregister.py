
from fastapi import APIRouter, HTTPException

router = APIRouter()

database = {}

@router.delete("/deregister/{item_id}")
async def deregister(item_id: int):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    del database[item_id]
    return {"message": "Item deregistered successfully"}
