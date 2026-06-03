from langgraph.graph import END, START, StateGraph
from app.graph.state import ResearchState
from app.nodes.research_node import research_node
from app.nodes.analysis_node import analysis_node
from app.nodes.planner_node import planner_node
from app.nodes.writer_node import writer_node

graph = StateGraph(ResearchState)
graph.add_node("planner", planner_node)
graph.add_node("research",research_node)
graph.add_node("analysis", analysis_node)
graph.add_node("writer", writer_node)
graph.add_edge(START, "planner")
graph.add_edge("planner", "research")
graph.add_edge("research", "analysis")
graph.add_edge("analysis", "writer")
graph.add_edge("writer", END)



app = graph.compile()