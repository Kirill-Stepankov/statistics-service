import json
from abc import ABC

from src.abstract import AbstractRepository

from .exceptions import ThereIsNoStatisticsForPostException
from .shemas import PostStatsOutputSchema


class AbstractPagesStatisticsService(ABC):
    pass


class PagesStatisticsService(AbstractPagesStatisticsService):
    def __init__(self, pages_stats_repo: AbstractRepository):
        self.pages_stats_repo: AbstractRepository = pages_stats_repo

    async def insert(self, document: dict):
        return await self.pages_stats_repo.add_one(document)

    async def update_statistics(self, payload):
        document = await self.pages_stats_repo.get_document_by_post_id(
            payload.get("post_id")
        )
        if not document:
            document = {
                "page_id": payload.get("page_id"),
                "post_id": payload.get("post_id"),
                "user_id": payload.get("user_id"),
                "user_email": payload.get("user_email"),
                payload.get("stats_type"): payload.get("operation"),
            }
            await self.pages_stats_repo.add_one(document)
            return

        await self.pages_stats_repo.update_document(
            payload.get("page_id"),
            payload.get("post_id"),
            payload.get("stats_type"),
            payload.get("operation"),
        )

    async def get_post_statistics(self, post_id: int):
        document = await self.pages_stats_repo.get_document_by_post_id(post_id)
        if not document:
            raise ThereIsNoStatisticsForPostException(post_id)
        return PostStatsOutputSchema(**document)

    async def get_posts_statistics(self):
        documents_cursor = await self.pages_stats_repo.get_documents_group_by_page()
        statistics = [document async for document in documents_cursor]
        return statistics
