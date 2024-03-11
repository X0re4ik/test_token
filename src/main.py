from typing import Literal
from .settings import FLASK_CONFIG
from flask import Flask





class FlaskApp:
    __app = Flask(__name__)
    
    def __init__(self) -> None:
        from src.jwt.api import jwt
        from src.auth.views import auth
        from src.auth.commands import create_superuser
        
        self.__app.config.from_object(FLASK_CONFIG)
        
        self.__app.register_blueprint(jwt, url_prefix='/jwt')
        self.__app.register_blueprint(auth, url_prefix='/auth')
        
        self.__app.cli.add_command(create_superuser)
        
    
    @property
    def app(self):
        return self.__app


def create_app():
    return FlaskApp().app

app = create_app()

from flask_jwt_extended import JWTManager

from src.auth.models import User
from src.database import Session

jwt = JWTManager(app=app)

@jwt.user_identity_loader
def user_identity_lookup(user: User):
    print("User.id", user.id)
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity: int = jwt_data.get("sub")
    return Session.query(User).filter_by(id=identity).one_or_none()

if __name__ == '__main__':
    app.run(
        host=FLASK_CONFIG.SERVER_PORT,
        port=FLASK_CONFIG.SERVER_HOST,
    )