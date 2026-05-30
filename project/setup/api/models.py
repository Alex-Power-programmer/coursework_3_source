from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})
director: Model = api.model('Режиссер', {
    "id": fields.Integer(required=True, example=1),
    "name": fields.String(required=True, max_length=100, example='Тейлор Шеридан'),
})

movie: Model = api.model("Movie", {
    "id": fields.Integer(required=True, example=1),
    "title": fields.String(example= "Упс... Приплыли!"),
    "description": fields.String(example="От Великого потопа зверей спас ковчег. Но спустя полгода скитаний они готовы сбежать с него куда угодно. Нервы на пределе. Хищники готовы забыть про запреты и заглядываются на травоядных. Единственное спасение — найти райский остров. Там простор и полно еды. Но даже если он совсем близко, будут ли рады местные такому количеству гостей?"),
    "trailer": fields.String(example="https://www.youtube.com/watch?v=Qjpmysz4x-4"),
    "year": fields.Integer(example=2020),
    "rating": fields.Float(example=5.9),
    "genre_id": fields.Integer(example=16),
    "director_id": fields.Integer(example=19),
    "pk": fields.Integer(example=20)
})
