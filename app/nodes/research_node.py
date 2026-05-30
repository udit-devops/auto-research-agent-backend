from app.graph.state import ResearchState
from app.services.tavily_service import tavily_client

def research_node(state: ResearchState):
    topic = state['topic']
    result = tavily_client.search(topic)
    return {
        "research_data": result
    }