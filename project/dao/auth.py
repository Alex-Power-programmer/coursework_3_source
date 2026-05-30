from typing import Optional

from project.dao.base import BaseDAO
from project.models import User, AuthUserSchema


class AuthDAO(BaseDAO):
    def create(self, email: str, password: str) -> AuthUserSchema:
        new_user = User(
            email=email,
            password_hash=password
        )
        self._db_session.add(new_user)
        self._db_session.commit()

        return AuthUserSchema().dump(new_user)

    def get_user_by_email(self, email: str) -> Optional[AuthUserSchema]:
        user: Optional[User] = self._db_session.query(
            User,
        ).filter(
            User.email == email,
        ).one_or_none()

        if user is not None:
            return AuthUserSchema().dump(user)

        return None

