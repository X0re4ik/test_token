import click
from flask.cli import AppGroup

from src.database import Session
from src.auth.models import User
from sqlalchemy import insert
auth_cli = AppGroup('auth')

@auth_cli.command('createsuperuser')
@click.argument('email', nargs=-1)
@click.argument('password', nargs=1)
def create_superuser(email, password):
    user = User(
        email=email,
        username="Superuser",
        is_superuser=True, 
        is_stuff=True, 
        is_active=True
    )
    user.password = password
    Session.add(user)
    Session.commit()