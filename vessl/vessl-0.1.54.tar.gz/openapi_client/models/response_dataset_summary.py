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


class ResponseDatasetSummary(object):
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
        'created_dt': 'datetime',
        'summary': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'summary': 'summary',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_dt=None, summary=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ResponseDatasetSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._summary = None
        self._updated_dt = None
        self.discriminator = None

        self.created_dt = created_dt
        self.summary = summary
        self.updated_dt = updated_dt

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseDatasetSummary.  # noqa: E501


        :return: The created_dt of this ResponseDatasetSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseDatasetSummary.


        :param created_dt: The created_dt of this ResponseDatasetSummary.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def summary(self):
        """Gets the summary of this ResponseDatasetSummary.  # noqa: E501


        :return: The summary of this ResponseDatasetSummary.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ResponseDatasetSummary.


        :param summary: The summary of this ResponseDatasetSummary.  # noqa: E501
        :type summary: str
        """
        if self.local_vars_configuration.client_side_validation and summary is None:  # noqa: E501
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseDatasetSummary.  # noqa: E501


        :return: The updated_dt of this ResponseDatasetSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseDatasetSummary.


        :param updated_dt: The updated_dt of this ResponseDatasetSummary.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

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
        if not isinstance(other, ResponseDatasetSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseDatasetSummary):
            return True

        return self.to_dict() != other.to_dict()
