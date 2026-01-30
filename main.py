from fastapi import FastAPI
from models import Product

app=FastAPI()

@app.get("/")
def greet():
     return {"message": "Welcome"}

products =[
    Product(id=1,name="laptop",description="budget phone",price=100,quantity=2),
    Product(id=2,name="bag",description="budget phone",price=99,quantity=6),
    Product(id=3,name="phone",description="budget phone",price=200,quantity=3)
]

@app.get("/products")
def get_all_products():
    return products




    

