import flask

from app.accounts import accounts

@accounts.route("/")
def index():
    return flask.render_template("index.html")