
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def sampleEndpoint():
    return "This is a sample endpoint"