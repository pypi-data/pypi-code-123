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


class WorkspaceConnectionDto(Model):
    """object used for creating workspace connection.

    :param name: Friendly name of the workspace connection
    :type name: str
    :param category: Category of the workspace connection.
    :type category: str
    :param target: Target of the workspace connection.
    :type target: str
    :param auth_type: Authorization type of the workspace connection.
    :type auth_type: str
    :param value: Value details of the workspace connection.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'target': {'key': 'properties.target', 'type': 'str'},
        'auth_type': {'key': 'properties.authType', 'type': 'str'},
        'value': {'key': 'properties.value', 'type': 'str'},
    }

    def __init__(self, name=None, category=None, target=None, auth_type=None, value=None):
        super(WorkspaceConnectionDto, self).__init__()
        self.name = name
        self.category = category
        self.target = target
        self.auth_type = auth_type
        self.value = value
