def generate_suggestions(missing_skills, score):
    suggestions = []

    if score < 60:
        suggestions.append("Improve resume with more relevant skills.")

    if missing_skills:
        suggestions.append("Add missing skills: " + ", ".join(missing_skills))

    suggestions.append("Use action verbs (developed, built, implemented).")
    suggestions.append("Keep resume concise (1 page ideal).")

    return suggestions