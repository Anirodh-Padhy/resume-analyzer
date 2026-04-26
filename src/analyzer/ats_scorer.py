def ats_score(resume_text, skills, job_desc):
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()

    job_words = set(job_desc.split())
    resume_words = set(resume_text.split())

    # 🔹 Skill match (max 40)
    required_skills = [skill for skill in skills if skill in job_desc]
    matched_skills = [skill for skill in required_skills if skill in resume_text]

    if len(required_skills) > 0:
        skill_score = (len(matched_skills) / len(required_skills)) * 40
    else:
        skill_score = 0

    # 🔹 Keyword similarity (max 30)
    common_words = job_words.intersection(resume_words)

    if len(job_words) > 0:
        keyword_score = (len(common_words) / len(job_words)) * 30
    else:
        keyword_score = 0

    # 🔹 Resume length score (max 20)
    word_count = len(resume_words)

    if 300 <= word_count <= 800:
        length_score = 20
    else:
        length_score = max(0, min(20, (word_count / 300) * 20))

    # 🔹 Penalty for missing skills
    missing_skills = [skill for skill in required_skills if skill not in resume_text]
    penalty = len(missing_skills) * 2  # subtract points

    total_score = skill_score + keyword_score + length_score - penalty

    # Clamp between 0–100
    total_score = max(0, min(100, total_score))

    return {
        "Skill Score": round(skill_score, 2),
        "Keyword Score": round(keyword_score, 2),
        "Length Score": round(length_score, 2),
        "Penalty": penalty,
        "Total Score": round(total_score, 2)
    }