from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


class Models:
    def __init__(self):
        pass

    def get_model(self, model_name):
        if model_name == "logistic_regression":
            return LogisticRegression()
        elif model_name == "random_forest":
            return RandomForestClassifier(verbose=2)
        else:
            raise ValueError(f"Unknown model name: {model_name}")