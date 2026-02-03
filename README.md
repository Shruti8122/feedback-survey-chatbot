# 💬 AI-Powered Feedback Survey Chatbot

An interactive **Streamlit-based feedback survey chatbot** that collects structured and unstructured user feedback, performs **sentiment analysis**, computes **business metrics (NPS, CSAT)**, and generates **actionable recommendations** — all in real time.

This project is designed to simulate a **real-world feedback system** used by SaaS platforms and customer support teams.

---

## 🚀 Features

- 🧠 **Chatbot-style survey interface**
- 📊 **Metrics computation**
  - Net Promoter Score (NPS)
  - Positive / Negative sentiment percentage
- 😊 **Sentiment analysis** using NLP (TextBlob)
- 🆔 **Unique respondent ID** for each user session
- 🕒 **Timestamped responses**
- 📁 **Persistent CSV storage**
- 🧩 Modular, clean, production-style architecture
- 📈 Auto-generated **recommendations** based on feedback trends

---

## 🏗️ Project Structure

feedback-chat-bot/
│
├── app.py # Main Streamlit app
├── survey_logic.py # Survey questions & follow-up logic
├── sentiment.py # Sentiment analysis logic
├── scaledown.py # Survey optimization logic
├── analytics.py # Metrics computation
├── recommendations.py # Business recommendations
├── data/
│ └── responses.csv # Stored survey responses
├── requirements.txt # Dependencies
└── README.md # Project documentation
---

## 🧪 How It Works

1. User answers survey questions via chat UI
2. Each session gets a **unique respondent ID**
3. Responses are:
   - Stored in CSV
   - Analyzed for sentiment
   - Converted into metrics
4. System generates **recommendations** based on trends

---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/feedback-chatbot.git
cd feedback-chat-bot
```
### 2️⃣ Create Virtual Environment (Optional)
```bash
python -m venv venv
```
Activate it:
Windows
```bash
venv\Scripts\activate
```

Mac/Linux
```bash
source venv/bin/activate
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
▶️ Run the Application
```bash
streamlit run app.py
```

Then open:

http://localhost:8501

📦 requirements.txt
streamlit
pandas
textblob
scikit-learn

📊 Example Metrics Output
{
  "Average NPS": 8.2,
  "Positive %": 65.0,
  "Negative %": 12.0
}

🧠 Recommendation Logic

High negative sentiment → Improve customer support

Low NPS → Focus on service quality

Healthy feedback → Maintain current strategy

🌟 Unique / Creative Enhancements

Session-based respondent tracking

Chat-style UX instead of forms

Modular design (easy to extend)

Ready for deployment (Streamlit Cloud / Render)

🔮 Future Enhancements

Authentication & user login

Dashboard with charts

Database integration (PostgreSQL)

Email follow-ups

AI-powered summarization (LLMs)

📌 Use Cases

Customer feedback systems

Product surveys

SaaS NPS tracking

Academic / portfolio projects
