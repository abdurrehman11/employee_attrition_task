import os
import sys 
import yaml
import pandas as pd
import logging

from Constants import Constants
from EmployeeAttritionDataset import EmployeeAttritionDataset
from Train import Train


class Driver:
    def __init__(self):
        branch_tag = os.environ.get(Constants.BRANCH_TAG.value, Constants.DEFAULT_BRANCH_TAG.value)
        config_file = os.environ.get(Constants.CONFIG_FILE.value, Constants.DEFAULT_CONFIG_FILE.value)
        config_path = os.path.abspath(os.path.join( Constants.CONFIGS.value, config_file))
        
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        self.config.update({Constants.BRANCH_TAG.value: branch_tag})

        self.initialize_logger()

    def initialize_logger(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME.value)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(funcName)s - %(message)s')

        # Log to console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        self.logger.addHandler(console_handler)

        # Log to file
        log_file_path = os.path.join(os.path.sep, Constants.LOG_DIR.value, Constants.LOG_FILE.value)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)

    def run_pipeline(self):
        # Load and preprocess dataset
        self.logger.info("Train Pipeline execution Started")
        employee_dataset = EmployeeAttritionDataset(self.config, self.logger)
        train_test_splits = employee_dataset.preprocess()

        # train and evaluate model
        train = Train(self.config, self.logger, train_test_splits)
        train.train_model()
        train.evaluate_model()
        train.create_experiment()
        
        self.logger.info("Train Pipeline execution Completed!")

if __name__ == '__main__':
    driver = Driver()
    driver.run_pipeline()
