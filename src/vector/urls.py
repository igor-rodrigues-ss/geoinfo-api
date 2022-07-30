from fastapi import APIRouter
from src.vector.views import info
from src.vector.schemas import InfoResponseSchema


router = APIRouter()


router.post("/info", response_model=InfoResponseSchema)(info)
