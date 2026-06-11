from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from app.nodes import (
    extractor_node,
    competitor_node,
    scorer_node,
    coach_node
)

# Define the shared state structure
class AnalysisState(TypedDict):
    transcript: str
    objections: List[str]
    competitors_mentioned: List[str]
    performance_score: int
    score_breakdown: dict
    coaching_suggestions: List[str]

def build_graph():
    # Create the graph
    graph = StateGraph(AnalysisState)
    
    # Add all 4 nodes
    graph.add_node("extractor", extractor_node)
    graph.add_node("competitor", competitor_node)
    graph.add_node("scorer", scorer_node)
    graph.add_node("coach", coach_node)
    
    # Connect nodes in sequence
    graph.set_entry_point("extractor")
    graph.add_edge("extractor", "competitor")
    graph.add_edge("competitor", "scorer")
    graph.add_edge("scorer", "coach")
    graph.add_edge("coach", END)
    
    return graph.compile()

# Single instance reused everywhere
analysis_graph = build_graph()