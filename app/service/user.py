from app.db.repo.user import UserRepo
from .base import CrudService


class UserService(CrudService):
    repo = UserRepo()
