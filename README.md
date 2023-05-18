# azuredevops

## Prerequirements

 <!-- - [Azure ML subscription parameters](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment) as config.json or login via `az login` -->
 - [miniconda](https://docs.conda.io/en/latest/miniconda.html) (with python version specified in `environment.yml`)
 - [Azure CLI (v2)](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
 - [optional] [vscode](https://code.visualstudio.com/)
 
 ## Installation
- Create env using conda: 
 ```bash
    conda env create -f environment.yml
 ```
- Log in to Azure:
```bash
    az login
```
- Install the Azure Machine Learning extension for CLI (v2):
```bash
    az extension add -n ml
```
# Monitoring tips

## What to Monitor:
I. DevOps pipelines  <br />
II. AML Pipelines and Model quality metrics  <br />
III. Dataset quality metrics (e.g. datadrift)  <br />
IV. Web service (performance + additional metrics)
 

## Levels:
1. Azure DevOps Pipelines (I):
    - dashboard: pipelines -> specific pipeline -> analytics
    - alerts: settings -> notifications
2. AML Pipelines (II):
    - dashboard: jobs -> specific experiment name -> (turn on include child jobs) charts
    -  alerts: add a step to check pipeline metrics history, and faile the pipeline if check will not pass -> see that pipeline is failed
        on Azure Devops Dashboard and recive an alert <br />
        OR
    - dashboard: jobs -> specific experiment name -> (turn on include child jobs) charts
    - alerts: use [some](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-log-pipelines-application-insights?view=azureml-api-1) library to put metrics to log analytics and invoke alerts
3. Tabular Build-In **(In preview)** Train Data Drift Detection (III):
    - dashboards: data -> dataset monitor
    - alerts: data -> dataset monitor
4. Online endpoint itself (IV):
    - dashboard: endpoint application insights -> workbooks or shared dashboard
    - alerts: endpoint application insights -> alerts
5. Infer Build-In **(In preview)** Data Drift monitoring (IV + III):
    - datadrift: [enable data collection](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-enable-data-collection?view=azureml-api-1), then dashboards: data -> dataset monitor
    - alerts: data -> dataset monitor <br />
        OR
    - [transfer data to a blob storage](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/tools/logicapps), then dashboards: data -> dataset monitor
    - alerts: data -> dataset monitor
6. Infer custom metrics (IV):
    - dashboard: endpoint application insights -> workbooks or shared dashboard
    - alerts: endpoint application insights -> alerts
7. Custom data monitoring (III):
    - Implement as an AML pipeline <br />
        OR
    - [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/monitor-visually)
 
## Other:
1. App Insight + Azure DevOps Integration https://learn.microsoft.com/en-us/azure/azure-monitor/app/continuous-monitoring
