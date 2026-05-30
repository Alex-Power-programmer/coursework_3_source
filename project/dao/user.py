from typing import Optional

from project.dao.base import BaseDAO
from project.models import User, UserSchema, AuthUserSchema


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def get_user_by_email(self, email: str):
        user: Optional[User] = self._db_session.query(
            User,
        ).filter(
            User.email == email,
        ).one_or_none()

        if user is not None:
            return user

        return None

    def update_patch_user(self, user_data):
        user = self.get_user_by_email(user_data['email'])

        if "name" in user_data:
            user.name = user_data['name']
        if "surname" in user_data:
            user.surname = user_data['surname']
        if "favorite_genre" in user_data:
            user.favorite_genre = user_data['favorite_genre']

        self._db_session.add(user)
        self._db_session.commit()
        return UserSchema().dump(user)

