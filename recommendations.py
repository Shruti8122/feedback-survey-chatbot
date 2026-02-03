
def generate_recommendations(metrics):
    if metrics.get("Negative %", 0) > 30:
        return "🚨 High negative sentiment detected. Improve customer support and reduce friction."

    if metrics.get("Average NPS", 10) < 7:
        return "⚠️ NPS is low. Focus on product quality and customer experience."

    return "✅ Customer feedback is positive. Maintain current strategy."
