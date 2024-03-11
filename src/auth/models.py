import bcrypt

from sqlalchemy import \
    (Column,
     Integer,
     String,
     Boolean)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(500), nullable=False)
    
    is_superuser = Column(Boolean, default=False)
    is_stuff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    
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