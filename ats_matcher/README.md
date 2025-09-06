# ATS Matcher — Resume vs Job Description
A small, portfolio‑ready Python project that analyzes how well a resume matches a job description. It computes a match score, highlights missing keywords, and suggests improvements. Built with FastAPI, SQLite, and scikit‑learn.

## Features
- Paste a job description or upload a `.txt` file
- Paste your resume text (export from PDF) or upload a `.txt` file
- Match score using TF‑IDF cosine similarity
- Extracts and counts keywords (unigrams & bigrams)
- Highlights missing role‑critical terms
- Stores analyses in SQLite for history
- Simple REST API + minimal HTML frontend (Jinja2)
- Unit tests, pre-commit config, type hints

## Tech stack
- Python 3.11+
- FastAPI + Uvicorn
- scikit-learn, numpy
- SQLite (via SQLModel)
- Jinja2 templates

## Quickstart
```bash
# 1) Create & activate a venv (Windows PowerShell shown; on macOS/Linux use python3 & source)
python -m venv .venv
. .venv/Scripts/Activate.ps1

# 2) Install
pip install -r requirements.txt

# 3) Run dev server
uvicorn ats_matcher.main:app --reload

# 4) Open
# http://127.0.0.1:8000
```

## Project structure
```
ats_matcher/
├─ src/ats_matcher/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ scoring.py
│  ├─ keywords.py
│  ├─ storage.py
│  ├─ schemas.py
│  └─ templates/
│     ├─ base.html
│     └─ index.html
├─ tests/
│  ├─ test_scoring.py
│  └─ test_keywords.py
├─ requirements.txt
├─ .gitignore
├─ pyproject.toml
├─ pre-commit-config.yaml
└─ README.md
```

## API (minimal)
- `POST /api/score` → JSON body `{ "resume": "...", "job": "..." }` → match score + keywords
- `GET /` → minimal form UI

## Notes
- For best results, paste **plain text** from your resume PDF and job post.
- This project avoids heavy models to install quickly in interviews.
- You can extend with: PDF parsing, OpenAI/GPT suggestions, or a React UI.
