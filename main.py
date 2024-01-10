from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def base_get_route():
    return {"message": "Hello World"}

@app.post("/",description="Super")
def post():
    return {"data ":"hello from the post"}

@app.put("/")
def put():
    return {"message":"Hello from the put route"}



class FoodEnum(str , Enum):
    fruits ="Fruits"
    vegetables="vegetables"
    dairy ="dairy"
    meat= "meat"

@app.get("/food/{food_name}")
def food_item(food_name: FoodEnum):
    if food_name ==FoodEnum.vegetables:
        return {"message":"YOu are a healthy person"}
    
    if food_name.value == FoodEnum.dairy:
        return {"message":"You are an healthy person , but you like the milk produt"}

fake_item_db=[{"Item_name":"simple"},{"item_name":"abc"},{"item_name":"yzx"}]

@app.get("/item")
def list_item(skip :int=0,limit :int=10):
    return fake_item_db[skip : skip+limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q:  str | None = None):
    if q:
        return {"item_id": item_id,"q":q}
    return {"item_id":item_id}


class item(BaseModel):
    name :str
    price: float
    tax: float |None = None
    desription : str | None = None
     



@app.post("/items")
async def create_item(item : item):
    return item

