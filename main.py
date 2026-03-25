import pandas as pd

from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_rfm, add_behavioral_features
from src.utils import scale_data
from src.clustering.kmeans import run_kmeans
from src.evaluation import evaluate_clustering


# LOAD DATA
data_path = "data/raw/2019-Nov.csv/2019-NOV.csv"

df = load_data(data_path, nrows=500000)

# CLEAN DATA

df = clean_data(df)


# FEATURE ENGINEERING

rfm = create_rfm(df)
rfm = add_behavioral_features(df, rfm)


# SCALING

X = scale_data(rfm)


# CLUSTERING

labels = run_kmeans(X, k=4)

# EVALUATION

sil_score, db_score = evaluate_clustering(X, labels)

print("Number of Clusters:", len(set(labels)))
print("Silhouette Score:", sil_score)
print("Davies-Bouldin Index:", db_score)