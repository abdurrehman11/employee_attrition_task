import os
import yaml
import joblib
import joblib
import pandas as pd 
import numpy as np
import mlflow

from Employee import Employee
from Constants import Constants

class Predict:
    def __init__(self):
        config_file = os.environ.get(Constants.CONFIG_FILE.value, Constants.DEFAULT_CONFIG_FILE.value)
        config_path = os.path.abspath(os.path.join( Constants.CONFIGS.value, config_file))
        
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        self.ohe_preprocessor = joblib.load(self.config[Constants.OHE_ENCODER_PATH.value])
        self.trg_encoder = joblib.load(self.config[Constants.TARGET_ENCODER_PATH.value])

        # load best run model
        self.load_best_run_model()

    def load_best_run_model(self):
        mlflow.set_tracking_uri(self.config[Constants.MLFLOW_TRACKING_URI.value])

        # get the best from all the runs
        current_experiment = dict(mlflow.get_experiment_by_name(
            self.config[Constants.EXPERIMENT_NAME.value]
        ))
        experiment_id = current_experiment[Constants.EXPERIMENT_ID.value]
        search_order_by_metric = (Constants.MLFLOW_RUN_ROC_AUC.value + " " + 
                                  self.config[Constants.MLFLOW_METRIC_ORDER.value]) 
        
        df = mlflow.search_runs([experiment_id], order_by = [search_order_by_metric])
        best_run_id = df.loc[0, Constants.MLFLOW_RUN_ID.value]

        model_path = f'runs:/{best_run_id}/{self.config[Constants.MODEL_NAME.value]}'
        self.model = mlflow.sklearn.load_model(model_path)

        print(f"Loaded {self.config[Constants.MODEL_NAME.value]} from MLflow successfully!")

    def process_features(self, feat_dict):
        data = pd.DataFrame([feat_dict])

        categorical_cols = self.config[Constants.CATEGORICAL_COLS.value]
        categorical_data = data[categorical_cols]
        numerical_data = data.drop(columns=categorical_cols).values

        encoded_data = self.ohe_preprocessor.transform(categorical_data)
        features = np.concatenate((encoded_data, numerical_data), axis=1)

        return features

    def predict_employee_attrition(self, employee: Employee):
        employee_dict = employee.__dict__
        features = self.process_features(employee_dict)
        predict_attrition = self.trg_encoder.inverse_transform(self.model.predict(features))[0]
        employee_dict.update({self.config[Constants.TARGET_COL.value]: predict_attrition})

        return employee_dict
