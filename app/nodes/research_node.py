from app.graph.state import ResearchState
from app.services.tavily_service import tavily_client

def research_node(state: ResearchState):
    questions = state['research_ques']
    all_results = []
    for question in questions:
        result = tavily_client.search(question)
        all_results.append({question: result})
    
    return {
        "research_data": all_results
    }