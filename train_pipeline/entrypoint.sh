#!/bin/bash

# Clone the repository
git clone https://github.com/abdurrehman11/employee_attrition_task.git &&
cd employee_attrition_task/train_pipeline &&
git fetch --tags &&

# Check if BRANCH_TAG environment variable is set to DEV
if [ "$BRANCH_TAG" == "DEV" ]; then
    echo "checkout the dev branch"
    git checkout dev
else
    echo "Checkout the tag: $BRANCH_TAG" 
    git checkout $BRANCH_TAG
fi

python Driver.py

sleep 10

mlflow ui --backend-store-uri=file:///mlflow_runs --host=0.0.0.0 --port=5000
