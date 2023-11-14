import asyncio
from functools import partial
from typing import Annotated

from aiokafka import AIOKafkaConsumer
from fastapi import Depends, FastAPI
from src.pages.dependencies import pages_stats_service
from src.pages.router import router
from src.pages.service import AbstractPagesStatisticsService

from . import config
from .consumer import Consumer
from .database import get_db

settings = config.get_settings()


def create_app():
    loop = asyncio.get_event_loop()
    kafka_consumer = AIOKafkaConsumer(
        settings.kafka_topic, bootstrap_servers=settings.bootstrap_servers, loop=loop
    )

    db = get_db()

    consumer = Consumer(loop, kafka_consumer, pages_stats_service(db))

    app = FastAPI(lifespan=consumer.lifespan)

    app.include_router(router)

    app.dependency_overrides[AbstractPagesStatisticsService] = partial(
        pages_stats_service, db
    )

    @app.get("/healthcheck")
    async def info(settings: Annotated[config.Settings, Depends(config.get_settings)]):
        return {
            "app_name": settings.logger_config_path,
        }

    return app


# осталось: end stats service, endpoint for getting page stats by id, celery schedule task, sending email to admin
