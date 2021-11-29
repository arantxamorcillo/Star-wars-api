"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend"
    }

    return jsonify(response_body), 200


@api.route("/people", methods = ['GET'])
def get_people():
    characters = Character.query.all()
    characters = list(map (lambda character: character.serialize(), characters))
    return jsonify(characters), 200

@api.route('/people/<int:people_id>', methods = ['GET'])
def get_people_by_id():
    character = Character.filter_by(id = people_id)
    return jsonify(character.serialize()), 200

@api.route("/planets", methods = ['GET'])
def get_planets():
    planets = Planet.query.all()
    planets = list(map (lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

@api.route('/planet/<int:planet_id>', methods = ['GET'])
def get_planet_by_id():
    planet = Planet.filter_by(id = planet_id)
    return jsonify(planet.serialize()), 200

@api.route('/users', methods =['GET'])
def get_users():
    users = User.query.all()
    users = list(map (lambda user: user.serialize(), users))
    return jsonify(users), 200

@api.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):
    user = User.query.get(user_id)
    favorites = []
    for character in user.favorite_characters:
        favorites.apiend(character.name)
    for planet in user.favorite_planets:
        favorites.apiend(planet.name)

    return jsonify(favorites), 200

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    planet = Planet.query.get("planet_id")
    user_id = request.json.get("userId")
    user.favorites_planets.apiend(planet_id)
    db.session.commit()
    return jasonfy(planet.serialize()),200

@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    character = Character.query.get("people_id")
    user_id = request.json.get("userId")
    user.favorites_characters.apiend(character_id)
    db.session.commit()
    return jasonfy(character.serialize()),200

@api.route('/favorite/people/<int:character_id>', methods=['DELETE'])
def delete_favorite_character(character_id):
    character = Character.query.get(character_id)
    user = User.query.get(1)
    character_position = user.favorite_characters.index(character)
    user.favorite_characters.pop(character_position)
    db.session.commit()
    return jsonify(character.serialize()), 200

@api.route('/favorite/planets/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    planet = Planet.query.get(planet_id)
    user = User.query.get(1)
    planet_position = user.favorite_planets.index(planet)
    user.favorite_planets.pop(planet_position)
    db.session.commit()
    return jsonify(planet.serialize()), 200