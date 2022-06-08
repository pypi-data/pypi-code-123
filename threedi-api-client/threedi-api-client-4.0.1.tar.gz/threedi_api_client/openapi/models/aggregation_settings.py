# coding: utf-8

"""
    3Di API

    3Di simulation API (latest stable version: v3)   Framework release: 2.19.3   3Di core release: 2.2.11  deployed on:  10:31AM (UTC) on June 01, 2022  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import logging
import pprint
import re  # noqa: F401

import six

from threedi_api_client.openapi.configuration import Configuration

logger = logging.getLogger(__name__)

class AggregationSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'name': 'str',
        'flow_variable': 'str',
        'method': 'str',
        'interval': 'float'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'flow_variable': 'flow_variable',
        'method': 'method',
        'interval': 'interval'
    }

    def __init__(self, url=None, name=None, flow_variable=None, method=None, interval=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """AggregationSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._name = None
        self._flow_variable = None
        self._method = None
        self._interval = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.name = name
        self.flow_variable = flow_variable
        self.method = method
        self.interval = interval

    @property
    def url(self):
        """Gets the url of this AggregationSettings.  # noqa: E501


        :return: The url of this AggregationSettings.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AggregationSettings.


        :param url: The url of this AggregationSettings.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this AggregationSettings.  # noqa: E501

        Give your aggregation setting a name to be able to find it back in the results file.  # noqa: E501

        :return: The name of this AggregationSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AggregationSettings.

        Give your aggregation setting a name to be able to find it back in the results file.  # noqa: E501

        :param name: The name of this AggregationSettings.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 120):
            self.__handle_validation_error("Invalid value for `name`, length must be less than or equal to `120`")  # noqa: E501

        self._name = name

    @property
    def flow_variable(self):
        """Gets the flow_variable of this AggregationSettings.  # noqa: E501

        Options:  water_level = Water Level flow_velocity = Flow Velocity discharge = Discharge volume = Volume pump_discharge = Pump Discharge wet_cross_section = Wet Cross Section lateral_discharge = Lateral Discharge wet_surface = Wet Surface rain = Rain simple_infiltration = Simple Infiltration leakage = Leakage interception = Interception surface_source_sink_discharge = Surface Source Sink Discharge   # noqa: E501

        :return: The flow_variable of this AggregationSettings.  # noqa: E501
        :rtype: str
        """
        return self._flow_variable

    @flow_variable.setter
    def flow_variable(self, flow_variable):
        """Sets the flow_variable of this AggregationSettings.

        Options:  water_level = Water Level flow_velocity = Flow Velocity discharge = Discharge volume = Volume pump_discharge = Pump Discharge wet_cross_section = Wet Cross Section lateral_discharge = Lateral Discharge wet_surface = Wet Surface rain = Rain simple_infiltration = Simple Infiltration leakage = Leakage interception = Interception surface_source_sink_discharge = Surface Source Sink Discharge   # noqa: E501

        :param flow_variable: The flow_variable of this AggregationSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and flow_variable is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `flow_variable`, must not be `None`")  # noqa: E501
        allowed_values = ["water_level", "flow_velocity", "discharge", "volume", "pump_discharge", "wet_cross_section", "lateral_discharge", "wet_surface", "rain", "simple_infiltration", "leakage", "interception", "surface_source_sink_discharge"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and flow_variable not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `flow_variable` ({0}), must be one of {1}"  # noqa: E501
                .format(flow_variable, allowed_values)
            )

        self._flow_variable = flow_variable

    @property
    def method(self):
        """Gets the method of this AggregationSettings.  # noqa: E501

        Options:  min = minimum value of the variable in the configured interval max = maximum value of the variable in the configured interval avg = average value of the variable in the configured interval cum = variable integration over time [dt * variable] cum_positive = variable integration over time [dt * variable] in positive direction cum_negative = variable integration over time [dt * variable] in negative direction current = current value of a variable sum = variable summation over configured interval  Note: 'current' is required in case one checks the water balance for variables that are the result of the processes. Only valid for flow_variable 'volume' and 'intercepted_volume'  # noqa: E501

        :return: The method of this AggregationSettings.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AggregationSettings.

        Options:  min = minimum value of the variable in the configured interval max = maximum value of the variable in the configured interval avg = average value of the variable in the configured interval cum = variable integration over time [dt * variable] cum_positive = variable integration over time [dt * variable] in positive direction cum_negative = variable integration over time [dt * variable] in negative direction current = current value of a variable sum = variable summation over configured interval  Note: 'current' is required in case one checks the water balance for variables that are the result of the processes. Only valid for flow_variable 'volume' and 'intercepted_volume'  # noqa: E501

        :param method: The method of this AggregationSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `method`, must not be `None`")  # noqa: E501
        allowed_values = ["min", "max", "avg", "cum", "cum_positive", "cum_negative", "current", "sum"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            self.__handle_validation_error(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def interval(self):
        """Gets the interval of this AggregationSettings.  # noqa: E501

        aggregation interval in seconds  # noqa: E501

        :return: The interval of this AggregationSettings.  # noqa: E501
        :rtype: float
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this AggregationSettings.

        aggregation interval in seconds  # noqa: E501

        :param interval: The interval of this AggregationSettings.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and interval is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def __handle_validation_error(self, message):
        # Only raise ValueError when not fetched from API
        from threedi_api_client import __version__ as VERSION

        if not self._fetched_from_api:
            raise ValueError(message + f" It is possible that the current threedi-api-client version ({VERSION}) is out of date: consult https://pypi.org/project/threedi-api-client/ and consider upgrading.")  # noqa: E501
        logger.warning(message + " Please update to the latest threedi-api-client version.")  # noqa: E501

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AggregationSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregationSettings):
            return True

        return self.to_dict() != other.to_dict()
