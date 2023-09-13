from uuid import UUID

from app.db.repo.base import BaseRepo


class CrudService:
    repo: BaseRepo = None

    async def get_by_id(self, id: UUID):
        return await self.repo.find_by_id(id)
