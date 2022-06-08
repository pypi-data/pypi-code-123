# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azureml._vendor.azure_cli_core.decorators import Completer


@Completer
def get_subscription_id_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    from azureml._vendor.azure_cli_core._profile import load_subscriptions

    subscriptions = load_subscriptions(cmd.cli_ctx)
    result = []
    for subscription in subscriptions:
        result.append(subscription['id'])
        result.append(subscription['name'])
    return result
