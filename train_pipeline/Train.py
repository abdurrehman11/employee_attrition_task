import mlflow

from Models import Models
from Evaluate import Evaluate
from Constants import Constants


class Train:
    def __init__(self, config, train_test_splits):
        self.config = config
        self.models = Models()
        self.X_train, self.y_train, self.X_test, self.y_test = train_test_splits

    def train_model(self):
        self.model = self.models.get_model(self.config[Constants.MODEL_NAME.value])
        print(f"========= Going to start {self.config[Constants.MODEL_NAME.value]} model training... ========")
        self.model.fit(self.X_train, self.y_train)
        print("============ Model training completed! ===============")

    def evaluate_model(self):
        self.y_pred_prob = self.model.predict_proba(self.X_test)[:, 1]
        evaluate = Evaluate(self.y_test, self.y_pred_prob)
        self.eval_metrics = evaluate.get_evaluation_metrics()
        print(f"Model Evaluation Metrics: {self.eval_metrics}")

    def create_experiment(self):
        # Initialize MLflow
        mlflow.set_tracking_uri(self.config[Constants.MLFLOW_TRACKING_URI.value])
        mlflow.set_experiment(self.config[Constants.EXPERIMENT_NAME.value])

        mlflow_run_name = (self.config[Constants.BRANCH_TAG.value] + "_" + 
                           self.config[Constants.RUN_NAME.value])
        
        with mlflow.start_run(
            run_name=mlflow_run_name,
            description='Employee Attrition - Random Forest Experiment Tracking'
        ):
            self.model_params = self.model.get_params()
            
            # log model params
            mlflow.log_params(self.model_params)
                
            # log evaluation metrics
            mlflow.log_metrics(self.eval_metrics)
            
            # save trained model in registry
            mlflow.sklearn.log_model(self.model, self.config[Constants.MODEL_NAME.value])

            # mlflow.log_artifact(confusion_matrix_path, 'confusion_matrix')
            # mlflow.log_artifact(roc_auc_plot_path, "roc_auc_plot")
            
            mlflow.set_tag(Constants.BRANCH_TAG.value, self.config[Constants.BRANCH_TAG.value])
                
        print(f'Run - {mlflow_run_name} is logged to Experiment - {self.config[Constants.EXPERIMENT_NAME.value]}')

