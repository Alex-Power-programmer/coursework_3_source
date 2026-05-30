from project.dao import GenresDAO, DirectorsDAO, MoviesDAO
from project.dao.auth import AuthDAO
from project.dao.user import UsersDAO

from project.services import GenresService, MoviesService, DirectorsService
from project.services.auth_service import AuthService
from project.services.users_service import UsersService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)
auth_dao = AuthDAO(db.session)
# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService(dao=auth_dao)