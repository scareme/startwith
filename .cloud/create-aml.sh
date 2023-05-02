LOCATION='northeurope'                                        
RESOURCE_GROUP_NAME='test-devops-aml-rg'
AML_WORKSPACE_NAME='test-devops-aml-ws'

# Create a resource group
az group create \
    --location $LOCATION \
    --name $RESOURCE_GROUP_NAME

# Create an Azure Machine Learning workspace
az ml workspace create \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $AML_WORKSPACE_NAME
