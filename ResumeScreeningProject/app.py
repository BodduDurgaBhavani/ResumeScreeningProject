import streamlit as st
import fitz
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Enter Job Description"
)

if uploaded_file is not None and job_description:

    # Read PDF
    pdf_bytes = uploaded_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    resume_text = ""

    for page in doc:
        resume_text += page.get_text()

    # Convert to lowercase
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Clean text
    resume_text = re.sub(r'[^a-z0-9\s]', ' ', resume_text)
    job_description = re.sub(r'[^a-z0-9\s]', ' ', job_description)

    # Skills list
    skills = [
        "python",
        "java",
        "c",
        "machine learning",
        "artificial intelligence",
        "data structures",
        "html",
        "css",
        "oracle",
        "blockchain",
        "natural language processing",
        "generative ai",
        "communication",
        "teamwork",
        "adaptability",
        "time management"
    ]

    matched_skills = []

    for skill in skills:
        if skill in resume_text and skill in job_description:
            matched_skills.append(skill)

    # Skill score
    skill_score = (len(matched_skills) / len(skills)) * 100

    # TF-IDF score
    docs = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(docs)

    similarity_score = cosine_similarity(matrix)[0][1] * 100

    # Final score
    final_score = round((skill_score * 0.7) + (similarity_score * 0.3), 2)

    st.subheader("Match Result")
    st.write(f"Match Score: {final_score}%")

    if final_score >= 70:
        st.success("Good Match")
    elif final_score >= 40:
        st.warning("Average Match")
    else:
        st.error("Low Match")

    st.subheader("Matched Skills")

    if matched_skills:
        st.write(", ".join(matched_skills))
    else:
        st.write("No matching skills found")

    st.write(f"Skills Matched: {len(matched_skills)} / {len(skills)}")

    with st.expander("Resume Preview"):
        st.write(resume_text[:5000])