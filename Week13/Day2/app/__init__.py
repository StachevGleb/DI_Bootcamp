import os
from flask import Flask
import flask_migrate
import flask_sqlalchemy

flask_app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'robots.db')

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import models, routes