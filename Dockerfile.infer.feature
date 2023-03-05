FROM python:3.8-slim-buster

# Set working directory
WORKDIR /inference_pipeline

COPY inference_pipeline/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

# Run API script
CMD ["uvicorn", "App:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]