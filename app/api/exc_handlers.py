from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from tortoise.exceptions import DoesNotExist, IntegrityError

from app.util.exceptions import NotFoundException


def register_handlers(app: FastAPI):

    # Handlers for lib exceptions.

    @app.exception_handler(DoesNotExist)
    async def doesnotexist_exc_handler(request: Request,
                                       exc: DoesNotExist):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "description": "Could not find requested resource",
                "detail": [{
                    "type": "NotFoundError",
                    "msg": str(exc)
                }]
            })

    @app.exception_handler(IntegrityError)
    async def integrityerror_exc_handler(request: Request,
                                         exc: IntegrityError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "description": "Unable to process request",
                "detail": [{
                    "type": "IntegrityError",
                    "msg": str(exc)
                }]
            })

    # Handlers for custom exceptions.

    @app.exception_handler(DoesNotExist)
    async def notfound_exc_handler(request: Request,
                                   exc: NotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "description": "Could not find requested resource",
                "detail": [{
                    "type": "NotFoundError",
                    "msg": str(exc)
                }]
            })
