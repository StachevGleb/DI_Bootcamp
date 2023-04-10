from app import flask_app, db
from app.models import Human, Dog


@flask_app.route('/insert/<human_name>/<race>')
def insert_page(human_name, race):
    human = Human(name=human_name)
    dog = Dog(race=race, human=human)

    # db.session.add(human)
    # db.session.add(dog)
    db.session.add_all([human, dog])
    db.session.commit()

    return f"human with name {human_name} and dog with race {race} added successfully"


@flask_app.route('/show_dogs/<human_id>')
def show_dogs(human_id):
    human = Human.query.filter_by(human_id=human_id).first()
    return f"human with name"