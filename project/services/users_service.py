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

    def get_by_email(self, email: str):
        return self.dao.get_user_by_email(email)

    def update_patch_user(self, data_user):
        return self.dao.update_patch_user(data_user)
