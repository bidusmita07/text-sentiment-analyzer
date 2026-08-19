

import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(page_title="Text Sentiment Analyzer", page_icon="💬", layout="centered")

analyzer = SentimentIntensityAnalyzer()

st.title("💬 Text Sentiment Analyzer")
st.write("Paste any text — a review, a tweet, a comment — and see its emotional tone, instantly.")

text = st.text_area("Enter text to analyze", height=150, placeholder="Type or paste something here...")

if st.button("Analyze Sentiment", type="primary"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        scores = analyzer.polarity_scores(text)
        compound = scores["compound"]

        if compound >= 0.05:
            sentiment, emoji, color = "Positive", "😊", "green"
        elif compound <= -0.05:
            sentiment, emoji, color = "Negative", "😞", "red"
        else:
            sentiment, emoji, color = "Neutral", "😐", "gray"

        st.markdown(f"### {emoji} Overall Sentiment: :{color}[{sentiment}]")
        st.progress((compound + 1) / 2)  # normalize -1..1 range to 0..1 for the bar
        st.caption(f"Compound score: {compound:.3f}  (ranges from -1 to +1)")

        col1, col2, col3 = st.columns(3)
        col1.metric("Positive", f"{scores['pos']*100:.1f}%")
        col2.metric("Neutral", f"{scores['neu']*100:.1f}%")
        col3.metric("Negative", f"{scores['neg']*100:.1f}%")

st.divider()
st.caption("Built with Streamlit + VADER Sentiment Analysis · Bindu · KIIT")
