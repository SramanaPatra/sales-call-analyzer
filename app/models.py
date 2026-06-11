from pydantic import BaseModel
from typing import List, Optional

class TranscriptRequest(BaseModel):
    transcript: str
    rep_name: Optional[str] = "Sales Rep"

class ScoreBreakdown(BaseModel):
    active_listening: int
    objection_handling: int
    value_proposition: int
    professional_tone: int
    next_steps: int

class AnalysisResponse(BaseModel):
    rep_name: str
    objections: List[str]
    competitors_mentioned: List[str]
    performance_score: int
    score_breakdown: dict
    coaching_suggestions: List[str]
    status: str = "success"