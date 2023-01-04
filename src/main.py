import logging

from http import HTTPStatus

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.vector.models import BrUf
from src.external.helper.client import client
from scripts.load_shapefile import load_shapefile
from src.vector.urls import router as router_vector
from src.external.urls import router as router_external


logger = logging.getLogger(__name__)


app = FastAPI()

app.include_router(router_external, prefix="/external", tags=["External"])
app.include_router(router_vector, prefix="/vector", tags=["Vector"])


@app.on_event("startup")
async def startup():
    if not await BrUf.exists():
        logger.info("Load BR_UF_2021 layer.")
        await load_shapefile()


@app.on_event("shutdown")
async def shutdown():
    await client.aclose()


@app.exception_handler(Exception)
async def http_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": HTTPStatus.INTERNAL_SERVER_ERROR.phrase},
    )
