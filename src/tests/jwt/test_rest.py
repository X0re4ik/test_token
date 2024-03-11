
from src.database import Session
from sqlalchemy import select
from src.auth.models import User
from flask_jwt_extended import get_jwt_identity

def test_request_example(db_session, app, authorization_header):
    
    #print(mocker_db_session)
    #print(db_session1)
    #Session.begin()
    query = select(User)
    #print(db_session)
    #print(authorization_header)
    
    response = app.test_client().get('/jwt/simple', headers=authorization_header)
    print(response)
    row = Session.execute(query)
    #print(row.all())
    
    
# def test_1request_example(client, db_session):
#     response = client.get("/jwt/simple")
    
#     print(dir(response), response.status_code, response.json)
#     print(response)