from app.graph.state import ResearchState
from app.services.groq_service import planner_llm


def planner_node(state:ResearchState):
    topic = state['topic']
    prompt = f"""
Generate exactly 5 research questions for:

{topic}

Return a Python list only.

Example:
[
"question 1",
"question 2",
"question 3",
"question 4",
"question 5"
]
"""
    response = planner_llm.invoke(prompt)
    question = []
    for line in response.content.split("\n"):
        line = line.strip()
        if line.startswith('"') and line.endswith('",'):
            question.append(line.strip('",'))
        elif line.startswith('"') and line.endswith('"'):
            question.append(line.strip('"'))

    print("QUESTIONS:")
    print(question)
        


    return {
        "research_ques": question
    }