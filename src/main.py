from http import HTTPStatus

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.external.helper.client import client
from src.vector.urls import router as router_vector
from src.external.urls import router as router_external


app = FastAPI()


app.include_router(router_external, prefix="/external", tags=["External"])
app.include_router(router_vector, prefix="/vector", tags=["Vector"])


@app.on_event("shutdown")
async def shutdown():
    await client.aclose()


@app.exception_handler(Exception)
async def http_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": HTTPStatus.INTERNAL_SERVER_ERROR.phrase},
    )
