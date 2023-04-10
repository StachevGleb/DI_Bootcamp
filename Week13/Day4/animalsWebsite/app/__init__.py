
import flask_migrate
import flask_sqlalchemy
from flask import Flask

flask_app = Flask(__name__)

flask_app.config['SECRET_KEY'] = '8621a178fa36f43ad89fd885015b7b46eb0a98708c94a3d598124d40e0a60b382bcef7b60e5a917818bb5674fadb3041060bbfe5e42dcc86'

db_info = {'host': 'localhost',
           'database': 'animals_web',
           'psw': 'Lena091165',
           'user': 'postgres',
           'port': ''}

flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from app import routes, models


