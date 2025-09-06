from ats_matcher.keywords import extract_terms, missing_terms

def test_terms_and_missing():
    resume = "python fastapi sql docker"
    job = "python fastapi sql aws kubernetes"
    r_terms = extract_terms(resume, top_k=10)
    j_terms = extract_terms(job, top_k=10)
    miss = missing_terms(j_terms, r_terms, k=10)
    assert "aws" in miss or "kubernetes" in miss
