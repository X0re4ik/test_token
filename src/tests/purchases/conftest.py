import pytest
from src.main import app as base_flask_app
from src.database import Session, engine, Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, scoped_session
from src.settings import DATA_BASE_CONFIG


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_jwt_extended import create_access_token
from src.db.base import Base

import contextlib




@pytest.fixture(scope="function")
def db_session(request):
    # def teardown():
    #     with engine.connect() as con:
    #         trans = con.begin()
    #         for base in [Base]:
    #             for table in reversed(base.metadata.sorted_tables):
    #                 con.execute(table.delete())
    #         trans.commit()
    # request.addfinalizer(teardown)
    return Session


@pytest.fixture()
def app():
    base_flask_app.config.update({
        "TESTING": True,
    })
    with base_flask_app.app_context():
        yield base_flask_app

@pytest.fixture()
def client(app):
    return app.test_client()


from src.auth.models import User
from mixer.backend.sqlalchemy import mixer

@pytest.fixture
def super_user():
    user = mixer.blend(
        User,
        id=1,
        is_superuser=True, 
        is_stuff=True, 
        is_active=True
    )
    Session.add(user)
    Session.commit()
    return user
    


@pytest.fixture(scope="function")
def authorization_header(super_user):
    access_token = create_access_token(identity=super_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    return headers


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
