from flask import Flask

flask_app = Flask(__name__)

from app.filters import mail_create

flask_app.jinja_env.filters['add_mail'] = mail_create

from app import routes
