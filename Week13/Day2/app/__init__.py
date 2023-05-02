import os
from flask import Flask
import flask_migrate
import flask_sqlalchemy
from flask_bcrypt import Bcrypt

flask_app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'robots.db')
flask_app.config['SECRET_KEY'] = "123"
db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

bcrypt = Bcrypt(flask_app)

from app import models, routes