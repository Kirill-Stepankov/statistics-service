from typing import Annotated

from fastapi import Depends, FastAPI
from logs import logger

from . import config

logger = logger.get_logger()


def create_app():
    app = FastAPI()

    @app.get("/healthcheck")
    async def info(settings: Annotated[config.Settings, Depends(config.get_settings)]):
        logger.warning("TEST")

        return {
            "app_name": settings.logger_config_path,
        }

    return app


# mongodb docker, mongodb sesssion and repository, ses configurate and kafka and github workflow with testing
