import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from score_analyzer import calculate_score
from utils import (
    get_missing_skills,
    generate_suggestions
)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title(
    "📄 AI Resume Analyzer & ATS Score Checker"
)

st.markdown(
    """
    Analyze your resume against a Job Description and get:

    - ATS Compatibility Score
    - Skill Match Analysis
    - Missing Skills Detection
    - Resume Improvement Suggestions
    """
)

st.sidebar.info(
    """
    Upload your resume and compare it with a Job Description.

    Features:
    ✅ ATS Score
    ✅ Skill Extraction
    ✅ Missing Skills
    ✅ Resume Suggestions
    """
)

st.title(
    "📄 AI Resume Analyzer & ATS Score Checker"
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if resume and jd:

    resume_text = extract_resume_text(
        resume
    )

    score = calculate_score(
        resume_text,
        jd
    )

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        jd
    )

    missing_skills = get_missing_skills(
        resume_skills,
        jd_skills
    )

    suggestions = generate_suggestions(
        score,
        missing_skills
    )

    # ATS Score Section
    st.subheader("ATS Match Score")

    st.metric(
        "Score",
        f"{score}%"
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {
                    "range": [0, 100]
                    },
                "steps": [
                    {
                        "range": [0, 50],
                        "color": "lightcoral"
                    },
                    {
                        "range": [50, 80],
                        "color": "khaki"
                    },
                    {
                        "range": [80, 100],
                        "color": "lightgreen"
                    }
                ]
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ATS Status
    if score >= 80:
        st.success("Excellent ATS Match")

    elif score >= 60:
        st.warning("Moderate ATS Match")

    else:
        st.error("Low ATS Match")

    # Skills Found
    st.subheader("Skills Found")

    if resume_skills:

        df = pd.DataFrame({
            "Skill": resume_skills,
            "Count": [1] * len(resume_skills)
        })

        fig_bar = px.bar(
            df,
            x="Skill",
            y="Count",
            title="Detected Skills"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

    st.write(
        resume_skills
    )

    # Missing Skills
    st.subheader("Missing Skills")

    st.write(
        missing_skills
    )

    # Analysis Summary
    st.subheader("Analysis Summary")

    st.write(
        f"""
        Resume Skills Found: {len(resume_skills)}

        Job Description Skills: {len(jd_skills)}

        Missing Skills: {len(missing_skills)}
        """
    )

    report = f"""
    ATS Score: {score}%

    Skills Found:
    {', '.join(resume_skills)}

    Missing Skills:
    {', '.join(missing_skills)}

    Suggestions:
    {chr(10).join(suggestions)}
    """

    st.download_button(
        label="📥 Download Analysis Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )

    # Suggestions
    st.subheader("Suggestions")

    for suggestion in suggestions:

        st.write(
            "✅",
            suggestion
        )