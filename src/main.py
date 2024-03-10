from typing import Literal
from .settings import FLASK_CONFIG
from flask import Flask


app = Flask(__name__)

from src.jwt.api import jwt
from src.auth.views import auth
from src.auth.commands import create_superuser
app.config.from_object(FLASK_CONFIG)


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(jwt, url_prefix='/jwt')
app.cli.add_command(create_superuser)



if __name__ == '__main__':
    app.run(
        host=FLASK_CONFIG.SERVER_PORT,
        port=FLASK_CONFIG.SERVER_HOST,
    )