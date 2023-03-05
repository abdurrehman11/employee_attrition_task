# employee_attrition_task

docker build -t attrition_train_image -f Dockerfile.train.feature .

# Run only train
docker run -e CONFIG_FILE=config_dev.yaml -v ${PWD}/train_pipeline:/train_pipeline -v ${PWD}/data:/data attrition_train_image

# to run MLFlow 
docker run -p 5000:5000 -e CONFIG_FILE=config_dev.yaml -v ${PWD}/train_pipeline:/train_pipeline -v ${PWD}/data:/data attrition_train_image

# run MLFlow with host artifact directory
docker run -p 5000:5000  -e CONFIG_FILE=config_dev.yaml -v ${PWD}/train_pipeline:/train_pipeline -v ${PWD}/data:/data -v ${PWD}/mlflow_runs:/mlflow_runs attrition_train_image

# run docker-compose by specifying file name
docker-compose -f docker-compose.train.feature.yaml up

docker-compose -e CONFIG_FILE=config_dev.yaml -e BRANCH_TAG=dev -f docker-compose.train.yaml up

# to build image whenever you run docker-compose up
docker-compose up --build


docker run -p 5000:5000 -e CONFIG_FILE=config_dev.yaml -v ${PWD}/train_pipeline:/train_pipeline -v ${PWD}/data:/data emp_train_image

docker run -it -v ${PWD}/train_pipeline:/train_pipeline -v ${PWD}/data:/data emp_train_image /bin/bash

docker run -p 5000:5000 -v ${PWD}/train_pipeline:/train_pipeline -v ${PWD}/data:/train_pipeline/data -v ${PWD}/configs:/train_pipeline/configs emp_train_image



----------------------------------------------------------------------

docker build -t emp_infer_image -f Dockerfile.infer .

docker run -p 8080:8080 -e CONFIG_FILE=config_dev.yaml -v ${PWD}/inference_pipeline:/inference_pipeline -v ${PWD}/data:/data -v ${PWD}/mlflow_runs:/mlflow_runs emp_infer_image


{
  "Age": 41,		
  "BusinessTravel": "Travel_Rarely",
  "DailyRate": 1102,	
  "Department": "Sales",	
  "DistanceFromHome": 1,	
  "Education": 2,
  "EducationField": "Life Sciences",	
  "EmployeeCount": 1,
  "EmployeeNumber": 1,	
  "EnvironmentSatisfaction": 2,	
  "Gender": "Female",
  "HourlyRate": 94,	
  "JobInvolvement": 3,	
  "JobLevel": 2,
  "JobRole": "Sales Executive",	
  "JobSatisfaction": 4,
  "MaritalStatus": "Single",	
  "MonthlyIncome": 5993,	
  "MonthlyRate": 19479,
  "NumCompaniesWorked": 8,	
  "Over18": "Y",
  "OverTime": "Yes",	
  "PercentSalaryHike": 11,	
  "PerformanceRating": 3,	
  "RelationshipSatisfaction": 1,	
  "StandardHours": 80,
  "StockOptionLevel": 0,	
  "TotalWorkingYears": 8,	
  "TrainingTimesLastYear": 0,	
  "WorkLifeBalance": 1,
  "YearsAtCompany": 6,	
  "YearsInCurrentRole": 4,	
  "YearsSinceLastPromotion": 0,	
  "YearsWithCurrManager": 5
}