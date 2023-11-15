from typing import Any

from .abstract import AbstractRepository
from .config import get_settings
from .database import aws_client

settings = get_settings()


class MongoDBRepository(AbstractRepository):
    collection = None

    def __init__(self, database) -> None:
        self.db = database

    async def add_one(self, document: dict | Any):
        result = await self.db[self.collection].insert_one(document)
        return result.inserted_id
