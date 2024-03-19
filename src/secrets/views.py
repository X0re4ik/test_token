
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
from sqlalchemy_file import File, FileField
from src.secrets.schemas import SecretFileModel
from src.secrets.models import SecretFile
from src.tags.models import Tag
from src.database import Session
from pydantic import Field

secrets = Blueprint('Secrets', __name__)

@secrets.post('/')
@validate()
def create(body: SecretFileModel):
    data = body.model_dump(exclude=['tags'])
    with Session() as session:
        sf = SecretFile(**data)
        sf.tags.extend([
            session.query(Tag).get(tag)
            for tag in body.tags
        ])
        session.add(sf)
        session.commit()
    answer = {
        "secretToken": "",
    }
    return jsonify(**data), 201
