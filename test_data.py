from sklearn.datasets.samples_generator import make_blobs
import pandas as pd
import numpy as np
def two_d_data():
    X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)
    return X
def five_d_data():
    n_samples = 4000
    n_components = 4
    n_features = 5

    X, y_true = make_blobs(n_samples=n_samples,
                        n_features = n_features,
                        centers=n_components,
                        cluster_std=0.60,
                        random_state=0)
    return X


