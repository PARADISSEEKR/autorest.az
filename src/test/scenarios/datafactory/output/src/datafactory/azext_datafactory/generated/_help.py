# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['datafactory'] = """
    type: group
    short-summary: datafactory
"""

helps['datafactory list'] = """
    type: command
    short-summary: Lists factories under the specified subscription.
    examples:
      - name: Factories_ListByResourceGroup
        text: |-
               az datafactory list --resource-group "exampleResourceGroup"
"""

helps['datafactory show'] = """
    type: command
    short-summary: Gets a factory.
    examples:
      - name: Factories_Get
        text: |-
               az datafactory show --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory create'] = """
    type: command
    short-summary: Creates or updates a factory.
    examples:
      - name: Factories_CreateOrUpdate
        text: |-
               az datafactory create --location "East US" --factory-name "exampleFactoryName" --resource-group "example\
ResourceGroup"
"""

helps['datafactory update'] = """
    type: command
    short-summary: Updates a factory.
    examples:
      - name: Factories_Update
        text: |-
               az datafactory update --factory-name "exampleFactoryName" --tags exampleTag="exampleValue" --resource-gr\
oup "exampleResourceGroup"
"""

helps['datafactory delete'] = """
    type: command
    short-summary: Deletes a factory.
    examples:
      - name: Factories_Delete
        text: |-
               az datafactory delete --factory-name "exampleFactoryName" --resource-group "exampleResourceGroup"
"""

helps['datafactory configure-factory-repo'] = """
    type: command
    short-summary: Updates a factory's repo information.
    examples:
      - name: Factories_ConfigureFactoryRepo
        text: |-
               az datafactory configure-factory-repo --factory-resource-id "/subscriptions/12345678-1234-1234-1234-1234\
5678abc/resourceGroups/exampleResourceGroup/providers/Microsoft.DataFactory/factories/exampleFactoryName" --factory-vst\
s-configuration account-name="ADF" collaboration-branch="master" last-commit-id="" project-name="project" repository-na\
me="repo" root-folder="/" tenant-id="" --location-id "East US"
"""

helps['datafactory get-data-plane-access'] = """
    type: command
    short-summary: Get Data Plane access.
    examples:
      - name: Factories_GetDataPlaneAccess
        text: |-
               az datafactory get-data-plane-access --factory-name "exampleFactoryName" --access-resource-path "" --exp\
ire-time "2018-11-10T09:46:20.2659347Z" --permissions "r" --profile-name "DefaultProfile" --start-time "2018-11-10T02:4\
6:20.2659347Z" --resource-group "exampleResourceGroup"
"""

helps['datafactory get-git-hub-access-token'] = """
    type: command
    short-summary: Get GitHub Access Token.
    examples:
      - name: Factories_GetGitHubAccessToken
        text: |-
               az datafactory get-git-hub-access-token --factory-name "exampleFactoryName" --git-hub-access-code "some"\
 --git-hub-access-token-base-url "some" --git-hub-client-id "some" --resource-group "exampleResourceGroup"
"""