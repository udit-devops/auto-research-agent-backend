from app.graph.state import ResearchState
from app.services.groq_service import llm

def analysis_node(state:ResearchState):
    research_summary = state['research_summary']
    prompt = f""" Research Summary:

{research_summary}

Extract the key findings and important insights.

Return a structured analysis.
    """
    response = llm.invoke(prompt)
    content = response.content
    if "</think>" in content:
        content = content.split("</think>")[-1].strip()
    return {
        "analysis": content
    }