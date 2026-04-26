# 📄 AI Resume Analyzer

### 🚀 Intelligent Resume Screening & ATS Scoring System

---

## 🧠 Overview

AI Resume Analyzer is a real-time web application that evaluates resumes using Natural Language Processing (NLP) and Machine Learning. It analyzes resume content, compares it with job descriptions, and provides actionable insights such as ATS score, missing skills, and improvement suggestions.

The system also includes a hybrid resume validation module that ensures only valid resumes are processed using a combination of Machine Learning classification and rule-based heuristics.

---

## ✨ Features

- 📄 Upload and parse resume (PDF)
- 🧠 Automatic skill extraction using NLP
- 🎯 Job description matching
- 📊 ATS-style scoring system
- ⚠️ Missing skill detection
- 💡 Personalized improvement suggestions
- 🤖 Resume validation using ML + rule-based system
- 📥 Downloadable PDF report
- 🎨 Interactive UI built with Streamlit

---

## 🧠 Core Components

### 🔍 Resume Parsing
- Extracts text from PDF resumes
- Cleans and processes content for analysis

### 🧩 Skill Extraction
- Keyword + NLP-based skill detection
- Supports customizable skill list

### 📊 ATS Scoring Engine
- Weighted scoring based on:
  - Skill match
  - Keyword relevance
  - Resume length
  - Missing skill penalty

### 🤖 Resume Validation (Advanced)
- ML Classifier (TF-IDF + Logistic Regression)
- Rule-based scoring system
- Combined using a hybrid approach

### 📄 Report Generation
- Generates a structured PDF report
- Includes score, skills, missing items, and suggestions

---

## 🧰 Tech Stack

- Frontend/UI: Streamlit  
- Backend: Python  
- Machine Learning: Scikit-learn  
- NLP: TF-IDF Vectorization  
- PDF Processing: PyPDF / FPDF  
- Data Handling: NumPy, Pandas  

---

## 📁 Project Structure

resume-analyzer/
│
├── app/
│ └── streamlit_app.py
│
├── data/
│ └── skills.txt
│
├── models/
│ ├── resume_model.pkl
│ └── vectorizer.pkl
│
├── scripts/
│ └── train_resume_classifier.py
│
├── src/
│ ├── analyzer/
│ │ ├── ats_scorer.py
│ │ ├── resume_checker.py
│ │ ├── skill_analyzer.py
│ │ └── suggestions.py
│ │
│ ├── matcher/
│ │ └── job_matcher.py
│ │
│ └── parser/
│ └── resume_parser.py
│
├── requirements.txt
└── README.md

---

## 📊 How It Works

1. Upload a resume (PDF)
2. System validates whether it is a resume
3. Extracts text and identifies skills
4. Compares with job description
5. Computes ATS score
6. Displays:
   - Score breakdown
   - Missing skills
   - Suggestions
7. Generates downloadable report

---

## 🎯 Key Highlights

- Hybrid AI system (ML + rule-based)
- Real-time processing with optimized pipeline
- Intelligent filtering to avoid invalid inputs
- Explainable scoring mechanism
- Professional report generation

---

## 🚀 Future Improvements

- Use transformer-based models (BERT) for better NLP
- Improve ML classifier with larger dataset
- Deploy on cloud (AWS / Streamlit Cloud)
- Mobile-friendly UI
- Semantic skill matching using embeddings

---

## 💡 Key Learnings

- Designing real-world ML pipelines
- Combining rule-based and ML approaches
- Handling noisy real-world data (PDF resumes)
- Building interactive AI applications
- Model evaluation and tuning

---

## 👨‍💻 Author

**Anirodh Padhy**

- 💼 Aspiring AI/ML Engineer  
- 💻 GitHub: (www.linkedin.com/in/anirodh-padhy-ab3455315)  
- 🔗 LinkedIn: (https://github.com/Anirodh-Padhy/moodtune-ai)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork!