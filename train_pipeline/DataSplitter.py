import pandas as pd
from sklearn.model_selection import train_test_split

class DataSplitter:
    def __init__(self, train_ratio=0.8, shuffle=True, stratify=None, random_seed=None):
        self.train_ratio = train_ratio
        self.shuffle = shuffle
        self.stratify = stratify
        self.random_seed = random_seed

    # this method can be used to implement other cross-validation techniques like
    # k-fold, time-series, multi-label etc.
    def split(self, data, target_col):
        X = data.drop(target_col, axis=1)
        y = data[target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, 
            y, 
            train_size=self.train_ratio, 
            shuffle=self.shuffle, 
            stratify=self.stratify, 
            random_state=self.random_seed
        )

        return X_train, y_train, X_test, y_test