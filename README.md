# Sales Call Analyzer

An AI-powered sales call analysis tool built with LangGraph, FastAPI, and Groq (LLaMA 3.1).

## What It Does
Paste any sales call transcript and get back:
- Customer objections extracted
- Competitors mentioned
- Sales rep performance score (0-100)
- Personalized coaching suggestions

## Agent Pipeline
Transcript
    -> [Agent 1: Extractor]   - Extracts customer objections
    -> [Agent 2: Competitor]  - Identifies competitor mentions
    -> [Agent 3: Scorer]      - Scores rep performance (0-100)
    -> [Agent 4: Coach]       - Generates coaching suggestions
    -> JSON Report via FastAPI

## Tech Stack
- Python 3.10
- FastAPI - REST API layer
- LangGraph - Multi-agent orchestration
- LangChain + Groq - LLM calls (LLaMA 3.1)
- Pydantic - Data validation

## How to Run

1. Clone the repo:
   git clone https://github.com/SramanaPatra/sales-call-analyzer

2. Create virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create .env file and add your Groq API key:
   GROQ_API_KEY=your-key-here

5. Run the server:
   uvicorn app.main:app --reload

6. Open http://127.0.0.1:8000/docs and test!

## API Endpoints
- GET  /              - API status
- GET  /health        - Health check
- POST /analyze-call  - Analyze a sales call transcript

## Sample Input
{
  "transcript": "The price is too high compared to HubSpot...",
  "rep_name": "Sarah Johnson"
}

## Sample Output
{
  "rep_name": "Sarah Johnson",
  "objections": ["price is too high", "no time to learn new tool"],
  "competitors_mentioned": ["HubSpot", "Salesforce"],
  "performance_score": 75,
  "score_breakdown": {
    "active_listening": 15,
    "objection_handling": 12,
    "value_proposition": 18,
    "professional_tone": 20,
    "next_steps": 10
  },
  "coaching_suggestions": [
    "Address pricing with ROI data early in the call",
    "Offer a free trial to reduce adoption hesitation"
  ],
  "status": "success"
}

## Project Structure
sales-call-analyzer/
├── app/
│   ├── main.py        - FastAPI endpoints
│   ├── graph.py       - LangGraph pipeline
│   ├── nodes.py       - 4 AI agent functions
│   ├── prompts.py     - Prompt engineering
│   └── models.py      - Request/response schemas
├── .env               - API keys (never pushed)
├── requirements.txt
├── README.md
└── sample_transcript.txt