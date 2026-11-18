import os

import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
client = MlflowClient()

experiment = client.get_experiment_by_name(os.environ["MLFLOW_EXPERIMENT_NAME"])
runs = client.search_runs(
    [experiment.experiment_id],
    order_by=["attributes.start_time DESC"],
    max_results=1,
)
run_id = runs[0].info.run_id
print(f"Latest run: {run_id}")

# Télécharge le dossier "model" dans /app/model
mlflow.artifacts.download_artifacts(run_id=run_id, artifact_path="model", dst_path=".")