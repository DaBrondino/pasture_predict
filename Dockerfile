FROM python:3.8.6-buster

COPY api /api
COPY pasture_predict /pasture_predict
COPY sanluismodel.joblib /model.joblib
COPY vieytesmodel.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
