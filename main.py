from fastapi import FastAPI
from models import Product

app=FastAPI()

@app.get("/")
def greet():
     return {"message": "Welcome"}

products =[
    Product(id=1,name="laptop",description="budget phone",price=100,quantity=2),
    Product(id=2,name="bag",description="budget phone",price=99,quantity=6),
    Product(id=3,name="phone",description="budget phone",price=200,quantity=3),
]

@app.get("/product")
def get_all_products():                               #python -m uvicorn main:app --reload
    return products

@app.get("/product/{id}")
def get_one_product(id:int):
     for product in products:
          if product.id==id:   #if product id matches that of URL
            return product
     else:
          return "product not found" 

@app.post("/product")
def add_product(product:Product):  #variable name and type hint,input expected
    products.append(product)
    return product

@app.put("/product")
def udpate_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
         products[i]=product
         return "product added successfully"
    return "no product found"

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
         del products[i]
         return "product deleted successfully"
    return "no product found"
    

