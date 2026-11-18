FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY fetch_model.py .

ARG MLFLOW_TRACKING_URI
ARG MLFLOW_EXPERIMENT_NAME

# Les identifiants DagsHub sont passés en secrets de build : ils ne restent pas dans l'image
RUN --mount=type=secret,id=dagshub_user \
    --mount=type=secret,id=dagshub_token \
    MLFLOW_TRACKING_USERNAME="$(cat /run/secrets/dagshub_user)" \
    MLFLOW_TRACKING_PASSWORD="$(cat /run/secrets/dagshub_token)" \
    python fetch_model.py

COPY app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]