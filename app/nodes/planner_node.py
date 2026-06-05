from app.graph.state import ResearchState
from app.services.groq_service import planner_llm
import ast

def planner_node(state:ResearchState):
    topic = state['topic']
    prompt = f"""
Topic:
{topic}

Generate exactly 5 short web-search-friendly research questions.

Rules:
- Maximum 12 words per question
- Be specific
- Be factual
- Easy to search on the web
- No academic wording
- No long explanations

Return a Python list only.
"""
    response = planner_llm.invoke(prompt)
    content = response.content
    
    question = []
    if "</think>" in content:
        content = content.split("</think>")[-1].strip()
       

    question = ast.literal_eval(content)

    # for line in response.content.split("\n"):
    #     line = line.strip()
    #     if line.startswith('"') and line.endswith('",'):
    #         question.append(line.strip('",'))
    #     elif line.startswith('"') and line.endswith('"'):
    #         question.append(line.strip('"'))

    print("QUESTIONS:")
    print(question)
        


    return {
        "research_ques": question
    }