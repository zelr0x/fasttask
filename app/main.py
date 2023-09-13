import fastapi as fa
from tortoise.contrib.fastapi import register_tortoise

from app.api import router
from app.api.exc_handlers import register_handlers
from app.config import app_settings, orm_settings


def configure_dbg():
    settings = app_settings()
    if (settings.app_dbg_enabled):
        import debugpy

        endpoint = (settings.app_dbg_host, settings.app_dbg_port)
        block = settings.app_dbg_wait_client
        debugpy.listen(endpoint)
        listen_type = ", waiting client..." if block else "..."
        # TODO: Make it a warning.
        print(f"Listening for debug connections on {endpoint}{listen_type}")
        if block:
            debugpy.wait_for_client()


def create_app():
    app = fa.FastAPI()
    app.include_router(router.router)
    return app


configure_dbg()
app = create_app()
register_tortoise(app,
                  config=orm_settings(),
                  generate_schemas=False,
                  add_exception_handlers=False)
register_handlers(app)


@app.on_event("startup")
async def on_startup():
    import tortoise
    print(await tortoise.Tortoise.get_connection('default').execute_query('SELECT 1'))
