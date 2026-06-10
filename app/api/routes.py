from fastapi import APIRouter
from pydantic import BaseModel
from app.graph.builder import app as flow

router = APIRouter()

 
class ResearchRequest(BaseModel):
    topic:str

@router.post("/research")
def generate_report(request: ResearchRequest):
    try:
         result = flow.invoke(
        {
            "topic": request.topic
        }
    )
         return{
        "report": result["report"],
        "sources":result["sources"]
    }
        

   

    
    except Exception as e:
        return {
            "error": str(e)
        }

