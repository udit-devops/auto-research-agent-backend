from app.graph.state import ResearchState
from app.services.groq_service import llm

def writer_node(state:ResearchState):
    analysis = state['analysis']
    prompt = f"""
Create a professional research report.

Sections:
1. Executive Summary
2. Key Findings
3. Market Analysis
4. Risks & Challenges
5. Future Outlook
6. Conclusion

Analysis:

{analysis}
"""
    response = llm.invoke(prompt)
    
    return{
        "report":response.content
    }