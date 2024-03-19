import logging

from typing import Literal, List, Any, Tuple
from .settings import FLASK_CONFIG, LOGGING_CONFIG
from flask import Flask


import logging
import logging.config
logger = logging.getLogger('prober')
logging.config.dictConfig(LOGGING_CONFIG.CONFIG)


class FlaskApp:
    __app = Flask(__name__)
    
    API_VERSION = 1
    
    def __init__(self) -> None:
        self.base_prefix = f"/api/v{self.API_VERSION}"
        
        self.set_blueprints()
    
    def set_blueprints(self):
        from src.secrets.views import secrets as secrets_blueprint
        from src.jwt.api import jwt as jwt_blueprint
        from src.auth.views import auth as auth_blueprint
        
        blueprints = [
            (secrets_blueprint, 'secrets'),
            (jwt_blueprint, 'jwt'),
            (auth_blueprint, 'auth'),
        ]
        self._set_blueprints(blueprints)
        return self
    
    def _set_blueprints(self, blueprints: List[Tuple[Any]]):
        for (blueprint, prefix) in blueprints:
            url_prefix = self.base_prefix + "/" + prefix
            self.__app.register_blueprint(blueprint, url_prefix=url_prefix)
        
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
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity: int = jwt_data.get("sub")
    return Session.query(User).filter_by(id=identity).one_or_none()

import os

from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy_file.storage import StorageManager


# Configure Storage
os.makedirs("./upload_dir/attachment", 0o777, exist_ok=True)
container = LocalStorageDriver("./upload_dir").get_container("attachment")
StorageManager.add_storage("default", container)

if __name__ == '__main__':
    app.run(
        host=FLASK_CONFIG.SERVER_PORT,
        port=FLASK_CONFIG.SERVER_HOST,
    )