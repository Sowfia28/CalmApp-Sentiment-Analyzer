# 🧘 Calm App Sentiment Analyzer

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?style=flat-square&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-Educational-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Project-Academic%20Capstone-success?style=flat-square)

> A Streamlit-powered NLP dashboard to analyze, summarize, and visualize user sentiment on Calm app reviews using BERT and Groq’s LLAMA 3 models.

---

## 🚀 Live Demo

👉 [**Try the App Here**](https://calmapp-sentiment-analyzer.streamlit.app/)  
📎 Hosted on Streamlit Cloud

---

## 📌 Project Summary

This project was developed as part of the *Applied AI for Managers* course at the University at Buffalo. It uses state-of-the-art NLP models to classify and summarize user reviews from the Calm meditation app, enabling actionable business insights.

**Key Features:**
- Sentiment classification (Positive/Negative) using BERT
- Professional summarization using LLAMA 3 (Groq API)
- Business-style summaries with Likes & Dislikes in 10 words or less
- Interactive Streamlit app with clean UI
- Download-ready output CSV for business analysis

---

## App
![image](https://github.com/user-attachments/assets/f86a8a82-b2e3-47b8-a5fd-4a3d80ee8045)

---

### ▶️ Run Locally

```bash
git clone https://github.com/Sowfia28/CalmApp-Sentiment-Analyzer.git
cd CalmApp-Sentiment-Analyzer
pip install -r requirements.txt
streamlit run app.py

---

## 🗂️ Project Structure

```plaintext
├── app.py                         # Streamlit web app
├── calm_reviews.csv               # Raw dataset of Calm app reviews
├── Analysis code.ipynb            # Jupyter notebook pipeline
├── Project report.pdf             # Final project report
├── requirements.txt               # Python dependencies
└── README.md                      # Project description
