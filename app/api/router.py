from fastapi import APIRouter

from . import task, user


router = APIRouter(prefix="/api")
router.include_router(task.router, prefix="/tasks", tags=["tasks"])
router.include_router(user.router, prefix="/users", tags=["users"])
