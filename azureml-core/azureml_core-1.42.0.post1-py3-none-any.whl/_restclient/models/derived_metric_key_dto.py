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


class DerivedMetricKeyDto(Model):
    """DerivedMetricKeyDto.

    :param namespace:
    :type namespace: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'namespace': {'key': 'namespace', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, namespace=None, name=None):
        super(DerivedMetricKeyDto, self).__init__()
        self.namespace = namespace
        self.name = name
