import pandas as pd

def create_rfm(df):
    purchase_df = df[df["event_type"] == "purchase"]

    snapshot_date = df["event_time"].max()

    rfm = purchase_df.groupby("user_id").agg({
        "event_time": lambda x: (snapshot_date - x.max()).days,
        "user_id": "count",
        "price": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    return rfm


def add_behavioral_features(df, rfm):
    views = df[df["event_type"] == "view"].groupby("user_id").size()
    carts = df[df["event_type"] == "cart"].groupby("user_id").size()

    rfm["Views"] = views
    rfm["Carts"] = carts

    rfm = rfm.fillna(0)

    rfm["Purchase_Ratio"] = rfm["Frequency"] / (rfm["Views"] + 1)
    rfm["Avg_Spend"] = rfm["Monetary"] / (rfm["Frequency"] + 1)

    return rfm