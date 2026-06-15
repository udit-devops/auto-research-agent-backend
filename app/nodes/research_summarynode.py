from app.graph.state import ResearchState
from app.services.groq_service import llm

def research_summary_node(state:ResearchState):
    research_data = state['research_data']
    prompt = f"""
     Summarize the research findings.

For each question:
- Keep only the most important findings
- Use concise bullet points
- Remove repetition

Research Data:

{research_data}

    """
    print("RAW Size:", len(str(research_data)))
    response = llm.invoke(prompt)
    content = response.content
    if "</think>" in content:
        content = content.split("</think>")[-1].strip()
    return {
            "research_summary": content
    }


