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

class InlineResponse20028(object):
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
        'count': 'int',
        'next': 'str',
        'previous': 'str',
        'results': 'list[NetCDFTimeseriesLeakage]'
    }

    attribute_map = {
        'count': 'count',
        'next': 'next',
        'previous': 'previous',
        'results': 'results'
    }

    def __init__(self, count=None, next=None, previous=None, results=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """InlineResponse20028 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._count = None
        self._next = None
        self._previous = None
        self._results = None
        self.discriminator = None

        self.count = count
        self.next = next
        self.previous = previous
        self.results = results

    @property
    def count(self):
        """Gets the count of this InlineResponse20028.  # noqa: E501


        :return: The count of this InlineResponse20028.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineResponse20028.


        :param count: The count of this InlineResponse20028.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def next(self):
        """Gets the next of this InlineResponse20028.  # noqa: E501


        :return: The next of this InlineResponse20028.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this InlineResponse20028.


        :param next: The next of this InlineResponse20028.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this InlineResponse20028.  # noqa: E501


        :return: The previous of this InlineResponse20028.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this InlineResponse20028.


        :param previous: The previous of this InlineResponse20028.  # noqa: E501
        :type: str
        """

        self._previous = previous

    @property
    def results(self):
        """Gets the results of this InlineResponse20028.  # noqa: E501


        :return: The results of this InlineResponse20028.  # noqa: E501
        :rtype: list[NetCDFTimeseriesLeakage]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineResponse20028.


        :param results: The results of this InlineResponse20028.  # noqa: E501
        :type: list[NetCDFTimeseriesLeakage]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, InlineResponse20028):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20028):
            return True

        return self.to_dict() != other.to_dict()
