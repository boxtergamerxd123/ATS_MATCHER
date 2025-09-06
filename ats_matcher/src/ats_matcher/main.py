from __future__ import annotations
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from .schemas import ScoreRequest, ScoreResponse
from .scoring import compute_match
from .keywords import extract_terms, missing_terms
from .storage import init_db, save_analysis
from pathlib import Path

app = FastAPI(title="ATS Matcher")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
init_db()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/score", response_model=ScoreResponse)
def score(payload: ScoreRequest):
    score_val = compute_match(payload.resume, payload.job)
    resume_terms = extract_terms(payload.resume, top_k=20)
    job_terms = extract_terms(payload.job, top_k=20)
    miss = missing_terms(job_terms, resume_terms, k=20)
    save_analysis(score_val, payload.resume, payload.job)
    return ScoreResponse(
        score=score_val,
        top_resume_terms=resume_terms[:10],
        top_job_terms=job_terms[:10],
        missing_terms=miss
    )

@app.post("/score-form", response_class=HTMLResponse)
def score_form(resume: str = Form(...), job: str = Form(...)):
    payload = ScoreRequest(resume=resume, job=job)
    res = score(payload)
    return templates.TemplateResponse("index.html", {"request": {}, "result": res.model_dump()})
