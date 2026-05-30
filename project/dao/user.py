from project.dao.base import BaseDAO
from project.models import User


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def register(self, user_data):
        new_user = User(**user_data)
        self._db_session.add(new_user)
        self._db_session.commit()

        # return UserSchema().dump(new_user)

    def update_user(self, user_data):
        user = self.get_by_id(user_data['id'])

        user.email = user_data['email']
        user.password = user_data['password']
        user.name = user_data['name']
        user.surname = user_data['surname']
        user.favorite_genre = user_data['favorite_genre']

        self._db_session.add(user)
        self._db_session.commit()
        # return UserSchema().dump(user)


    def update_patch_user(self, user_data):
        user = self.get_by_id(user_data['id'])

        if "email" in user_data:
            user.email = user_data['email']
        if "password" in user_data:
            user.password = user_data['password']
        if "name" in user_data:
            user.name = user_data['name']
        if "surname" in user_data:
            user.surname = user_data['surname']
        if "favorite_genre" in user_data:
            user.favorite_genre = user_data['favorite_genre']

        self._db_session.add(user)
        self._db_session.commit()
        # return UserSchema().dump(user)
