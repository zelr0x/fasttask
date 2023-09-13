from .base import BaseRepo
from ..models import User


class UserRepo(BaseRepo):
    model = User
