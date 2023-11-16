import asyncio
import json
from contextlib import asynccontextmanager

from aiokafka import AIOKafkaConsumer
from fastapi import Depends, FastAPI
from logs import logger
from logs.logger import get_logger

from .config import get_settings

settings = get_settings()
logger = get_logger()


class Consumer:
    def __init__(self, loop, kafka_consumer, pages_stats_service) -> None:
        self.loop = loop
        self.consumer = kafka_consumer
        self.pages_stats_service = pages_stats_service

    async def consume(self):
        logger.info("Starting consuming..")
        await self.consumer.start()
        async for msg in self.consumer:
            await self.pages_stats_service.update_statistics(msg.value)

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        self.loop.create_task(self.consume())
        yield
        logger.info("Stopping consuming")
        await self.consumer.stop()
