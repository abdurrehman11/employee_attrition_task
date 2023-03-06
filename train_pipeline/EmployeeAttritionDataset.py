import pandas as pd 

from DataSplitter import DataSplitter
from CategoricalEncoder import CategoricalEncoder
from Constants import Constants


class EmployeeAttritionDataset:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def load_dataset(self):
        self.logger.info(f"Going to load dataset from {self.config[Constants.DATASET_PATH.value]}")
        self.data = pd.read_csv(self.config[Constants.DATASET_PATH.value])
        self.logger.info(f"Dataset loaded successfully with shape: {self.data.shape}")

    def preprocess(self):
        # Create an instance of the CategoricalEncoder class
        self.encoder = CategoricalEncoder(
            ohe_path=self.config[Constants.OHE_ENCODER_PATH.value],
            target_enc_path=self.config[Constants.TARGET_ENCODER_PATH.value],
            categorical_cols=self.config[Constants.CATEGORICAL_COLS.value],
            target_col=self.config[Constants.TARGET_COL.value]
        )

        # load the dataset
        self.load_dataset()

        # Fit and transform the data using the encoder
        encoded_data = self.encoder.fit_transform(self.data)
        self.logger.info(f"Dataset shape after preprocessing: {encoded_data.shape}")

        # Split the data with stratification
        self.splitter = DataSplitter(
            train_ratio=self.config[Constants.TRAIN_SPLIT_RATIO.value], 
            shuffle=True, 
            stratify=self.data[self.config[Constants.TARGET_COL.value]], 
            random_seed=42
        )

        X_train, y_train, X_test, y_test = self.splitter.split(encoded_data, self.config[Constants.TARGET_COL.value])
        self.logger.info(f"Splitted dataset into train and test with shapes, "
                         f"X_train: {X_train.shape}, y_train: {y_train.shape}, X_test: {X_test.shape}, y_test: {y_test.shape}")
        
        train_test_splits = [X_train, y_train, X_test, y_test]
        
        return train_test_splits
