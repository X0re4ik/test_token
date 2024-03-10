from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from .settings import DATA_BASE_CONFIG

engine = create_engine(
    DATA_BASE_CONFIG.URI,
    echo=True
)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)