class DefaultConfig:
    DEBUG = True
    SECRET_KEY = 'must_be_secret'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT = 'must_be_secret_too'
    SECURITY_TRACKABLE = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MIGRATE_COMPARE_TYPE = True
