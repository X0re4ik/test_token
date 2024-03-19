from typing import Optional, List

from sqlalchemy import String, ForeignKey, TIMESTAMP, DateTime, Table, Column
from sqlalchemy.orm import declarative_base, relationship, validates, Mapped, mapped_column
from sqlalchemy.sql import func

from sqlalchemy_file import FileField

from src.db.base import Base
from db.session import Session


secret_file_tags = Table(
    "secret_files_tags",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id")),
    Column("secret_file_id", ForeignKey("secret_files.id")),
)

from cryptography.fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

class SecretFile(Base):
    __tablename__ = "secret_files"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    create_date: Mapped[TIMESTAMP] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now()
    )
    file: Mapped[FileField] = mapped_column(FileField, nullable=True)
    tags: Mapped[List["Tag"]] = relationship(secondary=secret_file_tags)
    
    @property
    def uri(self):
        return "1"
    
    @classmethod
    def get_by_id(cls, id: int):
        return Session.query(SecretFile).filter_by(id=id).one_or_none()
    
    @classmethod
    def get_by_uri(cls, uri: str):
        return Session.query(SecretFile).filter_by(id=id).one_or_none()
    


class SecretFileOwner(Base):
    __tablename__ = "secret_files_owners"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False,
    )
    
    owner: Mapped['User'] = relationship()
    
    secret_file_id: Mapped[int] = mapped_column(
        ForeignKey("secret_files.id", ondelete="CASCADE"), 
        nullable=False,
    )
    
    secret_file: Mapped['SecretFile'] = relationship()