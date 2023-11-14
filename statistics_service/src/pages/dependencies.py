from .repository import PagesStatisticsRepository
from .service import PagesStatisticsService


def pages_stats_service(db):
    return PagesStatisticsService(PagesStatisticsRepository(db))
