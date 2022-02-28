from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base
from app.helpers import hashing


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    # order = relationship("Order", back_populates="user_info")
    # cart = relationship("Cart", back_populates="user_cart")
    
    def __init__(self, name, email, password, *args, **kwargs) -> None:
        self.name = name
        self.email = email
        self.password = hashing.get_password_hash(password)
        
    def check_password(self, password):
        return hashing.verify_password()