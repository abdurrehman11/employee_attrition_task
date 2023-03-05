import os 
import yaml
import pandas as pd
from Constants import Constants

from EmployeeAttritionDataset import EmployeeAttritionDataset
from Train import Train


class Driver:
    def __init__(self):
        config_file = os.environ.get(Constants.CONFIG_FILE.value, Constants.DEFAULT_CONFIG_FILE.value)
        config_path = os.path.abspath(os.path.join( Constants.CONFIGS.value, config_file))
        
        with open(config_path) as f:
            self.config = yaml.safe_load(f)


if __name__ == '__main__':
    driver = Driver()
    config = driver.config
    print(config)

    # Load and preprocess dataset
    employee_dataset = EmployeeAttritionDataset(config)
    train_test_splits = employee_dataset.preprocess()

    # train and evaluate model
    train = Train(config, train_test_splits)
    train.train_model()
    train.evaluate_model()
    train.create_experiment()
    