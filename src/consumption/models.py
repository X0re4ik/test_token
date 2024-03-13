import bcrypt
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy import \
    (Column,
     Integer, Float,
     String,
     Boolean, 
     ForeignKey)
    
from sqlalchemy.orm import \
    (declarative_base, 
     relationship, 
     validates)

from src.db.base import Base

from src.auth.models import User

class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="consumptions")
    
    price = Column(Float, nullable=False)
    
    @validates
    def validate_price(self, key, address):
        print(key, address)
        return address