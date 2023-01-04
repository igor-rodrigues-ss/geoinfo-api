from fastapi import APIRouter

from src.vector.views import info
from src.vector.schemas import InfoResponseSchema
from src.openapi import DEFAULT_INTERNAL_SERVER_ERROR


router = APIRouter()


router.post(
    "/info",
    name="check-vector-info",
    response_model=InfoResponseSchema,
    responses={500: DEFAULT_INTERNAL_SERVER_ERROR},
)(info)
