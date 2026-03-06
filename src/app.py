import streamlit as st
import pandas as pd
from src.matcher import get_similarity_score

st.title("AI Resume Screening System")

job_description = st.text_area("Paste Job Description")

resume1 = st.text_area("Resume 1")
resume2 = st.text_area("Resume 2")
resume3 = st.text_area("Resume 3")

if st.button("Rank Candidates"):

    scores = []

    resumes = [resume1, resume2, resume3]

    for i, resume in enumerate(resumes):

        score = get_similarity_score(job_description, resume)

        scores.append({
            "Candidate": f"Resume {i+1}",
            "Match Score": round(score*100,2)
        })

    df = pd.DataFrame(scores)

    df = df.sort_values("Match Score", ascending=False)

    st.write(df)
