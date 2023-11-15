from src.repository import MongoDBRepository


class PagesStatisticsRepository(MongoDBRepository):
    collection = "pages"

    async def get_document_by_page_id(self, page_id: int):
        return await self.db[self.collection].find_one({"page_id": page_id})

    async def update_document(
        self, page_id: int, post_id: int, stats_type: str, operation
    ):
        await self.db[self.collection].update_one(
            {"page_id": page_id, "post_id": post_id},
            {"$inc": {stats_type: operation or -1}},
        )
