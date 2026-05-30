import datetime
from typing import Optional, Dict

from flask import abort, current_app

from project.dao.auth import AuthDAO
from project.exceptions import UserNotFound
from project.models import AuthUserSchema
from project.tools.security import generate_password_hash, compose_password
import jwt


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    @staticmethod
    def __generate_tokens(user: AuthUserSchema):

        payload = {
            "email": user['email'],
            "id": user['id'],
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        }

        access_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        payload['exp'] = datetime.datetime.now() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
        refresh_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def register(self, email: str, password: Optional[str]) -> AuthUserSchema:
        password_hash = generate_password_hash(password)
        return self.dao.create(email=email, password=password_hash)


    def login(self, email: str, password: Optional[str], is_refresh: bool =False) -> Dict[str, str]:
        user: Optional[AuthUserSchema] = self.dao.get_user_by_email(email=email)
        if user is None:
            raise UserNotFound

        if not is_refresh:
            if not compose_password(user['password_hash'], password):
                abort(400)

        return self.__generate_tokens(user)

    def approve_refresh_token(self, refresh_token):
        try:
            user = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except Exception as e:
            print(e)
            return e

        email = user['email']
        return self.login(email=email, password=None, is_refresh=True)




