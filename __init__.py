import datetime, os, pymysql
from flask import *
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

from dotenv import load_dotenv

#load the environment variables from .env
load_dotenv()
env = os
from config.config import ConfigClass


# Create Flask app load app.config
app = Flask(__name__,  template_folder='templates')
app.config.from_object(__name__+'.ConfigClass')

# Initialize Flask-BabelEx
babel = Babel(app)

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

#calls database classes from database folder
from database.database import *

app.config['SESSION_SQLALCHEMY'] = db

#user manager
user_manager = UserManager(app, db, User)