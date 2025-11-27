"""
Simple rule-based resume analyzer.
This keeps logic explainable for interviews.
"""
import re
from collections import Counter

KNOWN_SKILLS = [
    "python", "java", "c++", "c", "javascript", "node", "flask",
    "fastapi", "django", "react", "html", "css", "sql", "mongodb",
    "git", "docker", "aws", "ml", "tensorflow", "pytorch", "nlp"
]

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def find_skills(text: str):
    text_lower = text.lower()
    found = [s for s in KNOWN_SKILLS if s in text_lower]
    return sorted(found)

def top_words(text: str, n=10):
    stops = {"the","and","to","of","in","for","with","a","an","on","is","as","by","that"}
    words = re.findall(r"\b[a-zA-Z0-9\+\-]+\b", text.lower())
    filtered = [w for w in words if w not in stops and len(w) > 1]
    counts = Counter(filtered)
    return [w for w,_ in counts.most_common(n)]

def summarize(text: str, max_chars=200):
    text = clean_text(text)
    if len(text) <= max_chars:
        return text
    cut = text.find('.', 120)
    if cut != -1 and cut < max_chars:
        return text[:cut+1]
    return text[:max_chars].rsplit(' ', 1)[0] + "..."

def analyze_resume(text: str):
    text = clean_text(text)
    words = len(text.split())
    characters = len(text)
    skills = find_skills(text)
    common = top_words(text, n=8)

    score = 50
    score += min(len(skills) * 5, 25)
    score += 5 if words > 300 else 0
    score = min(score, 100)

    return {
        "word_count": words,
        "char_count": characters,
        "skills_found": skills,
        "top_terms": common,
        "readability_score": score,
        "summary": summarize(text, max_chars=220)
    }
