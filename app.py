import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime

from survey_logic import get_survey_questions, get_follow_up
from sentiment import analyze_sentiment
from scaledown import apply_scaledown
from analytics import compute_metrics
from recommendations import generate_recommendations

st.set_page_config(page_title="Feedback Survey Chatbot")
st.title("💬 Feedback Collection Chatbot")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = []

if "respondent_id" not in st.session_state:
    st.session_state.respondent_id = str(uuid.uuid4())

base_questions = get_survey_questions()
questions = apply_scaledown(base_questions, st.session_state.responses)

user_input = st.chat_input("Type your response here")


if user_input:
    current_question = questions[st.session_state.step]

    response = {
        "respondent_id": st.session_state.respondent_id,
        "question": current_question["id"],
        "answer": user_input,
        "timestamp": datetime.utcnow().isoformat()
    }

    if current_question["type"] == "open":
        sentiment, polarity = analyze_sentiment(user_input)
        response["sentiment"] = sentiment
        response["polarity"] = polarity

    if current_question["type"] in ["NPS", "CSAT", "CES"]:
        response[current_question["type"].lower()] = int(user_input)

    st.session_state.responses.append(response)

    if current_question["id"] == "nps":
        follow_up = get_follow_up(int(user_input))
        if follow_up:
            st.chat_message("assistant").write(follow_up)

    st.session_state.step += 1

if st.session_state.step < len(questions):
    st.chat_message("assistant").write(
        questions[st.session_state.step]["question"]
    )
else:
    st.success("Thank you for your feedback! 🎉")

    df_new = pd.DataFrame(st.session_state.responses)
    os.makedirs("data", exist_ok=True)

    file_path = "data/responses.csv"

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        old_df = pd.read_csv(file_path)
        df = pd.concat([old_df, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(file_path, index=False)

    st.subheader("📊 Analytics")
    metrics = compute_metrics(df)
    st.json(metrics)

    st.subheader("🧠 Recommendations")
    st.write(generate_recommendations(metrics))
