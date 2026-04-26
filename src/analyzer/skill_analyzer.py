import spacy
from spacy.matcher import PhraseMatcher

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# 🔥 Synonyms mapping
SKILL_SYNONYMS = {
    "machine learning": ["ml"],
    "deep learning": ["dl"],
    "natural language processing": ["nlp"],
    "artificial intelligence": ["ai"],
    "javascript": ["js"],
    "structured query language": ["sql"]
}


def load_skills(path="data/skills.txt"):
    with open(path, "r") as f:
        return [line.strip().lower() for line in f.readlines()]


def extract_skills(text, skills_list):
    text = text.lower()
    doc = nlp(text)

    # 🔥 Phrase matcher (best for skills)
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(skill) for skill in skills_list]
    matcher.add("SKILLS", patterns)

    matches = matcher(doc)

    found_skills = set()

    # Extract matched skills
    for match_id, start, end in matches:
        span = doc[start:end]
        found_skills.add(span.text)

    # 🔥 Synonym support
    for skill, synonyms in SKILL_SYNONYMS.items():
        for syn in synonyms:
            if syn in text:
                found_skills.add(skill)

    return list(found_skills)