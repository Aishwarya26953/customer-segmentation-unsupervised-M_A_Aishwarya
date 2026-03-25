from sklearn.mixture import GaussianMixture

def run_gmm(X, n_components=4):
    model = GaussianMixture(n_components=n_components, random_state=42)
    labels = model.fit_predict(X)
    return labels