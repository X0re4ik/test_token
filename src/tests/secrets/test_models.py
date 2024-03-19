
import pytest

from sqlalchemy import select
from mixer.backend.sqlalchemy import mixer


from src.consumption.models import Consumption
from src.auth.models import User
from sqlalchemy_file import File, FileField
from src.secrets.models import SecretFile
from src.database import Session

@pytest.fixture(scope="function")
def secret_file(db_session):
    file = File(
        content="Hello World", 
        filename="hello.txt", 
        content_type="text/plain"
    )
    file = mixer.blend(SecretFile, file=file)
    db_session.add(file)
    db_session.commit()
    return file

def test_get_user(db_session, app, secret_file):
    
    # stmt = Session.query(Consumption).where(Consumption.user_id==user.id)
    # print(Session.execute(stmt).all())
    # print(Session.query(User).where(User.id==user.id).first().consumptions)
    print(secret_file.file)
    pass