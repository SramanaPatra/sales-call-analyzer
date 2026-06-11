from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import TranscriptRequest, AnalysisResponse
from app.graph import analysis_graph

app = FastAPI(
    title="Sales Call Analyzer",
    description="AI-powered sales call analysis using LangGraph agents",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {
        "message": "Sales Call Analyzer API is running 🚀",
        "docs": "/docs",
        "analyze_endpoint": "/analyze-call"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analyze-call", response_model=AnalysisResponse)
def analyze_call(request: TranscriptRequest):
    if not request.transcript or len(request.transcript.strip()) < 20:
        raise HTTPException(
            status_code=400,
            detail="Transcript too short. Please provide a meaningful sales call transcript."
        )
    
    try:
        initial_state = {
            "transcript": request.transcript,
            "objections": [],
            "competitors_mentioned": [],
            "performance_score": 0,
            "score_breakdown": {},
            "coaching_suggestions": []
        }
        
        result = analysis_graph.invoke(initial_state)
        
        return AnalysisResponse(
            rep_name=request.rep_name,
            objections=result.get("objections", []),
            competitors_mentioned=result.get("competitors_mentioned", []),
            performance_score=result.get("performance_score", 0),
            score_breakdown=result.get("score_breakdown", {}),
            coaching_suggestions=result.get("coaching_suggestions", [])
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )