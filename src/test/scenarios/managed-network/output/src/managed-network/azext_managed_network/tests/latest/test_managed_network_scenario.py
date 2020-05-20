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
from .. import try_manual, raise_if
from azure.cli.testsdk import ResourceGroupPreparer
from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: ManagedNetworksPut
@try_manual
def step_managednetworksput(test, rg):
    test.cmd('az managed-network mn create '
             '--location "eastus" '
             '--properties "{{\\"managementGroups\\":[{{\\"id\\":\\"/providers/Microsoft.Management/managementGroups/20'
             '000000-0001-0000-0000-000000000000\\"}},{{\\"id\\":\\"/providers/Microsoft.Management/managementGroups/20'
             '000000-0002-0000-0000-000000000000\\"}}],\\"subscriptions\\":[{{\\"id\\":\\"subscriptionA\\"}},{{\\"id\\"'
             ':\\"subscriptionB\\"}}],\\"virtualNetworks\\":[{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGro'
             'ups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn}\\"}},{{\\"id\\":\\"/subscriptions/{subscription'
             '_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vn_2}\\"}}],\\"subnets\\":[{{\\"id'
             '\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{'
             'vn_3}/subnets/default\\"}},{{\\"id\\":\\"/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/M'
             'icrosoft.Network/virtualNetworks/{vn_3}/subnets/default\\"}}]}}" '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagementNetworkGroupsPut
@try_manual
def step_managementnetworkgroupsput(test, rg):
    test.cmd('az managed-network mn group create '
             '--management-groups "[]" '
             '--subnets id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/V'
             'netA/subnets/subnetA" '
             '--virtual-networks id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualN'
             'etworks/VnetA" '
             '--virtual-networks id="/subscriptionB/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualN'
             'etworks/VnetB" '
             '--group-name "{myManagedNetworkGroup1}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az managed-network mn group wait --created '
             '--group-name "{myManagedNetworkGroup1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ScopeAssignmentsPut
@try_manual
def step_scopeassignmentsput(test, rg):
    test.cmd('az managed-network mn scope-assignment create '
             '--assigned-managed-network "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Mana'
             'gedNetwork/managedNetworks/{myManagedNetwork}" '
             '--scope "subscriptions/subscriptionC" '
             '--name "{subscriptionCAssignment}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesPut
@try_manual
def step_managednetworkpeeringpoliciesput(test, rg):
    test.cmd('az managed-network managed-network-peering-policy hub-and-spoke-topology create '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myHubAndSpoke}" '
             '--hub id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetwork'
             's/{vn_4}" '
             '--spokes id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.ManagedNetwork/mana'
             'gedNetworks/{myManagedNetwork}/managedNetworkGroups/{myManagedNetworkGroup1}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksGet
@try_manual
def step_managednetworksget(test, rg):
    test.cmd('az managed-network mn get-modify '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksListByResourceGroup
@try_manual
def step_managednetworkslistbyresourcegroup(test, rg):
    test.cmd('az managed-network mn list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksListBySubscription
@try_manual
def step_managednetworkslistbysubscription(test, rg):
    test.cmd('az managed-network mn list '
             '-g ""',
             checks=[])


# EXAMPLE: ScopeAssignmentsGet
@try_manual
def step_scopeassignmentsget(test, rg):
    test.cmd('az managed-network mn scope-assignment show '
             '--scope "subscriptions/subscriptionC" '
             '--name "{subscriptionCAssignment}"',
             checks=[])


# EXAMPLE: ScopeAssignmentsList
@try_manual
def step_scopeassignmentslist(test, rg):
    test.cmd('az managed-network mn scope-assignment list '
             '--scope "subscriptions/subscriptionC"',
             checks=[])


# EXAMPLE: ManagementNetworkGroupsGet
@try_manual
def step_managementnetworkgroupsget(test, rg):
    test.cmd('az managed-network mn group show '
             '--group-name "{myManagedNetworkGroup1}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksGroupsListByManagedNetwork
@try_manual
def step_managednetworksgroupslistbymanagednetwork(test, rg):
    test.cmd('az managed-network mn group list '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesGet
@try_manual
def step_managednetworkpeeringpoliciesget(test, rg):
    test.cmd('az managed-network managed-network-peering-policy show '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myHubAndSpoke}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesListByManagedNetwork
@try_manual
def step_managednetworkpeeringpolicieslistbymanagednetwork(test, rg):
    test.cmd('az managed-network managed-network-peering-policy list '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworkPeeringPoliciesDelete
@try_manual
def step_managednetworkpeeringpoliciesdelete(test, rg):
    test.cmd('az managed-network managed-network-peering-policy delete '
             '--managed-network-name "{myManagedNetwork}" '
             '--policy-name "{myHubAndSpoke}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ScopeAssignmentsDelete
@try_manual
def step_scopeassignmentsdelete(test, rg):
    test.cmd('az managed-network mn scope-assignment delete '
             '--scope "subscriptions/subscriptionC" '
             '--name "{subscriptionCAssignment}"',
             checks=[])


# EXAMPLE: ManagementNetworkGroupsDelete
@try_manual
def step_managementnetworkgroupsdelete(test, rg):
    test.cmd('az managed-network mn group delete '
             '--group-name "{myManagedNetworkGroup1}" '
             '--managed-network-name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: ManagedNetworksDelete
@try_manual
def step_managednetworksdelete(test, rg):
    test.cmd('az managed-network mn delete '
             '--name "{myManagedNetwork}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step_managednetworksput(test, rg)
    step_managementnetworkgroupsput(test, rg)
    step_scopeassignmentsput(test, rg)
    step_managednetworkpeeringpoliciesput(test, rg)
    step_managednetworksget(test, rg)
    step_managednetworkslistbyresourcegroup(test, rg)
    step_managednetworkslistbysubscription(test, rg)
    step_scopeassignmentsget(test, rg)
    step_scopeassignmentslist(test, rg)
    step_managementnetworkgroupsget(test, rg)
    step_managednetworksgroupslistbymanagednetwork(test, rg)
    step_managednetworkpeeringpoliciesget(test, rg)
    step_managednetworkpeeringpolicieslistbymanagednetwork(test, rg)
    step_managednetworkpeeringpoliciesdelete(test, rg)
    step_scopeassignmentsdelete(test, rg)
    step_managementnetworkgroupsdelete(test, rg)
    step_managednetworksdelete(test, rg)
    cleanup(test, rg)


@try_manual
class ManagedNetworkManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestmanaged_network_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetA'[:7], key='vn', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetB'[:7], key='vn_2', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_VnetC'[:7], key='vn_3', resource_group_key='rg')
    @VirtualNetworkPreparer(name_prefix='clitestmanaged_network_myHubVnet'[:7], key='vn_4', resource_group_key='rg')
    def test_managed_network(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myManagedNetwork': self.create_random_name(prefix='managed_networks'[:8], length=16),
            'subscriptionCAssignment': self.create_random_name(prefix='scope_assignments'[:8], length=17),
            'myManagedNetworkGroup1': self.create_random_name(prefix='managed_network_groups'[:11], length=22),
            'myHubAndSpoke': self.create_random_name(prefix='managed_network_peering_policies'[:16], length=32),
        })

        call_scenario(self, rg)
        raise_if()
