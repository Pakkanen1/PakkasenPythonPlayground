from flask import jsonify
from flask import Blueprint, request, redirect, render_template
from flask_jwt_extended import jwt_required, get_current_user, \
    create_access_token, set_access_cookies, create_refresh_token, set_refresh_cookies
from .models import User

blueprint = Blueprint("user", __name__)

@blueprint.route("/login", methods=["GET", "POST"])
def load_login_page():
    error = None
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user is not None and user.check_password(request.form["password"]):
            return _create_access_cookies(user)
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)

@blueprint.route("/token/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_current_user()
    token = create_access_token(identity=current_user)
    response = jsonify({"refresh": True})
    set_access_cookies(response, token)
    return response

@blueprint.route("/api/user", methods=["GET"])
@jwt_required()
def get_user():
    user = get_current_user()
    return {"id": user.id, "username": user.username}

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

def _create_access_cookies(identity):
    token = create_access_token(identity=identity, fresh=True)
    refresh = create_refresh_token(identity=identity)
    response = jsonify({"msg": "login successful"})
    set_access_cookies(response, token)
    set_refresh_cookies(response, refresh)
    return response
