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

from src.database import \
    (Session)

from src.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(500), nullable=False)
    
    is_superuser = Column(Boolean, default=False)
    is_stuff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    consumptions = relationship("Consumption", back_populates="user")

    @property
    def password():
        raise AttributeError("password is read-only")
    
    @password.setter
    def password(self, password: str) -> None:
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode("utf-8")
        self.password_hash = password_hash
    
    def set_password(self, password: str) -> None:
        self.password = password
    
    def check_password(self, password: str) -> str:
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())
    
    
    @classmethod
    def find_user_by_email(cls, email: str):
        return cls._find_by_unique_value(email=email)

    @classmethod
    def find_user_by_id(cls, id: int):
        return cls._find_by_unique_value(id=id)


    @staticmethod
    def _find_by_unique_value(**kwargs):
        return Session.query(User).filter_by(**kwargs).one_or_none()