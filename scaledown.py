def apply_scaledown(questions, responses):
    sentiments = [r.get("sentiment") for r in responses]

    if sentiments.count("Positive") >= 2:
        return questions[:3]
    if sentiments.count("Negative") >= 2:
        return questions[:4]

    return questions
