# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def managed_network_managed_networks_list(cmd, client,
                                          resource_group_name=None,
                                          top=None,
                                          skiptoken=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name, top=top, skiptoken=skiptoken)
    return client.list_by_subscription(top=top, skiptoken=skiptoken)


def managed_network_managed_networks_show(cmd, client,
                                          resource_group_name,
                                          managed_network_name):
    return client.get(resource_group_name=resource_group_name, managed_network_name=managed_network_name)


def managed_network_managed_networks_create(cmd, client,
                                            resource_group_name,
                                            managed_network_name,
                                            location=None,
                                            tags=None,
                                            scope_management_groups=None,
                                            scope_subscriptions=None,
                                            scope_virtual_networks=None,
                                            scope_subnets=None):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, location=location, tags=tags, management_groups=scope_management_groups, subscriptions=scope_subscriptions, virtual_networks=scope_virtual_networks, subnets=scope_subnets)


def managed_network_managed_networks_update(cmd, client,
                                            resource_group_name,
                                            managed_network_name,
                                            tags=None):
    return client.update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, tags=tags)


def managed_network_managed_networks_delete(cmd, client,
                                            resource_group_name,
                                            managed_network_name):
    return client.delete(resource_group_name=resource_group_name, managed_network_name=managed_network_name)


def managed_network_scope_assignments_list(cmd, client,
                                           scope):
    return client.list(scope=scope)


def managed_network_scope_assignments_show(cmd, client,
                                           scope,
                                           scope_assignment_name):
    return client.get(scope=scope, scope_assignment_name=scope_assignment_name)


def managed_network_scope_assignments_create(cmd, client,
                                             scope,
                                             scope_assignment_name,
                                             location=None,
                                             assigned_managed_network=None):
    return client.create_or_update(scope=scope, scope_assignment_name=scope_assignment_name, location=location, assigned_managed_network=assigned_managed_network)


def managed_network_scope_assignments_update(cmd, client,
                                             scope,
                                             scope_assignment_name,
                                             location=None,
                                             assigned_managed_network=None):
    return client.create_or_update(scope=scope, scope_assignment_name=scope_assignment_name, location=location, assigned_managed_network=assigned_managed_network)


def managed_network_scope_assignments_delete(cmd, client,
                                             scope,
                                             scope_assignment_name):
    return client.delete(scope=scope, scope_assignment_name=scope_assignment_name)


def managed_network_managed_network_groups_list(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                top=None,
                                                skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name, managed_network_name=managed_network_name, top=top, skiptoken=skiptoken)


def managed_network_managed_network_groups_show(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                managed_network_group_name):
    return client.get(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name)


def managed_network_managed_network_groups_create(cmd, client,
                                                  resource_group_name,
                                                  managed_network_name,
                                                  managed_network_group_name,
                                                  location=None,
                                                  management_groups=None,
                                                  subscriptions=None,
                                                  virtual_networks=None,
                                                  subnets=None):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name, location=location, management_groups=management_groups, subscriptions=subscriptions, virtual_networks=virtual_networks, subnets=subnets)


def managed_network_managed_network_groups_update(cmd, client,
                                                  resource_group_name,
                                                  managed_network_name,
                                                  managed_network_group_name,
                                                  location=None,
                                                  management_groups=None,
                                                  subscriptions=None,
                                                  virtual_networks=None,
                                                  subnets=None):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name, location=location, management_groups=management_groups, subscriptions=subscriptions, virtual_networks=virtual_networks, subnets=subnets)


def managed_network_managed_network_groups_delete(cmd, client,
                                                  resource_group_name,
                                                  managed_network_name,
                                                  managed_network_group_name):
    return client.delete(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name)


def managed_network_managed_network_peering_policies_list(cmd, client,
                                                          resource_group_name,
                                                          managed_network_name,
                                                          top=None,
                                                          skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name, managed_network_name=managed_network_name, top=top, skiptoken=skiptoken)


def managed_network_managed_network_peering_policies_show(cmd, client,
                                                          resource_group_name,
                                                          managed_network_name,
                                                          managed_network_peering_policy_name):
    return client.get(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name)


def managed_network_managed_network_peering_policies_create(cmd, client,
                                                            resource_group_name,
                                                            managed_network_name,
                                                            managed_network_peering_policy_name,
                                                            properties_type,
                                                            location=None,
                                                            id=None,
                                                            properties_spokes=None,
                                                            properties_mesh=None):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name, location=location, type=properties_type, id=id, spokes=properties_spokes, mesh=properties_mesh)


def managed_network_managed_network_peering_policies_update(cmd, client,
                                                            resource_group_name,
                                                            managed_network_name,
                                                            managed_network_peering_policy_name,
                                                            properties_type,
                                                            location=None,
                                                            id=None,
                                                            properties_spokes=None,
                                                            properties_mesh=None):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name, location=location, type=properties_type, id=id, spokes=properties_spokes, mesh=properties_mesh)


def managed_network_managed_network_peering_policies_delete(cmd, client,
                                                            resource_group_name,
                                                            managed_network_name,
                                                            managed_network_peering_policy_name):
    return client.delete(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name)


def managed_network_operations_list(cmd, client):
    return client.list()