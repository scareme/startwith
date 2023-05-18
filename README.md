# Levels:
1. Azure DevOps Pipelines (I):
    - dashboard: pipelines -> specific pipeline -> analytics
    - alerts: settings -> notifications
2. AML Pipelines (II):
    - dashboard: jobs -> specific experiment name -> (turn on include child jobs) charts
    -  alerts: add a step to check pipeline metrics history, and fail the pipeline if check will not pass -> see that pipeline is failed on Azure Devops Dashboard and recive an alert <br />
        OR
    - dashboard: jobs -> specific experiment name -> (turn on include child jobs) charts
    - alerts: use [OpenCensys](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-log-pipelines-application-insights?view=azureml-api-1) python library to put metrics to log analytics and invoke alerts
3.  Tabular Build-In Train Data Drift Detection (III):
    - dashboards: data -> dataset monitor
    - alerts: data -> dataset monitor  <br />
        methods:
    - **[In preview]** Build-In Train Data Drift Detection
    - manual written solution
4. Online endpoint itself (IV):
    - dashboard: endpoint application insights -> workbooks or shared dashboard
    - alerts: endpoint application insights -> alerts
5. Infer Data Drift monitoring (IV + III):
    - dashboard: **[In preview]** [enable data collection](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-enable-data-collection?view=azureml-api-1), then dashboards: data -> dataset monitor
    - alerts: data -> dataset monitor <br />
        OR
    - [transfer data to a blob storage with Logic App](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-export-logic-app), then dashboards: data -> dataset monitor
    - alerts: data -> dataset monitor <br />
        OR
    - dashboards: [transform](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-transformations) data from Azure monitor by a rule and save as a table, then send to a Log Analytics Workspace (automatically), then export by **[Will be depricated]** **[Not supported in China]**["continuous export"](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/app/export-telemetry), then as in item 3 or 7.
    - alerts: data -> dataset monitor <br />
        OR
    - dashboards: AML Pipeline + [Application Insights Rest API](https://learn.microsoft.com/en-us/rest/api/application-insights/) and [Monitor Query Python API](https://learn.microsoft.com/en-us/python/api/overview/azure/monitor-query-readme?view=azure-python), send to a blob storage, then as in item 3 or 7.
    - alerts: data -> dataset monitor  <br />
        methods:
    - **[In preview]** Build-In Train Data Drift Detection
    - manual written solution
6. Infer custom metrics (IV):
    - dashboard: endpoint application insights -> workbooks or shared dashboard
    - alerts: endpoint application insights -> alerts
7. Custom data monitoring (III):
    - Implement as an AML pipeline <br />
        OR
    - [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/monitor-visually)
 
# Other:
1. App Insight + Azure DevOps Integration https://learn.microsoft.com/en-us/azure/azure-monitor/app/continuous-monitoring
