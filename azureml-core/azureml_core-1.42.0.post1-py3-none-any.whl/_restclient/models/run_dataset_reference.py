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


class RunDatasetReference(Model):
    """A class that references a dataset.

    :param id: The id of the saved dataset.
    :type id: str
    :param name: The name of the registered dataset.
    :type name: str
    :param version: The version of the registered dataset.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, version=None):
        super(RunDatasetReference, self).__init__()
        self.id = id
        self.name = name
        self.version = version
