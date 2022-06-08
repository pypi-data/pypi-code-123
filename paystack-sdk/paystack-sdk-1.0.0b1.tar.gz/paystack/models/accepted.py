# coding: utf-8

"""
    Paystack

    The OpenAPI specification of the Paystack API that merchants and developers can harness to build financial solutions in Africa.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: techsupport@paystack.com
"""


import inspect
import pprint
import re  # noqa: F401
import six

from paystack.configuration import Configuration


class Accepted(object):
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
        'status': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, status=None, message=None, local_vars_configuration=None):  # noqa: E501
        """Accepted - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def status(self):
        """Gets the status of this Accepted.  # noqa: E501


        :return: The status of this Accepted.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Accepted.


        :param status: The status of this Accepted.  # noqa: E501
        :type status: bool
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this Accepted.  # noqa: E501


        :return: The message of this Accepted.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Accepted.


        :param message: The message of this Accepted.  # noqa: E501
        :type message: str
        """

        self._message = message

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
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
        if not isinstance(other, Accepted):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Accepted):
            return True

        return self.to_dict() != other.to_dict()
