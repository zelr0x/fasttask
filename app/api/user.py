from fastapi import Depends, APIRouter, Path

from app.service.user import UserService


router = APIRouter()


@router.get("/{id}")
async def get_user(id: str = Path(..., title="User id"),
                   service: UserService = Depends()):
    return await service.get_by_id(id)
