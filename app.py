import streamlit as st
import pandas as pd
from src.extractor import extract_text_from_pdf
from src.matcher import get_similarity_score

st.title("AI Resume Screening System")

st.write("Upload resumes and compare them with a job description.")

job_description = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Rank Candidates"):

    if not job_description:
        st.warning("Please enter a job description")

    elif not uploaded_files:
        st.warning("Please upload resumes")

    else:

        results = []

        for file in uploaded_files:

            resume_text = extract_text_from_pdf(file)

            score = get_similarity_score(job_description, resume_text)

            results.append({
                "Candidate": file.name,
                "Match Score": round(score * 100, 2)
            })

        df = pd.DataFrame(results)

        df = df.sort_values("Match Score", ascending=False)

        st.subheader("Candidate Ranking")
        st.dataframe(df)

        st.bar_chart(df.set_index("Candidate"))
