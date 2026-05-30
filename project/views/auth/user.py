import jwt
from flask import request, abort, current_app
from flask_restx import Namespace, Resource

from project.container import user_service

api = Namespace('user')

def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            user = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            kwargs['email'] = user['email']
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)


        return func(*args, **kwargs)

    return wrapper



@api.route('/')
class UserView(Resource):
    @auth_required
    def get(self, email):
        if not email:
            abort(400, 'Email not found in token')
        user = user_service.get_by_email(email=email)
        return user, 200

    @auth_required
    def patch(self, email):
        data = request.json
        data['email'] = email
        user = user_service.update_patch_user(data)
        return user, 204