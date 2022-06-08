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


class ManyModelsRunValidationInput(Model):
    """ManyModelsRunValidationInput.

    :param version:
    :type version: int
    :param max_concurrent_runs:
    :type max_concurrent_runs: int
    :param max_severity:
    :type max_severity: int
    :param auto_ml_settings:
    :type auto_ml_settings: str
    :param number_of_processes_per_core:
    :type number_of_processes_per_core: int
    """

    _attribute_map = {
        'version': {'key': 'version', 'type': 'int'},
        'max_concurrent_runs': {'key': 'maxConcurrentRuns', 'type': 'int'},
        'max_severity': {'key': 'maxSeverity', 'type': 'int'},
        'auto_ml_settings': {'key': 'autoMLSettings', 'type': 'str'},
        'number_of_processes_per_core': {'key': 'numberOfProcessesPerCore', 'type': 'int'},
    }

    def __init__(self, version=None, max_concurrent_runs=None, max_severity=None, auto_ml_settings=None, number_of_processes_per_core=None):
        super(ManyModelsRunValidationInput, self).__init__()
        self.version = version
        self.max_concurrent_runs = max_concurrent_runs
        self.max_severity = max_severity
        self.auto_ml_settings = auto_ml_settings
        self.number_of_processes_per_core = number_of_processes_per_core
