import os

from google.cloud import storage
from termcolor import colored
from pasture_predict.params import BUCKET_NAME, MODEL_NAME, MODEL_VERSION


def storage_upload(filename, rm=False):
    client = storage.Client().bucket(BUCKET_NAME)

    local_model_name = f"{filename}model.joblib"
    storage_location = f"models/{MODEL_NAME}/{MODEL_VERSION}/{local_model_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename(f"{filename}model.joblib")
    print(colored(f"=> model.joblib uploaded to bucket {BUCKET_NAME} inside {storage_location}",
                  "green"))
    if rm:
        os.remove(f"{filename}model.joblib")
