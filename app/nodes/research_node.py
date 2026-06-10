from app.graph.state import ResearchState
from app.services.tavily_service import tavily_client

def research_node(state: ResearchState):
    questions = state['research_ques']
    all_results = []
    sources = []
    for question in questions:
        findings = []
        result = tavily_client.search(question)
        for item in result['results'][:2]:
            findings.append({
                "title": item['title'],
                "content": item['content'][:200],
                "url":item['url']
            })

            sources.append(item['url'])
        all_results.append({
            "question": question,
            "findings": findings
        })
    
    return {
        "research_data": all_results,
        "sources":list(set(sources))
    }