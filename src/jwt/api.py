
from typing import Optional
from flask import Blueprint, jsonify
from flask_jwt_extended import \
    (create_access_token,
     create_refresh_token,
     get_jwt_identity, 
     jwt_required,
     current_user)
from flask_pydantic import validate
from sqlalchemy import select

from src.auth.models import User
from .schemas import LoginModel
from src.database import Session

jwt = Blueprint('jwt', __name__)

@jwt.route('/create', methods=["POST"])
@validate()
def create(body: LoginModel):
    user: Optional[User] = Session.query(User).filter_by(email=body.email).one_or_none()
    if (user is None) or (not user.check_password(body.password)):
        return jsonify({
                "success": False,
                "message": "email or password is not valid"
            }), 401

    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    
    return jsonify({
            "access": access_token,
            "refresh": refresh_token
        }), 200


@jwt.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify({
            "access": access_token
        }), 200
    

@jwt.route("/simple", methods=["GET"])
@jwt_required()
def simple():
    user = User(username="Ferretik55", email="xoore4ik@gmail.com", password_hash="4242443123dsfg")
    _user: User = current_user
    print("_user", _user.email)
    Session.add(user)
    Session.commit()
    
    return jsonify({
            "access": "1231",
        }), 200