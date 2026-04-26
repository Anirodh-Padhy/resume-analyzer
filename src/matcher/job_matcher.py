from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.analyzer.skill_analyzer import SKILL_SYNONYMS
def match_score(resume_text, job_desc):
    documents = [resume_text, job_desc]

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return round(float(similarity[0][0] * 100), 2)
def missing_skills(resume_skills, job_desc, skills_list):
    job_desc = job_desc.lower()

    required = []
    for skill in skills_list:
        if skill in job_desc:
            required.append(skill)

    # 🔥 include synonyms
    for skill, synonyms in SKILL_SYNONYMS.items():
        for syn in synonyms:
            if syn in job_desc:
                required.append(skill)

    required = list(set(required))

    missing = [skill for skill in required if skill not in resume_skills]

    return missing