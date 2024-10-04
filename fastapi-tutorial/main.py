from __future__ import annotations

from fastapi import FastAPI

from enum import Enum

from pydantic import BaseModel

app = FastAPI()


@app.get("/", description="This is a minor test", deprecated=True)
async def base_route():
    return {"message": "fastapi demo"}


@app.post("/")
async def post():
    return {"message": "This is a new post in the file"}


@app.get("/items")
async def list_items():
    return {"message": "This is a list of items"}


@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return {"item_id": item_id}


@app.put("/")
async def put():
    return {"message": "This is my out test"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetable = "vegetables"
    meat = "meat"


@app.get("/foods/{food}")
async def get_foods(food: FoodEnum):
    if food == FoodEnum.vegetable:
        return {"foodname": food, "message": "you are health"}

    if food == FoodEnum.fruits:
        return {"foodname": food, "messge": "you are sweet"}
    if food == FoodEnum.meat:
        return {"foodname": food, "message": "Thats meaty"}


fake_items_db = [{"item_name": "Loo"}, {"item_name": "Loo"}, {"item_name": "Loo"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get("/items/{item_id}")
async def get_items(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
        return {"item_id": item_id}


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
        return item_dict
