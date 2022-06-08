# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ServiceServiceSystemMetricsResponse(object):
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
        'containers': 'list[InfluxdbSystemMetricList]',
        'pvcs': 'list[InfluxdbSystemMetricList]'
    }

    attribute_map = {
        'containers': 'containers',
        'pvcs': 'pvcs'
    }

    def __init__(self, containers=None, pvcs=None, local_vars_configuration=None):  # noqa: E501
        """ServiceServiceSystemMetricsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._containers = None
        self._pvcs = None
        self.discriminator = None

        self.containers = containers
        self.pvcs = pvcs

    @property
    def containers(self):
        """Gets the containers of this ServiceServiceSystemMetricsResponse.  # noqa: E501


        :return: The containers of this ServiceServiceSystemMetricsResponse.  # noqa: E501
        :rtype: list[InfluxdbSystemMetricList]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """Sets the containers of this ServiceServiceSystemMetricsResponse.


        :param containers: The containers of this ServiceServiceSystemMetricsResponse.  # noqa: E501
        :type containers: list[InfluxdbSystemMetricList]
        """
        if self.local_vars_configuration.client_side_validation and containers is None:  # noqa: E501
            raise ValueError("Invalid value for `containers`, must not be `None`")  # noqa: E501

        self._containers = containers

    @property
    def pvcs(self):
        """Gets the pvcs of this ServiceServiceSystemMetricsResponse.  # noqa: E501


        :return: The pvcs of this ServiceServiceSystemMetricsResponse.  # noqa: E501
        :rtype: list[InfluxdbSystemMetricList]
        """
        return self._pvcs

    @pvcs.setter
    def pvcs(self, pvcs):
        """Sets the pvcs of this ServiceServiceSystemMetricsResponse.


        :param pvcs: The pvcs of this ServiceServiceSystemMetricsResponse.  # noqa: E501
        :type pvcs: list[InfluxdbSystemMetricList]
        """
        if self.local_vars_configuration.client_side_validation and pvcs is None:  # noqa: E501
            raise ValueError("Invalid value for `pvcs`, must not be `None`")  # noqa: E501

        self._pvcs = pvcs

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceServiceSystemMetricsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceServiceSystemMetricsResponse):
            return True

        return self.to_dict() != other.to_dict()
