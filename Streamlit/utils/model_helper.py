import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class P95Capper(BaseEstimator, TransformerMixin):
    """Cap kolom 'campaign' di P95, dihitung dari training data saja."""
    def __init__(self, col_idx):
        self.col_idx = col_idx

    def fit(self, X, y=None):
        self.cap_ = np.percentile(X[:, self.col_idx], 95)
        self.n_features_in_ = X.shape[1]
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_[:, self.col_idx] = np.clip(X_[:, self.col_idx], a_min=None, a_max=self.cap_)
        return X_

    def get_feature_names_out(self, input_features=None):
        if input_features is not None:
            return np.array(input_features)
        return np.array([f"x{i}" for i in range(self.n_features_in_)])
