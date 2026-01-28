from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Item(BaseModel):
    id : int
    detail : bool = False
@app.get("/items/{item_id}")



    

