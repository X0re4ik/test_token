
from src.database import Session
from sqlalchemy import select
from src.auth.models import User
from mixer.backend.sqlalchemy import mixer
from src.consumption.models import Consumption
from flask_jwt_extended import get_jwt_identity

def test_get_user(db_session, app):
    user: User = mixer.blend(User)
    consumption = mixer.blend(Consumption, user=user)
    
    Session.add_all([
        user, 
        consumption,
    ])
    Session.commit()
    print(user.id)
    stmt = Session.query(Consumption).where(Consumption.user_id==user.id)
    print(Session.execute(stmt).all())
    print(Session.query(User).where(User.id==user.id).first().consumptions)
    pass