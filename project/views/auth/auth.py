from typing import Dict

from flask import request
from flask_restx import Namespace, Resource, fields

from project.container import auth_service
from project.models import AuthRegisterRequest

api = Namespace('auth')

docs_model = api.model('AuthRegisterRequest', {
    'email': fields.String(required=True),
    "password": fields.String(required=True),
})

out_token = api.model('Tokens', {
    "refresh_token": fields.String(required=True)
})


@api.route('/register/')
class RegisterView(Resource):
    @api.expect(docs_model)
    def post(self):
        data = request.json
        validated_data = AuthRegisterRequest().load(data)

        auth_service.register(email=validated_data['email'], password=validated_data['password'])

        return '', 201


@api.route('/login/')
class LoginView(Resource):
    @api.expect(docs_model)
    @api.response(201, description='Tokens for authorization')
    def post(self):
        data = request.json
        validated_data = AuthRegisterRequest().load(data)

        tokens: Dict[str, str] = auth_service.login(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return tokens, 201

    @api.expect(out_token)
    @api.response(201, description='Tokens (refresh)')
    def put(self):
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201