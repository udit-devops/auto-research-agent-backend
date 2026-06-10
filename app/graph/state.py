from typing import TypedDict

class ResearchState(TypedDict):
    topic:str
    research_ques:list[str]
    research_data:dict
    research_summary:str
    analysis:str
    report:str
    sources:list[dict]
    

    