import tortoise
from tortoise.models import Model

from app.util.exceptions import NotFoundException


class BaseRepo:
    model: Model

    async def find_by_id(self, id) -> Model:
        try:
            return await self.model.filter(pk=id).get()
        except tortoise.exceptions.DoesNotExist as ex:
            raise NotFoundException(
                f"No {self.model.__name__} found with id '{id}'"
            ) from ex
