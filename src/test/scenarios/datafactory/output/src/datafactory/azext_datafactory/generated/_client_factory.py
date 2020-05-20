# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_datafactory(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.datafactory import DFAZManagementClient
    return get_mgmt_service_client(cli_ctx, DFAZManagementClient)


def cf_factory(cli_ctx, *_):
    return cf_datafactory(cli_ctx).factory


def cf_trigger(cli_ctx, *_):
    return cf_datafactory(cli_ctx).trigger


def cf_integration_runtime(cli_ctx, *_):
    return cf_datafactory(cli_ctx).integration_runtime
