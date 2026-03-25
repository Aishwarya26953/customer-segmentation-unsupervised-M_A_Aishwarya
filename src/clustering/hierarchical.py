from scipy.cluster.hierarchy import linkage

def run_hierarchical(X):
    linked = linkage(X, method="ward")
    return linked