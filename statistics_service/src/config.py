from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    logger_config_path: str
    secret_key: str
    localstack_endpoint_url: str
    aws_access_key_id: str
    aws_secret_access_key: str
    email_identity: str

    mongo_db_name: str
    mongo_db_host: str
    mongo_db_port: int
    mongo_db_username: str
    mongo_db_password: str
    mongo_db_auth_mechanism: str

    mongo_initdb_root_username: str
    mongo_initdb_root_password: str

    bootstrap_servers: str
    kafka_topic: str

    kafka_advertised_listeners: str
    kafka_listener_security_protocol_map: str
    kafka_listeners: str
    kafka_inter_broker_listener_name: str
    kafka_zookeeper_connect: str

    celery_broker_url: str
    celery_backend_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
