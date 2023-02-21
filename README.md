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
