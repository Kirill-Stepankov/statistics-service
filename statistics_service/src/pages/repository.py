from src.repository import MongoDBRepository


class PagesStatisticsRepository(MongoDBRepository):
    collection = "likes"
