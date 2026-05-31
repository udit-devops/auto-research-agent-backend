from app.graph.state import ResearchState
from app.services.groq_service import llm

def analysis_node(state:ResearchState):
    research_data = state['research_data']
    prompt = f"""" research result: {research_data}"Read theses research result and extract the key findings and summarize important insights and Return structured analysis"
    """
    response = llm.invoke(prompt)
    return {
        "analysis": response.content
    }