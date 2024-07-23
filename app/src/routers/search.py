
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.item import Item

router = APIRouter()

database = {}

@router.get("/search", response_model=List[Item])
async def search(name: Optional[str] = None):
    results = []
    for item in database.values():
        if name is None or name.lower() in item.name.lower():
            results.append(item)
    if not results:
        raise HTTPException(status_code=404, detail="No items found")
    return results
