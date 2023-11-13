from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    logger_config_path: str
    secret_key: str
    localstack_endpoint_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    email_identity: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
