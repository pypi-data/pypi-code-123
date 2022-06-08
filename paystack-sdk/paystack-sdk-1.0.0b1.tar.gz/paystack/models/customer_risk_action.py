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


class CustomerRiskAction(object):
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
        'customer': 'str',
        'risk_action': 'str'
    }

    attribute_map = {
        'customer': 'customer',
        'risk_action': 'risk_action'
    }

    def __init__(self, customer=None, risk_action=None, local_vars_configuration=None):  # noqa: E501
        """CustomerRiskAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._customer = None
        self._risk_action = None
        self.discriminator = None

        self.customer = customer
        if risk_action is not None:
            self.risk_action = risk_action

    @property
    def customer(self):
        """Gets the customer of this CustomerRiskAction.  # noqa: E501

        Customer's code, or email address  # noqa: E501

        :return: The customer of this CustomerRiskAction.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerRiskAction.

        Customer's code, or email address  # noqa: E501

        :param customer: The customer of this CustomerRiskAction.  # noqa: E501
        :type customer: str
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def risk_action(self):
        """Gets the risk_action of this CustomerRiskAction.  # noqa: E501

        One of the possible risk actions [ default, allow, deny ]. allow to whitelist.  deny to blacklist. Customers start with a default risk action.   # noqa: E501

        :return: The risk_action of this CustomerRiskAction.  # noqa: E501
        :rtype: str
        """
        return self._risk_action

    @risk_action.setter
    def risk_action(self, risk_action):
        """Sets the risk_action of this CustomerRiskAction.

        One of the possible risk actions [ default, allow, deny ]. allow to whitelist.  deny to blacklist. Customers start with a default risk action.   # noqa: E501

        :param risk_action: The risk_action of this CustomerRiskAction.  # noqa: E501
        :type risk_action: str
        """

        self._risk_action = risk_action

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
        if not isinstance(other, CustomerRiskAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerRiskAction):
            return True

        return self.to_dict() != other.to_dict()
