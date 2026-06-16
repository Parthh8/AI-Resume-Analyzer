SKILLS = [
    "python",
    "java",
    "sql",
    "power bi",
    "excel",
    "aws",
    "machine learning",
    "streamlit",
    "pandas",
    "numpy",
    "tensorflow",
    "scikit-learn",
    "data analysis",
    "tableau",
    "mongodb",
    "mysql",
    "html",
    "css",
    "javascript"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills