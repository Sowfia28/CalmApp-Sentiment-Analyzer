# ========================
# Calm App Sentiment & Summarization Analyzer
# Updated Full Version
# ========================

import streamlit as st
import pandas as pd
import groq
from transformers import pipeline

# -----------------------
# Streamlit Page Settings
# -----------------------
st.set_page_config(
    page_title="Calm App Review Analyzer",
    page_icon="🧘‍♂️",
    layout="wide"
)

# Sidebar
st.sidebar.title("About this App")
st.sidebar.markdown(
    """
    - Analyze Calm app reviews
    - Summarize professionally (paragraph)
    - Summarize for business (2 bullet points)
    - Hugging Face for Sentiment
    - Groq Llama3 for Summarization
    """
)
st.sidebar.markdown("Built by KSJ")

# -----------------------
# Main Heading
# -----------------------
st.title("Calm App Sentiment and Professional Summarization Analyzer")
st.write(
    "Analyze user reviews from the Calm app to extract **sentiment** and generate both a **professional summary** and **business-focused bullet points** using cutting-edge AI models."
)

# -----------------------
# Text Input
# -----------------------
user_input = st.text_area(
    "Paste your Calm App Review:",
    height=200,
    placeholder="Paste the Calm App user review here..."
)

# -----------------------
# API Setup (Groq)
# -----------------------
groq_client = groq.Groq(api_key="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")  # <-- Replace with your real Groq API key

# -----------------------
# Analyze Button
# -----------------------
if st.button("Analyze Review"):

    if user_input.strip() == "":
        st.warning("Please paste a review before clicking Analyze.")
    else:
        # -----------------------
        # Sentiment Analysis
        # -----------------------
        sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        prediction = sentiment_pipeline(user_input)
        predicted_sentiment = prediction[0]['label']
        confidence_score = prediction[0]['score']

        # Display Sentiment
        st.subheader("Sentiment Analysis Result")
        if predicted_sentiment == "POSITIVE":
            st.success(f"**Detected Sentiment:** {predicted_sentiment} (Confidence: {confidence_score:.2%})")
        else:
            st.error(f"**Detected Sentiment:** {predicted_sentiment} (Confidence: {confidence_score:.2%})")

        # -----------------------
        # Summarizations
        # -----------------------

        # 1. Professional Full Summarization
        full_summary_prompt = f"""Summarize the following Calm App user review in a professional, concise paragraph.

Review:
{user_input}

Summary:"""

        full_summary = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": full_summary_prompt}
            ]
        )

        # 2. Business Bullet Points Summarization
        bullet_summary_prompt = f"""You are a business analyst.
Summarize the following Calm App user review into two very short bullet points:
- One for what the user liked (under 10 words)
- One for what the user disliked (under 10 words)

User Review:
{user_input}

Return only the two bullet points, no extra text."""

        bullet_summary = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": bullet_summary_prompt}
            ]
        )

        # Extract Responses
        full_summary_text = full_summary.choices[0].message.content
        bullet_summary_text = bullet_summary.choices[0].message.content

        # -----------------------
        # Display Summarizations
        # -----------------------

        st.subheader("Professional Summarization")
        st.success(full_summary_text)

        st.subheader("Business Insights (Likes and Dislikes)")
        st.info(bullet_summary_text)
