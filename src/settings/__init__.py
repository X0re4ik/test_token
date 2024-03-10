import datetime

from dotenv import dotenv_values
from pathlib import Path


SRC_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = SRC_DIR.parent
ENV_FILE = BASE_DIR / ".env"
config = dotenv_values(ENV_FILE)

class DataBaseConfig:
    #postgresql://scott:tiger@localhost/mydatabase
    URI = config.get("DATABASE_URL")
    

class ServerConfig:
    HOST = config.get("HOST")
    PORT = config.get("PORT")

class JWTConfig:
    SECRET_KEY = "sfsdfsdf"
    ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)
    REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    
    ALGORITHM = "HS256"


class FlaskConfig:
    SECRET_KEY = config.get("SECRET_KEY")
    
    DEBUG = config.get("DEBUG", True)
    TESTING = config.get("TESTING", False)
    CSRF_ENABLED = config.get("CSRF_ENABLED", True)
    
    DEVELOPMENT = config.get("DEVELOPMENT", True)
    
    SQLALCHEMY_DATABASE_URI = DataBaseConfig.URI
    
    
    SERVER_HOST = ServerConfig.HOST
    SERVER_PORT = ServerConfig.PORT
    
    JWT_SECRET_KEY = JWTConfig.SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = JWTConfig.ACCESS_TOKEN_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES = JWTConfig.REFRESH_TOKEN_EXPIRES
    JWT_ALGORITHM = JWTConfig.ALGORITHM

  
FLASK_CONFIG = FlaskConfig()
DATA_BASE_CONFIG = DataBaseConfig()