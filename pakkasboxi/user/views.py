from flask import Blueprint, request, redirect, render_template, url_for
from flask_jwt_extended import jwt_required, create_access_token, current_user
from .models import User

blueprint = Blueprint("user", __name__)

@blueprint.route("/login", methods=["GET", "POST"])
def load_login_page():
    error = None
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user is not None and user.check_password(request.form["password"]):
            user.token = create_access_token(identity=user, fresh=True)
            return redirect(url_for('factions.load_factions_page'))
        else:
            error = "Invalid Crendentials"
    return render_template('login.html', error=error)

@blueprint.route("/api/users/login", methods=["POST"])
def login_user():
    request_data = request.get_json()
    user = User.query.filter_by(username=request_data["username"]).first()
    if user is not None and user.check_password(request_data["password"]):
        user.token = create_access_token(identity=user, fresh=True)
        return user
    else:
        return "401"

@blueprint.route("/api/user", methods=["GET"])
@jwt_required()
def get_user():
    return current_user

@blueprint.route("/api/users/admin/init", methods=["POST"])
def initialize_admin_user():
    if not _admin_exists_in_database():
        request_data = request.get_json()
        salsa = request_data["salsa"]
        new_user = User("olav", salsa).save()
        return {"id": new_user.id, "username": new_user.username}
    else:
        return redirect("https://www.youtube.com/watch?v=AyMBu6cgA4E")


def _admin_exists_in_database():
    return User.query.filter_by(username="olav").first() is not None
