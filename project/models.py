from sqlalchemy import Column, String, Integer, Float, ForeignKey
from marshmallow import Schema, fields
from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    trailer = Column(String(), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer(), ForeignKey('genres.id'), nullable=False)
    director_id = Column(Integer(), ForeignKey('directors.id'), nullable=False)


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(ForeignKey(Genre.id))


class AuthUserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password_hash = fields.String(required=True)


class AuthRegisterRequest(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

class UserSchema(Schema):
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()