from fastapi import APIRouter

from src.openapi import DEFAULT_INTERNAL_SERVER_ERROR

from src.external.views import search_ip
from src.external.openapi import SEARCH_IP_BAD_REQUEST
from src.external.schemas import SeachIPResponseSchema


router = APIRouter()


router.get(
    "/ip",
    name="get-external-ip",
    response_model=SeachIPResponseSchema,
    responses={400: SEARCH_IP_BAD_REQUEST, 500: DEFAULT_INTERNAL_SERVER_ERROR},
)(search_ip)
