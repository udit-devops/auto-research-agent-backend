from fastapi import APIRouter
from pydantic import BaseModel
from app.graph.builder import app as flow
from app.db.database import SessionLocal
from app.db.models import Report
import json
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
         
         db = SessionLocal()
         new_report = Report(
             topic=request.topic,
             report=result["report"],
             sources=json.dumps(result["sources"])
         )
         db.add(new_report)
         db.commit()
         db.close()
            
         return{
        "report": result["report"],
        "sources":result["sources"]
    }
        

   

    
    except Exception as e:
        return {
            "error": str(e)
        }

@router.get("/reports")
def get_reports():
    db = SessionLocal()

    reports = db.query(Report).all()

    data=[]

    for report in reports:
        data.append({
            "id":report.id,
            "topic":report.topic,
            "created_at":report.created_at,
        })

    db.close()

    return data
    
@router.get("/reports/{id}")
def get_report(id: int):
    db = SessionLocal()
    report = db.query(Report).filter(Report.id==id).first()
    
    if report:
        data={
            "id":report.id,
            "topic":report.topic,
            "report":report.report,
            "sources":json.loads(report.sources),
            "created_at":report.created_at
        }
        db.close()
        return data
    else:
        db.close()
        return {
            "Error": "Report not found"
        }