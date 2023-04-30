from flask import render_template, flash, redirect, url_for
from app import flask_app
from app import models
from app import db
import json

@flask_app.route('/')
def populate():
    with open('app/static/users.json', 'r') as file_obj:
        robots = json.load(file_obj)
    models.User.query.delete()
    for user in robots:
        model = models.User(name=user['name'], street=user['address']['street'], city=user['address']['city'], zipcode=user['address']['zipcode'])
        db.session.add(model)
    db.session.commit()
    data_user = models.User.query.all()
    data_city = models.User.query.filter_by(city='Roscoeview').all()
    data5 = models.User.query.limit(5)
    dataZip5 = models.User.query.filter(models.User.zipcode.startswith('5')).all()
    return render_template('index.html', data_user=data_user, data_city=data_city, data5=data5, dataZip5=dataZip5)


