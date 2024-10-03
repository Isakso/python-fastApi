from fastapi import FastAPI

from enum import Enum

app = FastAPI()


@app.get("/", description= "This is a minor test", deprecated =True)
async def base_route():
    return {"message": "fastapi demo"}


@app.post("/")
async def post():
    return {"message": "This is a new post in the file"}

@app.get("/items")
async def list_items():
    return {"message": "This is a list of items"}

@app.get("/items/{item_id}")
async def get_items(item_id:int):
    return {"item_id":item_id}

@app.put("/")
async def put():
    return {"message":"This is my out test"}
class FoodEnum(str,Enum):
    fruits = "fruits"
    vegetable = "vegetables"
    meat = "meat"
@app.get("/foods/{food}")
async def get_foods(food:FoodEnum):
    if food == FoodEnum.vegetable:
        return {"foodname": food, "message":"you are health"}

    if food == FoodEnum.fruits:
        return {"foodname":food, "messge":"you are sweet"}
    if food == FoodEnum.meat:
        return {"foodname":food, "message":"Thats meaty"}
