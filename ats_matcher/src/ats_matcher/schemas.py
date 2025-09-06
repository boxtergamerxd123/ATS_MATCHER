from pydantic import BaseModel, Field

class ScoreRequest(BaseModel):
    resume: str = Field(min_length=10, description="Plain text of your resume")
    job: str = Field(min_length=10, description="Plain text of the job description")

class ScoreResponse(BaseModel):
    score: float
    top_resume_terms: list[str]
    top_job_terms: list[str]
    missing_terms: list[str]
