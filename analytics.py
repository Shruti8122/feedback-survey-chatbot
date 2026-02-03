
def compute_metrics(df):
    metrics = {}

    if "nps" in df:
        metrics["Average NPS"] = df["nps"].dropna().mean()

    metrics["Positive %"] = (df.get("sentiment") == "Positive").mean() * 100
    metrics["Negative %"] = (df.get("sentiment") == "Negative").mean() * 100
    metrics["Total Responses"] = len(df)

    return metrics
