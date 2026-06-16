from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume_text, jd_text):

    documents = [
        resume_text,
        jd_text
    ]

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(
        documents
    )

    similarity = cosine_similarity(
        matrix
    )

    score = similarity[0][1] * 100

    return round(
        score,
        2
    )