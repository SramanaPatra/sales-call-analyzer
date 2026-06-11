EXTRACTOR_PROMPT = """
You are an expert sales analyst.
Given the following sales call transcript, extract ALL objections 
raised by the customer or prospect.

An objection is any concern, hesitation, pushback, or reason 
given for not moving forward.

Return ONLY a JSON object in this exact format, nothing else:
{{
  "objections": ["objection 1", "objection 2", "objection 3"]
}}

If no objections found, return: {{"objections": []}}

Transcript:
{transcript}
"""

COMPETITOR_PROMPT = """
You are an expert competitive intelligence analyst.
Given the following sales call transcript, identify ALL competitors 
or alternative solutions mentioned by anyone on the call.

Return ONLY a JSON object in this exact format, nothing else:
{{
  "competitors_mentioned": ["Competitor A", "Competitor B"]
}}

If no competitors mentioned, return: {{"competitors_mentioned": []}}

Transcript:
{transcript}
"""

SCORER_PROMPT = """
You are an expert sales performance coach.
Given the following sales call transcript and the objections raised,
score the sales representative's performance from 0 to 100.

Scoring criteria:
- Listened actively (0-20 points)
- Addressed objections clearly (0-20 points)  
- Communicated value proposition (0-20 points)
- Maintained professional tone (0-20 points)
- Moved deal forward / clear next steps (0-20 points)

Return ONLY a JSON object in this exact format, nothing else:
{{
  "performance_score": 75,
  "score_breakdown": {{
    "active_listening": 15,
    "objection_handling": 12,
    "value_proposition": 18,
    "professional_tone": 20,
    "next_steps": 10
  }}
}}

Transcript:
{transcript}

Objections raised:
{objections}
"""

COACH_PROMPT = """
You are a world-class sales coach.
Given the sales call transcript, objections raised, and performance score,
generate 3 to 5 specific, actionable coaching suggestions for the sales rep.

Each suggestion must:
- Be specific to what happened in THIS call (not generic advice)
- Be actionable (something they can do differently next time)
- Be encouraging in tone

Return ONLY a JSON object in this exact format, nothing else:
{{
  "coaching_suggestions": [
    "Specific suggestion 1",
    "Specific suggestion 2",
    "Specific suggestion 3"
  ]
}}

Transcript:
{transcript}

Objections raised:
{objections}

Performance score:
{score}
"""