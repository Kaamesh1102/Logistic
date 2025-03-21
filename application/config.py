class Config():
    DEBUG = False
    SQL_ALCHEMY_TRACK_MODIFICATIONS = True

class LocalDevelopmentCongif(Config):
    SQL_ALCHEMY_DATABASE_URL = "sqlite:///lmsv2.sqlite3"
    DEBUG = True

    SECRET_KEY = "this-is-a-secret-key"
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "this is salt"
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"