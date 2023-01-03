import logging

from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


async def catcher(request: Request, call_next):
    try:
        return await call_next(request)

    except Exception as exc:
        logger.exception(exc)

        return JSONResponse(
            {"detail": HTTPStatus.INTERNAL_SERVER_ERROR.phrase},
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        )
