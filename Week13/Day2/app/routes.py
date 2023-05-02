from flask import render_template, flash, redirect, url_for
from app import flask_app
from app import models
from app import db, bcrypt
import json
from app.forms import FormLogin

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

@flask_app.route('/login', methods=('GET', 'POST'))
def login():
    form = FormLogin()
    if form.validate_on_submit():
        if form.address.data.isdigit() or form.name.data.isdigit():
            flash('Not correct! Seems to be char not digit', 'error')
            return redirect(url_for('login'))
        else:
            address = form.address.data
            name = form.name.data
            return redirect(url_for('add_user', name=name, address=address))
    return render_template('login.html', form=form)

@flask_app.route('/user/<name>/<address>')
def add_user(name, address):
    return render_template('add_user.html', address=address, name=name)
