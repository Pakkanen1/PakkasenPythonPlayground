from flask import Flask
from pakkasboxi.extensions import db, migrate, jwt, bcrypt
from pakkasboxi.settings import DevConfig
from pakkasboxi import blog, factions, user
from pakkasboxi.user.models import User

def create_app(config_obj=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.user_lookup_loader(user_lookup_callback)
    jwt.user_identity_loader(user_identity_loader)
    jwt.init_app(app)

def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(blog.views.blueprint)
    app.register_blueprint(factions.views.blueprint)

@jwt.user_identity_loader
def user_identity_loader(user_object):
    return user_object.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

