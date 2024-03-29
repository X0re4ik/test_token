from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#from src.main import app
from .settings import DATA_BASE_CONFIG

Base = declarative_base()

engine = create_engine(
    DATA_BASE_CONFIG.URI,
    #echo=True
)

Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
