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


class ComputeRequest(Model):
    """ComputeRequest.

    :param node_count:
    :type node_count: int
    """

    _attribute_map = {
        'node_count': {'key': 'nodeCount', 'type': 'int'},
    }

    def __init__(self, node_count=None):
        super(ComputeRequest, self).__init__()
        self.node_count = node_count
