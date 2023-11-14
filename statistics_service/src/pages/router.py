from fastapi import APIRouter, Depends, Header, Query, status

from .service import AbstractPagesStatisticsService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/testdb")
async def testdb(pages_stats_service: AbstractPagesStatisticsService = Depends()):
    response = await pages_stats_service.insert({"user": "key"})
    print(response)
    return {"ok": "ok"}
