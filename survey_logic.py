def get_survey_questions():
    return [
        {"id": "nps", "question": "On a scale of 0–10, how likely are you to recommend us?", "type": "NPS"},
        {"id": "csat", "question": "How satisfied are you with your experience? (1–5)", "type": "CSAT"},
        {"id": "ces", "question": "How easy was it to resolve your issue? (1–5)", "type": "CES"},
        {"id": "open", "question": "Tell us more about your experience.", "type": "open"},
        {"id": "chatbot_helpful", "question": "Was this chatbot helpful in resolving your query?","type":"open"},
        {"id": "followup", "question": "Would you like us to follow up? (Yes/No)", "type": "open"},
        {"id": "contact", "question": "If yes, please share your email ID.","type":"open"},

    ]


def get_follow_up(nps_score):
    if nps_score <= 6:
        return "Sorry about that 😟 ."
    elif nps_score >= 9:
        return "Awesome! 🎉 ."
    return None
