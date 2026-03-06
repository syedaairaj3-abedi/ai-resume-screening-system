# AI Resume Screening System

## Overview
Recruiters often review hundreds of resumes for a single job opening. This project demonstrates how Natural Language Processing (NLP) can support data-driven hiring decisions by automatically ranking resumes based on their similarity to a job description.

The system compares resume text against a job description using semantic similarity and produces a ranked list of candidates.

This project demonstrates practical applications of data analysis, text processing, and business analytics using Python.

---

## Features

• Resume and job description text comparison  
• NLP-based semantic similarity scoring  
• Candidate ranking based on match score  
• Interactive dashboard built with Streamlit  
• Data-driven candidate evaluation

---

## Tech Stack

Python  
Pandas  
Streamlit  
Sentence Transformers  
Scikit-learn  

---

## How It Works

1. A job description is entered into the system.
2. Multiple resumes are provided as input.
3. Text embeddings are generated using a pretrained NLP model.
4. Cosine similarity calculates how closely each resume matches the job description.
5. Candidates are ranked based on similarity scores.

---

## Example Output

Candidate Ranking Table

| Candidate | Match Score |
|-----------|-------------|
| Resume 2 | 91% |
| Resume 1 | 84% |
| Resume 3 | 67% |

---

## Future Improvements

• Resume PDF upload support  
• Skill extraction and keyword analysis  
• Visualization dashboard for recruiters  
• Integration with hiring platforms
