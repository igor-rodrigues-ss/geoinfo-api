import logging

from fastapi import Request, status
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


async def catcher(request: Request, call_next):
    try:
        return await call_next(request)

    except Exception as exc:
        logger.exception(exc)

        return JSONResponse(
            {"detail": "Internal Server Error"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
