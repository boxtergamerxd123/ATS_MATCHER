from __future__ import annotations
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional
from datetime import datetime

class Analysis(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    score: float
    resume_chars: int
    job_chars: int

engine = create_engine("sqlite:///ats_history.sqlite3")

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def save_analysis(score: float, resume_text: str, job_text: str) -> int:
    with Session(engine) as sess:
        a = Analysis(score=score, resume_chars=len(resume_text), job_chars=len(job_text))
        sess.add(a)
        sess.commit()
        sess.refresh(a)
        return a.id or 0
