from fastapi import FastAPI

from Employee import Employee
from Predict import Predict

app = FastAPI()

predict_api = Predict()


@app.post("/predict")
def predict_emp_attrition_api(employee: Employee):
    print("====== Going to call predict func ===============")
    return predict_api.predict_employee_attrition(employee)