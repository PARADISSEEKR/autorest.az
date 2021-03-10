# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_attached_database_configuration_create
from .example_steps import step_attached_database_configuration_show
from .example_steps import step_attached_database_configuration_list
from .example_steps import step_cluster_create
from .example_steps import step_cluster_show
from .example_steps import step_cluster_list
from .example_steps import step_cluster_list2
from .example_steps import step_cluster_list_sku
from .example_steps import step_cluster_list_sku2
from .example_steps import step_cluster_update
from .example_steps import step_cluster_add_language_extension
from .example_steps import step_cluster_detach_follower_database
from .example_steps import step_cluster_diagnose_virtual_network
from .example_steps import step_cluster_list_follower_database
from .example_steps import step_cluster_list_language_extension
from .example_steps import step_cluster_remove_language_extension
from .example_steps import step_cluster_start
from .example_steps import step_cluster_stop
from .example_steps import step_cluster_principal_assignment_create
from .example_steps import step_cluster_principal_assignment_show
from .example_steps import step_cluster_principal_assignment_list
from .example_steps import step_database_principal_assignment_create
from .example_steps import step_database_principal_assignment_show
from .example_steps import step_database_principal_assignment_list
from .example_steps import step_database_principal_assignment_delete
from .example_steps import step_database_create
from .example_steps import step_database_show
from .example_steps import step_database_list
from .example_steps import step_database_update
from .example_steps import step_database_add_principal
from .example_steps import step_database_list_principal
from .example_steps import step_database_remove_principal
from .example_steps import step_database_delete
from .example_steps import step_data_connection_create
from .example_steps import step_data_connection_list
from .example_steps import step_data_connection_show
from .example_steps import step_data_connection_update
from .example_steps import step_data_connection_data_connection_validation
from .example_steps import step_data_connection_delete
from .example_steps import step_cluster_delete
from .example_steps import step_attached_database_configuration_delete
from .example_steps import step_cluster_principal_assignment_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    step_attached_database_configuration_create(test, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("clusterResourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Kusto"
                   "/Clusters/{myCluster3}", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
    ])
    step_attached_database_configuration_show(test, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("defaultPrincipalsModificationKind", "Union", case_sensitive=False),
    ])
    step_attached_database_configuration_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_create(test, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enableDoubleEncryption", False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step_cluster_show(test, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
    ])
    step_cluster_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_list2(test, checks=[
        test.check('length(@)', 1),
    ])
    step_cluster_list_sku(test, checks=[])
    step_cluster_list_sku2(test, checks=[])
    step_cluster_update(test, checks=[
        test.check("name", "{myCluster}", case_sensitive=False),
        test.check("identity.type", "SystemAssigned", case_sensitive=False),
        test.check("location", "westus", case_sensitive=False),
        test.check("enablePurge", True),
        test.check("enableStreamingIngest", True),
        test.check("sku.name", "Standard_L8s", case_sensitive=False),
        test.check("sku.capacity", 2),
        test.check("sku.tier", "Standard", case_sensitive=False),
        test.check("keyVaultProperties.keyName", "keyName", case_sensitive=False),
        test.check("keyVaultProperties.keyVaultUri", "https://dummy.keyvault.com", case_sensitive=False),
        test.check("keyVaultProperties.keyVersion", "keyVersion", case_sensitive=False),
    ])
    step_cluster_add_language_extension(test, checks=[])
    step_cluster_detach_follower_database(test, checks=[])
    step_cluster_diagnose_virtual_network(test, checks=[])
    step_cluster_list_follower_database(test, checks=[])
    step_cluster_list_language_extension(test, checks=[])
    step_cluster_remove_language_extension(test, checks=[])
    step_cluster_start(test, checks=[])
    step_cluster_stop(test, checks=[])
    step_cluster_principal_assignment_create(test, checks=[])
    step_cluster_principal_assignment_show(test, checks=[])
    step_cluster_principal_assignment_list(test, checks=[])
    step_database_principal_assignment_create(test, checks=[])
    step_database_principal_assignment_show(test, checks=[])
    step_database_principal_assignment_list(test, checks=[])
    step_database_principal_assignment_delete(test, checks=[])
    step_database_create(test, checks=[])
    step_database_show(test, checks=[])
    step_database_list(test, checks=[])
    step_database_update(test, checks=[])
    step_database_add_principal(test, checks=[])
    step_database_list_principal(test, checks=[])
    step_database_remove_principal(test, checks=[])
    step_database_delete(test, checks=[])
    step_data_connection_create(test, checks=[])
    step_data_connection_list(test, checks=[
        test.check('length(@)', 1),
    ])
    step_data_connection_show(test, checks=[])
    step_data_connection_update(test, checks=[])
    step_data_connection_data_connection_validation(test, checks=[])
    step_data_connection_delete(test, checks=[])
    step_cluster_delete(test, checks=[])
    step_attached_database_configuration_delete(test, checks=[])
    step_cluster_principal_assignment_delete(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class KustoScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(KustoScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myCluster4': 'default',
            'myAttachedDatabaseConfiguration3': 'default',
            'myCluster2': 'leader4',
            'myCluster3': 'KustoClusterLeader',
            'myCluster': 'kustoclusterrptest4',
            'myAttachedDatabaseConfiguration': 'myAttachedDatabaseConfiguration',
            'myAttachedDatabaseConfiguration2': 'attachedDatabaseConfigurations1',
            'myDataConnection': 'DataConnections8',
            'myDataConnection2': 'kustoeventhubconnection1',
        })

    @ResourceGroupPreparer(name_prefix='clitestkusto_kustorptest'[:7], key='rg', parameter_name='rg')
    def test_kusto_Scenario(self, rg):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
