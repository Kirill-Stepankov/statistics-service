from functools import partial
from typing import Annotated

from fastapi import Depends, FastAPI
from src.pages.dependencies import pages_stats_service
from src.pages.router import router
from src.pages.service import AbstractPagesStatisticsService

from . import config
from .consumer import lifespan
from .database import get_db


def create_app():
    app = FastAPI(lifespan=lifespan)

    app.include_router(router)

    db = get_db()

    app.dependency_overrides[AbstractPagesStatisticsService] = partial(
        pages_stats_service, db
    )

    @app.get("/healthcheck")
    async def info(settings: Annotated[config.Settings, Depends(config.get_settings)]):
        return {
            "app_name": settings.logger_config_path,
        }

    return app
