def get_missing_skills(
        resume_skills,
        jd_skills
):

    return list(
        set(jd_skills)
        -
        set(resume_skills)
    )


def generate_suggestions(
        score,
        missing_skills
):

    suggestions = []

    if score < 50:

        suggestions.append(
            "Resume needs significant improvements."
        )

    elif score < 80:

        suggestions.append(
            "Add more relevant keywords from the job description."
        )

    else:

        suggestions.append(
            "Excellent ATS score."
        )

    if missing_skills:

        suggestions.append(
            "Add these skills: "
            +
            ", ".join(missing_skills)
        )

    return suggestions