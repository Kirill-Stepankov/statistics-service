from src.config import get_settings
from src.database import aws_client, get_db

from .dependencies import pages_stats_service

settings = get_settings()


async def send_email_stats():
    async with aws_client("ses") as ses:
        stats_service = pages_stats_service(get_db())

        stats = await stats_service.get_posts_statistics()
        data = "\n".join(list(map(str, stats)))

        await ses.send_email(
            Source=settings.email_identity,
            Destination={"ToAddresses": [settings.email_identity]},
            Message={
                "Subject": {"Data": "Statistics"},
                "Body": {"Text": {"Data": data}},
            },
        )
