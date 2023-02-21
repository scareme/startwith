# Overview
Contains cloud-specific code like templates to create an Azure Machine Learning workspace

## Installation
- Create a resource group and set as default
```bash
    $ az group create --name "some-group-name-dev-rg" --location "some-location"
    $ az configure --defaults group="some-group-name-dev-rg"
```
- по идее надо просто в отдельный баш файл
