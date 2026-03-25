import pandas as pd

def load_data(path, nrows=None):
    df = pd.read_csv(path, nrows=nrows)
    return df

def clean_data(df):
    df = df.dropna(subset=["user_id", "price"])
    df = df[df["price"] > 0]
    df["event_time"] = pd.to_datetime(df["event_time"])
    df = df.drop_duplicates()
    return df