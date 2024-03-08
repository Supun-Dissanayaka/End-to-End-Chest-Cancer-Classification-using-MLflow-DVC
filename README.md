# End-to-End-Chest-Cancer-Classification-using-MLflow-DVC

## Workflows

1.Update config.yaml <br>
2.Update secrets.yaml [Optional] <br>
3.Update params.yaml <br>
4.Update the entity <br>
5.Update the configuration manager in src config <br>
6.Update the components <br>
7.Update the pipeline <br>
8.Update the main.py <br>
9.Update the dvc.yaml


# CMD
- mlflow ui

# Dagshub
## [>>>>Dagshub<<<<](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/supunlakshan100/      End-to-End-Chest-Cancer-Classification-using-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=supunlakshan100 \
MLFLOW_TRACKING_PASSWORD=430a8eec27e5fab56a3a9cc4447bc0a001ee7974 \
python script.py

Run this to export as env variables:

export MLFLOW_TRACKING_URI=[https://dagshub.com/supunlakshan100/End-to-End-Chest-Cancer-Classification-using-MLflow-DVC.mlflow] <br>

export MLFLOW_TRACKING_USERNAME=supunlakshan100 <br>

export MLFLOW_TRACKING_PASSWORD=430a8eec27e5fab56a3a9cc4447bc0a001ee7974



# DVC cmd 

1.dvc init <br>
2.dvc repro <br>
3.dvc dag <br>
4.About MLflow & DVC <br>
5.MLflow

Its Production Grade
Trace all of your expriements
Logging & taging your model
DVC

Its very lite weight for POC only
lite weight expriements tracker
It can perform Orchestration (Creating Pipelines)