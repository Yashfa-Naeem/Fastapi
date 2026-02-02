
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Product(Base):   #to inherit class
    id : int
    name : str
    description : str
    price : float
    quantity : int