from typing import Optional

# from project.dao.base import BaseDAO
from project.dao.user import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def login(self, user_data):
        user_data['password'] = user_data['password']
        return self.dao.register(user_data)