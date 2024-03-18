from typing import List

from sqlalchemy import \
    (String, 
     Float,
     ForeignKey, 
     DateTime, 
     Table,
     Column,)
from sqlalchemy.orm import \
    (Mapped,
     mapped_column,
     relationship,
     validates)
from sqlalchemy.sql import func

from src.db.base import Base
from src.auth.models import User
from src.tags.models import Tag



purchases_tags = Table(
    "purchases_tags",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id")),
    Column("purchase_id", ForeignKey("purchases.id")),
)

class Purchase(Base):
    
    __tablename__ = 'purchases'
    
    id: Mapped[str] = mapped_column(primary_key=True)
    
    owner_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id", 
            ondelete="CASCADE"
        ),
        nullable=False,
    )
    
    owner: Mapped[User] = relationship()
    
    price: Mapped[float] = mapped_column(
        Float, 
        nullable=False
    )
    
    currency: Mapped[str] = mapped_column(
        String(255), 
        default="RUB"
    )
    
    create_date: Mapped[DateTime] = mapped_column(
        DateTime, 
        server_default=func.now(), 
        nullable=False
    )
    
    tags: Mapped[List["Tag"]] = relationship(secondary=purchases_tags)
    
    @validates("price")
    def validate_price(self, attr, value):
        if value < 0:
            raise ValueError("Price must be greater than zero")
        return value
    
    
    