# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegistryIdentity(Model):
    """RegistryIdentity.

    :param resource_id:
    :type resource_id: str
    :param client_id:
    :type client_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, resource_id=None, client_id=None):
        super(RegistryIdentity, self).__init__()
        self.resource_id = resource_id
        self.client_id = client_id
