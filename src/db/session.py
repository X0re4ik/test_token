from sqlalchemy import create_engine
from sqlalchemy.orm import \
    (sessionmaker, 
     scoped_session)

from src.settings import DATA_BASE_CONFIG

engine = create_engine(
    DATA_BASE_CONFIG.URI,
    #echo=True
)

Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
