from contextlib import asynccontextmanager

import aioboto3
from motor.motor_asyncio import AsyncIOMotorClient

from .config import get_settings

settings = get_settings()


def get_db() -> AsyncIOMotorClient:
    db_client = AsyncIOMotorClient(
        f"mongodb://{settings.mongo_initdb_root_username}:{settings.mongo_initdb_root_password}@{settings.mongo_db_host}:{settings.mongo_db_port}"
    )
    db_name = settings.mongo_db_name
    return db_client[db_name]


session = aioboto3.Session()


@asynccontextmanager
async def aws_client(service):
    async with session.client(
        service,
        endpoint_url=settings.localstack_endpoint_url,
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        region_name="us-east-1",
    ) as client:
        yield client
