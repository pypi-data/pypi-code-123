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


class ResourceSkuZoneDetails(Model):
    """Describes The zonal capabilities of a SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The set of zones that the SKU is available in with the
     specified capabilities.
    :vartype name: list[str]
    :ivar capabilities: A list of capabilities that are available for the SKU
     in the specified list of zones.
    :vartype capabilities: list[~_restclient.models.SKUCapability]
    """

    _validation = {
        'name': {'readonly': True},
        'capabilities': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': '[str]'},
        'capabilities': {'key': 'capabilities', 'type': '[SKUCapability]'},
    }

    def __init__(self):
        super(ResourceSkuZoneDetails, self).__init__()
        self.name = None
        self.capabilities = None
