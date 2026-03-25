from sklearn.preprocessing import StandardScaler

def scale_data(df):
    scaler = StandardScaler()
    X = scaler.fit_transform(df)
    return X