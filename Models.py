from pydantic import BaseModel
class Product(BaseModel):   #we don't need constructor when BaseModel is used
    id : int
    name : str
    description : str
    price : float
    quantity : int