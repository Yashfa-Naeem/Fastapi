from fastapi import Depends,FastAPI
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session

app=FastAPI()
database_models.Base.metadata.create_all(bind=engine)       #metadata is to import table name,column name etc. f



@app.get("/")
def greet():
     return {"message": "Welcome"}

products =[
    Product(id=1,name="laptop",description="budget phone",price=100,quantity=2),
    Product(id=2,name="bag",description="budget phone",price=99,quantity=6),
    Product(id=3,name="phone",description="budget phone",price=200,quantity=3),
]
def get_db():                                                #dependency injection so objects can use the database without repeatedly writing the code. 
    db = session()
    try:
        yield db
    finally:
        db.close()
         
def init_db():
    db=session()                                                                                 #session helps connect to the db.
    count = db.query(database_models.Product).count
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))                               #model_dump provides a library and ** helps unpack it
    db.commit()
init_db()

@app.get("/product")
def get_all_products(db:Session = Depends(get_db)):
    db_products=db.query(database_models.Product).all() 
                                                                        #python -m uvicorn main:app --reload
    return db_products   

@app.get("/product/{id}")
def get_one_product(id:int,db:Session = Depends(get_db)):
     db_product=db.query(database_models.Product).filter(database_models.Product.id == id).first()
     if db_product:                                                   #if product id matches that of URL
            return db_product
   
     return "product not found" 

@app.post("/product")
def add_product(product:Product,db:Session = Depends(get_db)):  #variable name and type hint,input expected
     db.add(database_models.Product(**product.model_dump()))                               #model_dump provides a library and ** helps unpack it
     db.commit()
     return product

@app.put("/product")
def udpate_product(id:int,product:Product,db:Session = Depends(get_db)):
      db_product=db.query(database_models.Product).filter(database_models.Product.id == id).first()
      if db_product:
         db_product.name=product.name
         db_product.description=product.description
         db_product.price=product.price
         db_product.quantity=product.quantity
         db.commit() 
         return "product updated successfully"
      else:
         return "no product found"

@app.delete("/product")
def delete_product(id:int,Product,db:Session = Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if  db_product:
       db.delete(db_product)
       db.commit()
       return "product deleted successfully"
    else:
        return "no product found" 

    

