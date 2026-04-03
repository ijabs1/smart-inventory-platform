from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary in-memory inventory
inventory = []

class Item(BaseModel):
    name: str
    quantity: int


@app.get("/")
def home():
    return {"message": "Smart Inventory API is running"}


@app.get("/items")
def get_items():
    return inventory


@app.post("/items")
def add_item(item: Item):
    inventory.append(item)
    return {"message": "Item added", "item": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(inventory):
        deleted_item = inventory.pop(item_id)
        return {"message": "Item removed", "item": deleted_item}
    return {"error": "Item not found"}