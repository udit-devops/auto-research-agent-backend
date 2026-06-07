from fastapi import APIRouter
from pydantic import BaseModel
from app.graph.builder import app

router = APIRouter()

 
class ResearchRequest(BaseModel):
    topic:str

@router.post("/research")
def generate_report(request: ResearchRequest):
    result = app.invoke(
        {
            "topic": request.topic
        }
    )

    return{
        "report": result["report"]
    }

