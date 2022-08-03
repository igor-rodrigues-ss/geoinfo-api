import logging

from fastapi import FastAPI

from src.vector.urls import router as router_vector
from src.external.urls import router as router_external

from src.external.helper.client import client
from src.middlewares.catcher import catcher
from scripts.load_shapefile import load_shapefile
from src.vector.models import BrUf

logger = logging.getLogger(__name__)

app = FastAPI()

app.middleware("http")(catcher)

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
