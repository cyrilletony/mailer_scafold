import datetime
from __init__ import env

class ConfigClass(object):
    env = env.environ
    
    SECRET_KEY = env.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI') 
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/mailer_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_MAX_OVERFLOW = 50
    SESSION_TYPE = 'sqlalchemy'
    MAX_CONTENT_LENGTH = 1024 * 1024 * 15
    MAIL_SERVER = env.get('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = env.get('MAIL_USERNAME')
    MAIL_PASSWORD = env.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = env.get('MAIL_DEFAULT_SENDER')
    USER_COPYRIGHT_YEAR = datetime.datetime.strftime(datetime.datetime.now(), '%Y')
    USER_CORPORATION_NAME = "AByte Corp"
    USER_APP_VERSION = "v1.0"
    USER_APP_NAME = "Mailer App"
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = False
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = env.get('USER_EMAIL_SENDER_EMAIL')
    DEBUG = True