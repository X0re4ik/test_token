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

from sqlalchemy import Integer, String, ForeignKey

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.db.base import Base
from enum import Enum

class Tag(Base):
    __tablename__ = "tags"
    
    name: Mapped[str] = mapped_column(primary_key=True)