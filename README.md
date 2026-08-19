💬 TEXT SENTIMENT ANALYZER

A small web app that reads any piece of text — a review, a tweet, a comment — and tells you whether the tone is positive, negative, or neutral, with a confidence breakdown.

DEMO
<img width="1056" height="902" alt="Screenshot 2026-08-19 225130" src="https://github.com/user-attachments/assets/3fa1754a-3f6a-41be-875c-717fb62f102d" />
Live app: https://text-sentiment-analyzer-cniqpesjxiexkladqgjdl2.streamlit.app/

HOW IT WORKS
Text is scored using VADER (Valence Aware Dictionary and sEntiment Reasoner) — a rule-based sentiment analysis model tuned for short, informal text. It returns a compound score from -1 (very negative) to +1 (very positive), plus the proportion of positive, neutral, and negative language detected.

TECH STACK
Python
Streamlit — for the web interface
VADER (vaderSentiment) — for sentiment scoring
Run it locally
bash
git clone <your-repo-url>
cd text-sentiment-analyzer
pip install -r requirements.txt
streamlit run app.py

The app opens automatically at http://localhost:8501.

WHAT I;D ADD NEXT
File upload support to analyze a whole CSV of reviews/comments at once
A history of past inputs during a session
Swap in an LLM API call for more nuanced, context-aware sentiment
