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


class VerificationBVNMatch(object):
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
        'account_number': 'str',
        'bank_code': 'int',
        'bvn': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'account_number': 'account_number',
        'bank_code': 'bank_code',
        'bvn': 'bvn',
        'first_name': 'first_name',
        'middle_name': 'middle_name',
        'last_name': 'last_name'
    }

    def __init__(self, account_number=None, bank_code=None, bvn=None, first_name=None, middle_name=None, last_name=None, local_vars_configuration=None):  # noqa: E501
        """VerificationBVNMatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._account_number = None
        self._bank_code = None
        self._bvn = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self.discriminator = None

        self.account_number = account_number
        self.bank_code = bank_code
        self.bvn = bvn
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name

    @property
    def account_number(self):
        """Gets the account_number of this VerificationBVNMatch.  # noqa: E501

        Bank Account Number  # noqa: E501

        :return: The account_number of this VerificationBVNMatch.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this VerificationBVNMatch.

        Bank Account Number  # noqa: E501

        :param account_number: The account_number of this VerificationBVNMatch.  # noqa: E501
        :type account_number: str
        """
        if self.local_vars_configuration.client_side_validation and account_number is None:  # noqa: E501
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def bank_code(self):
        """Gets the bank_code of this VerificationBVNMatch.  # noqa: E501

        You can get the list of banks codes by calling the List Bank endpoint  # noqa: E501

        :return: The bank_code of this VerificationBVNMatch.  # noqa: E501
        :rtype: int
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this VerificationBVNMatch.

        You can get the list of banks codes by calling the List Bank endpoint  # noqa: E501

        :param bank_code: The bank_code of this VerificationBVNMatch.  # noqa: E501
        :type bank_code: int
        """
        if self.local_vars_configuration.client_side_validation and bank_code is None:  # noqa: E501
            raise ValueError("Invalid value for `bank_code`, must not be `None`")  # noqa: E501

        self._bank_code = bank_code

    @property
    def bvn(self):
        """Gets the bvn of this VerificationBVNMatch.  # noqa: E501

        11 digits Bank Verification Number  # noqa: E501

        :return: The bvn of this VerificationBVNMatch.  # noqa: E501
        :rtype: str
        """
        return self._bvn

    @bvn.setter
    def bvn(self, bvn):
        """Sets the bvn of this VerificationBVNMatch.

        11 digits Bank Verification Number  # noqa: E501

        :param bvn: The bvn of this VerificationBVNMatch.  # noqa: E501
        :type bvn: str
        """
        if self.local_vars_configuration.client_side_validation and bvn is None:  # noqa: E501
            raise ValueError("Invalid value for `bvn`, must not be `None`")  # noqa: E501

        self._bvn = bvn

    @property
    def first_name(self):
        """Gets the first_name of this VerificationBVNMatch.  # noqa: E501

        Customer's first name  # noqa: E501

        :return: The first_name of this VerificationBVNMatch.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this VerificationBVNMatch.

        Customer's first name  # noqa: E501

        :param first_name: The first_name of this VerificationBVNMatch.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this VerificationBVNMatch.  # noqa: E501

        Customer's middle name  # noqa: E501

        :return: The middle_name of this VerificationBVNMatch.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this VerificationBVNMatch.

        Customer's middle name  # noqa: E501

        :param middle_name: The middle_name of this VerificationBVNMatch.  # noqa: E501
        :type middle_name: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this VerificationBVNMatch.  # noqa: E501

        Customer's last name  # noqa: E501

        :return: The last_name of this VerificationBVNMatch.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this VerificationBVNMatch.

        Customer's last name  # noqa: E501

        :param last_name: The last_name of this VerificationBVNMatch.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

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
        if not isinstance(other, VerificationBVNMatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerificationBVNMatch):
            return True

        return self.to_dict() != other.to_dict()
