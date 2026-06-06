from fastapi import APIRouter
from pydantic import BaseModel

class ResearchRequest(BaseModel):
    topic:str

router = APIRouter()

