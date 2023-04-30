import flask

from app.films import films


@films.route("/")
def list_of_films():
    return flask.render_template("homepage.html")
