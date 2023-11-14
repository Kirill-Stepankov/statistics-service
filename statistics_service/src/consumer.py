import asyncio
from contextlib import asynccontextmanager

from aiokafka import AIOKafkaConsumer
from fastapi import Depends, FastAPI
from logs import logger
from logs.logger import get_logger

from .config import get_settings

settings = get_settings()
logger = get_logger()

loop = asyncio.get_event_loop()
consumer = AIOKafkaConsumer(
    settings.kafka_topic, bootstrap_servers=settings.bootstrap_servers, loop=loop
)


async def consume():
    logger.info("Starting consuming..")
    await consumer.start()
    async for msg in consumer:
        print(
            "consumed: ",
            msg.topic,
            msg.partition,
            msg.offset,
            msg.key,
            msg.value,
            msg.timestamp,
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    loop.create_task(consume())
    yield
    logger.info("Stopping consuming")
    await consumer.stop()
