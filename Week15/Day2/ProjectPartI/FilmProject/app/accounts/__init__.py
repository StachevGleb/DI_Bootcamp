from flask import Blueprint

accounts = Blueprint('accounts', __name__, template_folder='views', static_folder='static')


from app.accounts import routes