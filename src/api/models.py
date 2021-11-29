from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


db = SQLAlchemy()


favorite_planets = db.Table('favorite_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('Planet.id'), primary_key=True)
)
favorite_characters = db.Table('favorite_characters',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('Character.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    favorite_planets = db.relationship('Planet', secondary=favorite_planets, lazy='subquery',
        backref=db.backref('Users', lazy=True))
    
    favorite_characters = db.relationship('Character', secondary=favorite_characters, lazy='subquery',
        backref=db.backref('Users', lazy=True))
        
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

class Character(db.Model):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    hair_colour = Column(String(250))
    eye_colour = Column(String(250))
    planet_id = Column(Integer, ForeignKey('Planet.id'))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair color": self.hair_colour,
            "eye color": self.eye_colour,
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    density = Column(Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "density": self.density
            }



