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


class PrivateLinkServiceConnectionState(Model):
    """A collection of information about the state of the connection between
    service consumer and provider.

    :param status: Indicates whether the connection has been
     Approved/Rejected/Removed by the owner of the service. Possible values
     include: 'Pending', 'Approved', 'Rejected', 'Disconnected', 'Timeout'
    :type status: str or
     ~_restclient.models.PrivateEndpointServiceConnectionStatus
    :param description: The reason for approval/rejection of the connection.
    :type description: str
    :param actions_required: A message indicating if changes on the service
     provider require any updates on the consumer.
    :type actions_required: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'actions_required': {'key': 'actionsRequired', 'type': 'str'},
    }

    def __init__(self, status=None, description=None, actions_required=None):
        super(PrivateLinkServiceConnectionState, self).__init__()
        self.status = status
        self.description = description
        self.actions_required = actions_required
