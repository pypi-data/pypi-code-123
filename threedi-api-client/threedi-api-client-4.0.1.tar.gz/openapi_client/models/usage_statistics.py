# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.16   3Di core release: 2.0.11  deployed on:  07:33AM (UTC) on September 04, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class UsageStatistics(object):
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
        "total_sessions": "int",
        "total_duration": "int",
        "avg_duration": "float",
        "min_duration": "int",
        "max_duration": "int",
        "duration_humanized": "str",
    }

    attribute_map = {
        "total_sessions": "total_sessions",
        "total_duration": "total_duration",
        "avg_duration": "avg_duration",
        "min_duration": "min_duration",
        "max_duration": "max_duration",
        "duration_humanized": "duration_humanized",
    }

    def __init__(
        self,
        total_sessions=None,
        total_duration=None,
        avg_duration=None,
        min_duration=None,
        max_duration=None,
        duration_humanized=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """UsageStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_sessions = None
        self._total_duration = None
        self._avg_duration = None
        self._min_duration = None
        self._max_duration = None
        self._duration_humanized = None
        self.discriminator = None

        self.total_sessions = total_sessions
        self.total_duration = total_duration
        self.avg_duration = avg_duration
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.duration_humanized = duration_humanized

    @property
    def total_sessions(self):
        """Gets the total_sessions of this UsageStatistics.  # noqa: E501


        :return: The total_sessions of this UsageStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_sessions

    @total_sessions.setter
    def total_sessions(self, total_sessions):
        """Sets the total_sessions of this UsageStatistics.


        :param total_sessions: The total_sessions of this UsageStatistics.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and total_sessions is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `total_sessions`, must not be `None`"
            )  # noqa: E501

        self._total_sessions = total_sessions

    @property
    def total_duration(self):
        """Gets the total_duration of this UsageStatistics.  # noqa: E501


        :return: The total_duration of this UsageStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_duration

    @total_duration.setter
    def total_duration(self, total_duration):
        """Sets the total_duration of this UsageStatistics.


        :param total_duration: The total_duration of this UsageStatistics.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and total_duration is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `total_duration`, must not be `None`"
            )  # noqa: E501

        self._total_duration = total_duration

    @property
    def avg_duration(self):
        """Gets the avg_duration of this UsageStatistics.  # noqa: E501


        :return: The avg_duration of this UsageStatistics.  # noqa: E501
        :rtype: float
        """
        return self._avg_duration

    @avg_duration.setter
    def avg_duration(self, avg_duration):
        """Sets the avg_duration of this UsageStatistics.


        :param avg_duration: The avg_duration of this UsageStatistics.  # noqa: E501
        :type: float
        """
        if (
            self.local_vars_configuration.client_side_validation
            and avg_duration is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `avg_duration`, must not be `None`"
            )  # noqa: E501

        self._avg_duration = avg_duration

    @property
    def min_duration(self):
        """Gets the min_duration of this UsageStatistics.  # noqa: E501


        :return: The min_duration of this UsageStatistics.  # noqa: E501
        :rtype: int
        """
        return self._min_duration

    @min_duration.setter
    def min_duration(self, min_duration):
        """Sets the min_duration of this UsageStatistics.


        :param min_duration: The min_duration of this UsageStatistics.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and min_duration is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `min_duration`, must not be `None`"
            )  # noqa: E501

        self._min_duration = min_duration

    @property
    def max_duration(self):
        """Gets the max_duration of this UsageStatistics.  # noqa: E501


        :return: The max_duration of this UsageStatistics.  # noqa: E501
        :rtype: int
        """
        return self._max_duration

    @max_duration.setter
    def max_duration(self, max_duration):
        """Sets the max_duration of this UsageStatistics.


        :param max_duration: The max_duration of this UsageStatistics.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and max_duration is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `max_duration`, must not be `None`"
            )  # noqa: E501

        self._max_duration = max_duration

    @property
    def duration_humanized(self):
        """Gets the duration_humanized of this UsageStatistics.  # noqa: E501


        :return: The duration_humanized of this UsageStatistics.  # noqa: E501
        :rtype: str
        """
        return self._duration_humanized

    @duration_humanized.setter
    def duration_humanized(self, duration_humanized):
        """Sets the duration_humanized of this UsageStatistics.


        :param duration_humanized: The duration_humanized of this UsageStatistics.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and duration_humanized is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `duration_humanized`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and duration_humanized is not None
            and len(duration_humanized) < 1
        ):
            raise ValueError(
                "Invalid value for `duration_humanized`, length must be greater than or equal to `1`"
            )  # noqa: E501

        self._duration_humanized = duration_humanized

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UsageStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsageStatistics):
            return True

        return self.to_dict() != other.to_dict()
