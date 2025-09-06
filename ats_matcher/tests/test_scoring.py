from ats_matcher.scoring import compute_match

def test_compute_match_basic():
    resume = "Python developer with FastAPI and SQL experience. Machine learning projects."
    job = "Looking for a Python engineer with FastAPI and SQL. ML experience a plus."
    score = compute_match(resume, job)
    assert 0 <= score <= 100
    assert score > 10
