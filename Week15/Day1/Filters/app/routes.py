import flask

from app import flask_app


@flask_app.route('/name')
def main_page():
    return flask.render_template("main.html", name=name)
