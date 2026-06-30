# ResumeScreeningProject
A Python and Streamlit-based Resume Screening System that compares PDF resumes with job descriptions and generates a match score.
# 📄 AI Resume Screening System

## 📌 Description

The AI Resume Screening System is a Python and Streamlit-based web application that helps evaluate resumes against a job description. It extracts text from PDF resumes, compares candidate skills with job requirements, and calculates a resume match score using TF-IDF and Cosine Similarity.

---

## 🚀 Features

- Upload PDF resumes
- Enter a job description
- Extract text from resumes
- Match candidate skills with job requirements
- Calculate resume match score
- Display matched skills
- Preview extracted resume text
- Simple and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- PyMuPDF (fitz)
- Scikit-learn
- Regular Expressions (re)

---

## 📁 Project Structure

```
ResumeScreeningProject/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ResumeScreeningProject.git
```

### Move to the project folder

```bash
cd ResumeScreeningProject
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## 📖 How to Use

1. Launch the application.
2. Upload a PDF resume.
3. Enter the job description.
4. View the generated match score.
5. Check the matched skills and resume preview.

---

## 🧠 How It Works

- Extracts text from the uploaded PDF resume.
- Cleans and processes the text.
- Compares resume content with the job description.
- Identifies matching skills.
- Calculates similarity using TF-IDF and Cosine Similarity.
- Displays the final resume match score.

---

## 📊 Output

The application displays:

- Resume Match Score (%)
- Match Result (Good, Average, or Low)
- Matched Skills
- Number of Skills Matched
- Resume Preview

---

## 🔮 Future Enhancements

- Support for DOCX resumes
- Automatic skill extraction using NLP
- Resume ranking for multiple candidates
- AI-based resume recommendations
- Database integration

---

## 👨‍💻 Author

**Durga Bhavani Boddu**

---

## ⭐ If you like this project, don't forget to star the repository!
