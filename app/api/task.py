from fastapi import APIRouter, Path


router = APIRouter()


@router.get("/{id}")
async def get_task(id: str = Path(..., title="Task id")):
    return {"error": "Not implemented"}  # FIXME: implement
