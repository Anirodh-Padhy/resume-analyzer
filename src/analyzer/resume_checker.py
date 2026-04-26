import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "resume_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")


# 🔹 RULE SCORE (0–100)
def rule_score(text):
    text = text.lower()

    sections = [
        "education", "experience", "skills", "projects",
        "work experience", "internship", "certifications",
        "achievements", "summary", "objective"
    ]

    section_matches = sum(1 for s in sections if s in text)
    has_email = "@" in text
    has_phone = any(char.isdigit() for char in text)
    word_count = len(text.split())

    score = 0

    # sections (important)
    score += min(section_matches * 15, 45)

    if has_email:
        score += 20

    if has_phone:
        score += 10

    if word_count > 150:
        score += 25

    return score  # out of ~100


# 🔹 ML PROBABILITY
def ml_score(text):
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)

        X = vectorizer.transform([text])
        prob = model.predict_proba(X)[0][1]

        return prob  # 0–1

    except:
        return 0


# 🔥 FINAL DECISION
def is_resume(text):
    r_score = rule_score(text)
    m_score = ml_score(text)

    # Normalize rule score to 0–1
    r_norm = r_score / 100

    # 🔥 weighted combination
    final_score = (0.6 * r_norm) + (0.4 * m_score)

    # DEBUG (optional)
    # print("Rule:", r_norm, "ML:", m_score, "Final:", final_score)

    return final_score > 0.7