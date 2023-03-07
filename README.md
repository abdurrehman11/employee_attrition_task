# Employee_Attrition_Task

## Prerequisites
Before running/cloning the code, make sure you have the following installed on your system:
- Operating System: Windows WSL/ Ubuntu
- Tools: Docker, Git

## Installation
To install the code, follow these steps:
- Clone the repository on your local machine using this command: 
  - git clone https://github.com/abdurrehman11/employee_attrition_task.git
- Open a command prompt or terminal window and navigate to the directory(`employee_attrition_task`) where the code is located.
- create a folder `mlflow_runs` in project directory to track mlflow runs.

## Git Branching Structure

<img width="569" alt="image" src="https://user-images.githubusercontent.com/24878579/223056933-a97c9934-d5f7-4579-b78a-ebc91a0c3884.png">

We will be following almost the above shown branching structure to manage code versioning and development collaboration.

## Code Overview
-	`data` --> this is a shared directory between train and inference pipeline and contains dataset and encoders that will be saved via train pipeline and used by inference pipeline.
-	`logs` --> this is a shared directory between train and inference pipeline logs and but currently have only train pipeline logs.
- `mlflow` --> this directory is used to share mlflow runs/models between train and inference pipeline (we need to create after code on local machine)
- `train_pipeline` --> this directory contains the train pipeline code modules like DataSet, Train, Evaluation class etc.
- `inference_pipeline` --> this directory contains the inference pipeline code module and API endpoint.
- `Dockerfile.train.feature` and `Dockerfile.infer.feature` are used to build local images and test local development of pipelines and `docker-compose.train.feature` and `docker-compose.infer.feature` are used to run the images locally. 
- `Dockerfile.train` and `Dockerfile.infer` are used to build images for `dev, qa and prod env` and `docker-compose.train` and `docker-compose.infer` are used to run the train and infer images on any env using env specific env variables. 

## How to Run/Test/Deploy

### Train Pipeline
- To run the train_pipeline on local machine, run the following command,
  - `docker-compose -f docker-compose.train.feature.yaml up`

- To run the train_pipeline on dev env, run the following command,
  - `CONFIG_FILE=config_dev.yaml BRANCH_TAG=dev docker-compose -f docker-compose.train.yaml up`

- To run the train_pipeline on uat env, run the following command,
  - `CONFIG_FILE=config_qa.yaml BRANCH_TAG=REL_UAT_V1.1 docker-compose -f docker-compose.train.yaml up`
  - You can pass `BRANCH_TAG` of current release that you want to test on qa.

- To run the train_pipeline on prod env, run the following command,
  - `CONFIG_FILE=config_prod.yaml BRANCH_TAG=REL_PROD_V1.1 docker-compose -f docker-compose.train.yaml up`
  - You can pass `BRANCH_TAG` of current release that you want to deploy on prod.

### Inference Pipeline
- To run the inference_pipeline on local machine, run the following command,
  - `docker-compose -f docker-compose.infer.feature.yaml up`

- To run the inference_pipeline on dev env, run the following command,
  - `CONFIG_FILE=config_dev.yaml BRANCH_TAG=dev docker-compose -f docker-compose.infer.yaml up`

- To run the inference_pipeline on uat env, run the following command,
  - `CONFIG_FILE=config_qa.yaml BRANCH_TAG=REL_UAT_V1.3 docker-compose -f docker-compose.infer.yaml up`
  - You can pass `BRANCH_TAG` of current release that you want to test on qa.

- To run the inference_pipeline on prod env, run the following command,
  - `CONFIG_FILE=config_prod.yaml BRANCH_TAG=REL_PROD_V1.1 docker-compose -f docker-compose.infer.yaml up`
  - You can pass `BRANCH_TAG` of current release that you want to deploy on prod.

- To test the `API endpoint` locally, enter this `URL: http://localhost:8080/docs` in your browser & copy/paste below request object in Request Body of `POST/predict` endpoint and hit Execute.

```
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
```

## Next Steps
- Set up logging for inference pipeline
- Exception handling for both train and inference pipeline
- Unit testing for both train and inference pipeline
- Cloud Infrastructure setup for project i.e. if we go for AWS, we can use AWS EC2 to deploy containers, setup MlFlow server, AWS S3 for datasets, models and other artifacts
- Post production monitoring of datasets, models and pipelines and take actions accordingly. e.g. retrain model based on model performance drift and data drift

## References
- https://towardsdatascience.com/how-to-structure-your-git-branching-strategy-by-a-data-engineer-45ff96857bb (Git Branching)
