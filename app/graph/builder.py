from langgraph.graph import END, START, StateGraph
from app.graph.state import ResearchState
from app.nodes.research_node import research_node


graph = StateGraph(ResearchState)
graph.add_node("research",research_node)

graph.add_edge(START, "research")
graph.add_edge("research", END)

app = graph.compile()