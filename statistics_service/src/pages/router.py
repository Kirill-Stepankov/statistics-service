from typing import Any

from fastapi import APIRouter, Depends, Header, Query, status

from .service import AbstractPagesStatisticsService
from .shemas import PostStatsOutputSchema

router = APIRouter(prefix="/stats", tags=["statistics"])


@router.get("/{post_id}", response_model=PostStatsOutputSchema)
async def get_statistics(
    post_id: int, pages_stats_service: AbstractPagesStatisticsService = Depends()
) -> Any:
    return await pages_stats_service.get_post_statistics(post_id)
