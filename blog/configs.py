import os

FLASK_ADMIN_SWATCH = 'vapor'


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\Users\\olegy\\Desktop\\Blog\\blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"
    WTF_CSRF_ENABLED = True


class DevConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


OPENAPI_URL_PREFIX = '/api/swagger'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.22.0'
