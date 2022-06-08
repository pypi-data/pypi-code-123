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


class TargetLags(Model):
    """TargetLags.

    :param mode: Possible values include: 'Off', 'Auto', 'Custom'
    :type mode: str or ~_restclient.models.TargetLagsMode
    :param lags:
    :type lags: list[int]
    """

    _attribute_map = {
        'mode': {'key': 'mode', 'type': 'TargetLagsMode'},
        'lags': {'key': 'lags', 'type': '[int]'},
    }

    def __init__(self, mode=None, lags=None):
        super(TargetLags, self).__init__()
        self.mode = mode
        self.lags = lags
