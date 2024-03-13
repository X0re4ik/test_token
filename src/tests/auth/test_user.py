
from src.database import Session
from sqlalchemy import select
from src.auth.models import User
from flask_jwt_extended import get_jwt_identity

def test_get_user(db_session, app, authorization_header):    
    response = app.test_client().get(
        '/auth/users/me', 
        headers=authorization_header
    )
    
    assert response.status_code == 200
    assert response.json["username"]
    assert response.json["email"]

def test_put_update(db_session, app, authorization_header):
    data = {
        "username": "Kotik",
        "email": "example@gmail.com",  
    }
    response = app.test_client().patch(
        '/auth/users/me',
        json=data,
        headers=authorization_header
    )
    
    assert response.status_code == 200
    assert response.json["username"] == data["username"]
    assert response.json["email"] == data["email"]
    assert User.find_user_by_email(data["email"])
    

def test_patch_update(db_session, app, authorization_header):
    data = {
        "email": "example@gmail.com",  
    }
    response = app.test_client().patch(
        '/auth/users/me',
        json=data,
        headers=authorization_header
    )

    assert response.status_code == 200
    assert response.json["username"]
    assert response.json["email"] == data["email"]
    assert User.find_user_by_email(data["email"])