import json
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from app.prompts import (
    EXTRACTOR_PROMPT,
    COMPETITOR_PROMPT,
    SCORER_PROMPT,
    COACH_PROMPT
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

def parse_json_response(response_text: str) -> dict:
    try:
        clean = response_text.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        return json.loads(clean.strip())
    except Exception:
        return {}

def extractor_node(state: dict) -> dict:
    print("🔍 Node 1: Extracting objections...")
    prompt = EXTRACTOR_PROMPT.format(transcript=state["transcript"])
    response = llm.invoke(prompt)
    parsed = parse_json_response(response.content)
    state["objections"] = parsed.get("objections", [])
    print(f"   Found {len(state['objections'])} objection(s)")
    return state

def competitor_node(state: dict) -> dict:
    print("🏢 Node 2: Identifying competitors...")
    prompt = COMPETITOR_PROMPT.format(transcript=state["transcript"])
    response = llm.invoke(prompt)
    parsed = parse_json_response(response.content)
    state["competitors_mentioned"] = parsed.get("competitors_mentioned", [])
    print(f"   Found {len(state['competitors_mentioned'])} competitor(s)")
    return state

def scorer_node(state: dict) -> dict:
    print("📊 Node 3: Scoring performance...")
    prompt = SCORER_PROMPT.format(
        transcript=state["transcript"],
        objections=json.dumps(state.get("objections", []))
    )
    response = llm.invoke(prompt)
    parsed = parse_json_response(response.content)
    state["performance_score"] = parsed.get("performance_score", 0)
    state["score_breakdown"] = parsed.get("score_breakdown", {})
    print(f"   Performance score: {state['performance_score']}/100")
    return state

def coach_node(state: dict) -> dict:
    print("🎯 Node 4: Generating coaching suggestions...")
    prompt = COACH_PROMPT.format(
        transcript=state["transcript"],
        objections=json.dumps(state.get("objections", [])),
        score=state.get("performance_score", 0)
    )
    response = llm.invoke(prompt)
    parsed = parse_json_response(response.content)
    state["coaching_suggestions"] = parsed.get("coaching_suggestions", [])
    print(f"   Generated {len(state['coaching_suggestions'])} suggestion(s)")
    return state