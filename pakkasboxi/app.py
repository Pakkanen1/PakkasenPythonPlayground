from flask import Flask
from pakkasboxi.extensions import db, migrate, jwt, bcrypt
from pakkasboxi.settings import DevConfig
from pakkasboxi import blog, factions, user

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
    jwt.init_app(app)

def register_blueprints(app):
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(blog.views.blueprint)
    app.register_blueprint(factions.views.blueprint)
