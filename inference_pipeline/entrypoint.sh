#!/bin/bash

# Clone the repository
git clone https://github.com/abdurrehman11/employee_attrition_task.git &&
cd employee_attrition_task &&

# Check if BRANCH_TAG environment variable is set to DEV
if [ "$BRANCH_TAG" == "dev" ]; then
    echo "checkout the $BRANCH_TAG branch"
    git checkout $BRANCH_TAG
else
    echo "Checkout the tag: $BRANCH_TAG" 
    git checkout $BRANCH_TAG
fi

git fetch --tags &&
cd inference_pipeline

sleep 10

uvicorn App:app --reload --host 0.0.0.0 --port 8080
