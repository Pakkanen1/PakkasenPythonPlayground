import os
from datetime import timedelta


class Config(object):
    SECRET_KEY = os.environ.get("PAKKASBOXI_SECRET", "test")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_USERNAME_KEY = 'username'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 5)
    JWT_ACCESS_COOKIE_NAME = "pakkasen_keksi"
    JWT_COOKIE_SAMESITE = "Strict"
    JWT_COOKIE_SECURE = True
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_COOKIE_PATH = ["/api/"]
    JWT_REFRESH_COOKIE_PATH = ["/token/refresh"]

class DevConfig(Config):
    ENV = "dev"
    DEBUG = True
    DB_NAME = "pakkasboxidev.db"
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
