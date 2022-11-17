from flask import Blueprint, request, redirect
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

@blueprint.route("/api/users/admin/init", methods=["POST"])
def initialize_admin_user():
    if not _admin_exists_in_database():
        request_data = request.get_json()
        salsa = request_data["salsa"]
        new_user = User("olav", salsa).save()
        new_user.user.token = create_access_token(identity=new_user.user)
    else:
        return redirect("https://www.youtube.com/watch?v=AyMBu6cgA4E")


def _admin_exists_in_database():
    return User.query.filter_by(username="olav").first() is not None
