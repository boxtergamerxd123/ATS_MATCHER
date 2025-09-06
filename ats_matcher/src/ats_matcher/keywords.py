from __future__ import annotations
import re
from collections import Counter
from typing import Iterable

STOPWORDS = set(
    """
    a an and are as at be by for from has he in is it its of on that the to was were will with
    de la los las y en para con por un una al del
    """.split()
)

TOKEN_RE = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9+#.-]{2,}")

def tokenize(text: str) -> list[str]:
    tokens = [t.lower() for t in TOKEN_RE.findall(text)]
    return [t for t in tokens if t not in STOPWORDS]

def extract_terms(text: str, top_k: int = 20) -> list[str]:
    tokens = tokenize(text)
    # unigrams
    unigrams = tokens
    # bigrams
    bigrams = [" ".join(pair) for pair in zip(tokens, tokens[1:])]
    counts = Counter(unigrams + bigrams)
    return [t for t, _ in counts.most_common(top_k)]

def missing_terms(job_terms: Iterable[str], resume_terms: Iterable[str], k: int = 20) -> list[str]:
    resume_set = set(resume_terms)
    miss = [t for t in job_terms if t not in resume_set]
    return miss[:k]
