from flask import Blueprint, jsonify
from flask_pydantic import validate

from .serializers import AuthenticationModel

auth = Blueprint('auth', __name__)

@auth.route('/', methods=["POST"])
@validate()
def authentication(body: AuthenticationModel):
    print(body)
    return jsonify({
        "success": True,
    })
