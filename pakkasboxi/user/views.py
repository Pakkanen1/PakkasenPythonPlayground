from flask import Blueprint, request
from flask_jwt_extended import jwt_required, create_access_token, current_user
from pakkasboxi.database import db
from .models import User

blueprint = Blueprint("user", __name__)

@blueprint.route("/api/users/login", methods=["POST"])
def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        user.token = create_access_token(identity=user, fresh=True)
        return user
    else:
        return "401"

@blueprint.route("/api/user", methods=["GET"])
@jwt_required
def get_user():
    return current_user
