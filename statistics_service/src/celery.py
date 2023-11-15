import asyncio

from celery import Celery
from celery.schedules import crontab
from logs.logger import get_logger
from src.config import get_settings
from src.pages.utils import send_email_stats

settings = get_settings()
logger = get_logger()

app = Celery(
    "statistics", broker=settings.celery_broker_url, backend=settings.celery_backend_url
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        send_statistics.s(),
        name="unblock pages due to its unblock date",
    )


@app.task
def send_statistics():
    logger.info("Executing email sending task...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_email_stats())

    logger.info("Email is sent.")
