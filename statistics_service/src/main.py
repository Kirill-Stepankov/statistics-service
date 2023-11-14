from functools import partial
from typing import Annotated

from fastapi import Depends, FastAPI
from logs import logger
from src.pages.dependencies import pages_stats_service
from src.pages.router import router
from src.pages.service import AbstractPagesStatisticsService

from . import config
from .database import get_db

logger = logger.get_logger()


def create_app():
    app = FastAPI()

    app.include_router(router)

    db = get_db()

    app.dependency_overrides[AbstractPagesStatisticsService] = partial(
        pages_stats_service, db
    )

    @app.get("/healthcheck")
    async def info(settings: Annotated[config.Settings, Depends(config.get_settings)]):
        logger.warning("TEST")

        return {
            "app_name": settings.logger_config_path,
        }

    return app


# ses configurate and kafka

# there is a db: picdb
# there are collections: likes,
