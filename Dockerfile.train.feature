FROM python:3.8-slim-buster

# Set working directory
WORKDIR /train_pipeline

COPY train_pipeline/requirements.txt .
RUN pip install -r requirements.txt

# RUN python test_train.py
EXPOSE 5000

# Run training script
# CMD python Driver.py
CMD ["/bin/bash", "-c", "python Driver.py; mlflow ui --backend-store-uri=file:///mlflow_runs --host=0.0.0.0 --port=5000"]