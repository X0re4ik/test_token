import logging
from flask import Blueprint, jsonify
from flask_pydantic import validate
from typing import Optional
from flask_jwt_extended import \
    (create_access_token,
     create_refresh_token,
     get_jwt_identity, 
     jwt_required,
     current_user)
from sqlalchemy import update
from flask import request
from .schemas import \
    (CreateUserModel, 
     UserPartUpdate, 
     UserModel)
from .models import User

from src.database import Session


logger = logging.getLogger(__name__)

auth = Blueprint('auth', __name__)

@auth.route('/', methods=["POST"])
@validate()
def authentication(body):
    print(body)
    return jsonify({
        "success": True,
    })


@auth.route('/users/', methods=["POST"])
@validate()
def create_user(body: CreateUserModel):
    user: Optional[User] = User.find_user_by_email(body.email)
    if user:
       return jsonify({
            "email": "User with email '%s' already exists" % user.email
       }), 400
       
    new_user = User(username=body.username, email=body.email, is_active=True) 
    new_user.set_password(body.password)
    Session.add(new_user)
    Session.commit()
    
    return jsonify(
            body.model_dump(mode="json")
        ), 201


@auth.route('/users/me', methods=["GET"])
@jwt_required()
def get_me():
    user: User = current_user
    return jsonify(
        UserModel(
            email=user.email, 
            username=user.username
        ).model_dump(mode="json")
    ), 200
    

@auth.route('/users/me', methods=["PATCH"])
@jwt_required()
@validate()
def patch_me(body: UserPartUpdate):
    user: User = current_user
        
    update_data = body.model_dump(exclude_unset=True)
    stmt = update(User)\
        .where(user.email==user.email)\
        .values(**update_data)
    
    logger.info("Update data for user %s" % user.email)
    
    Session.execute(stmt)
    Session.commit()
    
    return jsonify(
        UserModel(
            email=user.email, 
            username=user.username
        ).model_dump(mode="json")
    ), 200