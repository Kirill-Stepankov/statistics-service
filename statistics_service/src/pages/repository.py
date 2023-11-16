from src.repository import MongoDBRepository


class PagesStatisticsRepository(MongoDBRepository):
    collection = "pages"

    async def get_document_by_post_id(self, post_id: int):
        return await self.db[self.collection].find_one({"post_id": post_id})

    async def update_document(
        self, page_id: int, post_id: int, stats_type: str, operation
    ):
        await self.db[self.collection].update_one(
            {"page_id": page_id, "post_id": post_id},
            {"$inc": {stats_type: operation or -1}},
        )

    async def get_documents_group_by_page(self):
        documents_cursor = self.db[self.collection].aggregate(
            [{"$group": {"_id": "$page_id", "totalAmountOfLikes": {"$sum": "$like"}}}]
        )
        return documents_cursor
