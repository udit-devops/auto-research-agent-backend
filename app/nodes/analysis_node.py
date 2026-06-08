from app.graph.state import ResearchState
from app.services.groq_service import llm

def analysis_node(state:ResearchState):
    research_summary = state['research_summary']
    prompt = f""" Research Summary:

{research_summary}

Task:
Convert the research summary into a structured analysis.

Rules:
- Use ONLY information present in the research summary.
- Do NOT add new facts.
- Do NOT create statistics, percentages, market shares, or dates.
- Do NOT make assumptions.
- If information is missing, write "Not specified in research".
- Preserve factual accuracy.

Return a structured analysis with:
1. Key Findings
2. Important Insights
3. Risks
4. Opportunities
    """
    response = llm.invoke(prompt)
    content = response.content
    if "</think>" in content:
        content = content.split("</think>")[-1].strip()
    print("ANALYSIS:")
    print(content)
    return {
        "analysis": content
    }