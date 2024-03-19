
import io
from flask_jwt_extended import get_jwt_identity
from src.secrets.models import SecretFile
from src.database import Session

def test_get_user(db_session, app):
    payload = {
        "title": "asdasd",
        "description": "sfdfsdf",
        "tags": [],
    }
    
    response = app.test_client().post(
        '/api/v1/secrets/',
        json=payload,
    )
    
    assert response.status_code == 201
    # assert 
    #print(Session.query(SecretFile).all())
