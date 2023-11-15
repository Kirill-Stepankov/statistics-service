from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from src.pages.exceptions import ThereIsNoStatisticsForPostException


async def no_statistics(request: Request, exc: ThereIsNoStatisticsForPostException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": f"There is no statistics for post {exc.post_id}."},
    )


def init_exception_handlers(app: FastAPI):
    app.exception_handler(ThereIsNoStatisticsForPostException)(no_statistics)
