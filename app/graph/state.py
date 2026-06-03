from typing import TypedDict

class ResearchState(TypedDict):
    topic:str
    research_ques:list[str]
    research_data:dict
    analysis:str
    report:str
    

    