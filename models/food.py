from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sql.database import Base

class Food(Base):
    """Create table for Food objects"""
    __tablename__ = "food"

    id = Column(Integer, nullable =False, primary_key=True, unique= True)
    name = Column(String, nullable =False)
    description = Column(String, nullable =True)
    price = Column(Integer, nullable = True)
    is_special = Column(Boolean)
    is_vegan = Column(Boolean)
    is_publish = Column(Boolean)
    toppings = relationship("Toppings")
    category_id = relationship("FoodCategory")

class Topping(Base):
    "Create table for Topping objects"
    __tablename__ = "topping"

    id = Column(Integer, ForeignKey("food.id"))
    name = Column(String, nullable=False)

class FoodCategory(Base):
    "Create table for FoodCategory objects"
    __tablename__ = "food_category"

    id = Column(Integer, ForeignKey("food.id"))
    name = Column(String, nullable=False)
    is_publish = Column(Boolean) 
