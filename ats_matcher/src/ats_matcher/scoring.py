from __future__ import annotations
from typing import Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match(resume_text: str, job_text: str) -> float:
    """TF-IDF cosine similarity between resume and job text (0..100)."""
    vect = TfidfVectorizer(ngram_range=(1,2), min_df=1, max_features=4000)
    X = vect.fit_transform([resume_text, job_text])
    sim = cosine_similarity(X[0:1], X[1:2])[0,0]
    return round(float(sim * 100.0), 2)
