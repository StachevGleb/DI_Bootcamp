from app import flask_app
from flask import render_template, redirect, url_for

from app import models


@flask_app.route('/')
def index():
    return render_template('index.html')
    return reqdirect(url_for('pets'))

@flask_app.route('/pets')
def pets():
    all_pets = models.Pet.query.all()
    return render_template('pets.html', pets=all_pets)

@flask_app.route('/pet/<int:pet_id>')
def pet(pet_id):
    pet = models.Pet.query.filter_by(id=pet_id).first()
    return render_template('pet.html', pet_details=pet)

@flask_app.route('/add_pet/<int:pet_id>')
def add_to_cart(pet_id):
    pet = models.Pet.query.filter_by(id=pet_id).first()
    return redirect(url_for('pets'))

@flask_app.route('/cart')
def cart():
    return render_template('cart.html')