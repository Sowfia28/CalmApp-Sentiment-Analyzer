# 🧘 Calm App Sentiment Analyzer

This project performs **AI-powered sentiment analysis and summarization** on user reviews of the Calm meditation app. It uses a combination of **Hugging Face's BERT** for sentiment classification and **Groq's LLAMA 3** for both professional and business-style summarization.

The app was developed as part of the *Applied AI for Managers* course project at the University at Buffalo.

---

## 🚀 Features

- **Sentiment Classification** (Positive / Negative) using BERT
- **Professional Summarization** using LLAMA 3 (8B model via Groq API)
- **Business Insight Summarization** (likes/dislikes as bullet points)
- **Streamlit Web App** for interactive review analysis
- **CSV Output Support** for structured analysis and dashboard use

---

## 🗂️ Project Structure

```plaintext
├── app.py                         # Streamlit web app
├── calm_reviews.csv               # Raw dataset of Calm app reviews
├── Analysis code.ipynb            # Jupyter notebook pipeline
├── Project report.pdf             # Final project report
├── requirements.txt               # Python dependencies
└── README.md                      # Project description
