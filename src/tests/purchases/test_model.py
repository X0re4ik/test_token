
from src.database import Session
from src.auth.models import User
from mixer.backend.sqlalchemy import mixer
from src.consumption.models import Consumption
from src.purchases.models import Purchase
from src.tags.models import Tag

def test_get_user(db_session, app):
    user: User = mixer.blend(User)
    purchase: Purchase = mixer.blend(
        Purchase,
        owner=user,
        price=1000,
        currency="USD",
    )
    
    purchase.tags.extend(
        [
            mixer.blend(Tag), 
            mixer.blend(Tag)
        ]
    )
    
    print("dasdasda")
    
    Session.add_all([
        user, 
        purchase,
    ])
    Session.commit()
    
    
    # print(user.id)
    stmt: Purchase = Session.query(Purchase).where(Purchase.owner_id==user.id).first()
    print(stmt)
    # print(stmt.tags)
    # stmt.tags.clear()
    # Session.commit()
    # print(Session.query(Purchase).where(Purchase.owner_id==user.id).first().tags)
    # print(Session.query(User).where(User.id==user.id).first().consumptions)
    