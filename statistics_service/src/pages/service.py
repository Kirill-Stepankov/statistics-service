from abc import ABC

from src.abstract import AbstractRepository


class AbstractPagesStatisticsService(ABC):
    pass


class PagesStatisticsService(AbstractPagesStatisticsService):
    def __init__(self, pages_stats_repo: AbstractRepository):
        self.pages_stats_repo: AbstractRepository = pages_stats_repo

    async def insert(self, document: dict):
        return await self.pages_stats_repo.add_one(document)
