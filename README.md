# AI Resume Analyzer & ATS Score Checker

## Overview

AI Resume Analyzer is a Streamlit-based web application that evaluates resumes against job descriptions and provides an ATS (Applicant Tracking System) compatibility score.

## Features

* PDF Resume Upload
* ATS Match Score Calculation
* Skill Extraction
* Missing Skills Detection
* Resume Improvement Suggestions
* Skill Visualization Charts
* Downloadable Analysis Report

## Technologies Used

* Python
* Streamlit
* Scikit-Learn
* PDFPlumber
* Pandas
* Plotly

## How It Works

1. Upload a resume in PDF format.
2. Paste a job description.
3. The application extracts skills and keywords.
4. TF-IDF and Cosine Similarity calculate the ATS score.
5. Missing skills and recommendations are displayed.

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Parth
