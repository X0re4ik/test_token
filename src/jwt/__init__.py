
from flask_jwt_extended import JWTManager

from src.auth.models import User
from src.main import app
from src.database import session

jwt = JWTManager(app=app)

@jwt.user_identity_loader
def user_identity_lookup(user: User):
    return user

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity: int = jwt_data.get("sub")
    print(identity)
    return session.query(User).filter_by(id=identity).one_or_none()