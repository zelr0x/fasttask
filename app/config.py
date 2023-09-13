from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    app_host: str = Field(..., env="APP_HOST")
    app_port: int = Field(..., env="APP_PORT")
    app_dbg_enabled: bool = Field(..., env="APP_DBG_ENABLED")
    app_dbg_host: str = Field(default="0.0.0.0", env="APP_DBG_HOST")
    app_dbg_port: int = Field(default=5678, env="APP_DBG_PORT")
    app_dbg_wait_client: bool = Field(..., env="APP_DBG_WAIT_CLIENT")

    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')


class DbSettings(BaseSettings):
    db_uri_scheme: str = Field(..., env="DB_URI_SCHEME")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_password: str = Field(..., env="DB_PASSWORD")

    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')

    @property
    def db_url(self):
        return (
            f"{self.db_uri_scheme}://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )


@lru_cache
def app_settings():
    return AppSettings()


@lru_cache
def db_settings():
    return DbSettings()


@lru_cache
def orm_settings():
    return {
        "connections": {
            "default": db_settings().db_url
        },
        "apps": {
            "models": {
                "models": ["app.db.models"],
                "default_connection": "default",
            }
        },
    }
