from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.db.base import Base

class Tag(Base):
    __tablename__ = "tags"
    
    id: Mapped[str] = mapped_column(primary_key=True)