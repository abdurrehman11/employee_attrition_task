from enum import Enum

class Constants(Enum):
    CONFIGS = 'configs'
    CONFIG_FILE = 'CONFIG_FILE'
    DEFAULT_CONFIG_FILE = 'config_dev.yaml'

    DATASET_PATH = 'dataset_path'
    OHE_ENCODER_PATH = 'ohe_encoder_path'
    TARGET_ENCODER_PATH = 'target_encoder_path'
    CATEGORICAL_COLS = 'categorical_cols'
    TARGET_COL = 'target_col'

    TRAIN_SPLIT_RATIO = 'train_split_ratio'
    MODEL_NAME = 'model_name'

    EXPERIMENT_NAME = 'experiment_name'
    EXPERIMENT_ID = 'experiment_id'
    RUN_NAME = 'run_name'
    MLFLOW_TRACKING_URI = 'mlflow_tracking_uri'
    MLFLOW_RUN_ROC_AUC = 'metrics.roc_auc'
    MLFLOW_METRIC_ORDER = 'mlflow_metric_order'
    MLFLOW_RUN_ID = 'run_id'
    