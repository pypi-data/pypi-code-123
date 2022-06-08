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


class SignUpAPIInput(object):
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
        'email': 'str',
        'name': 'str',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'email': 'email',
        'name': 'name',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, email=None, name=None, password=None, username=None, local_vars_configuration=None):  # noqa: E501
        """SignUpAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._name = None
        self._password = None
        self._username = None
        self.discriminator = None

        self.email = email
        self.name = name
        self.password = password
        self.username = username

    @property
    def email(self):
        """Gets the email of this SignUpAPIInput.  # noqa: E501


        :return: The email of this SignUpAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SignUpAPIInput.


        :param email: The email of this SignUpAPIInput.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 255):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this SignUpAPIInput.  # noqa: E501


        :return: The name of this SignUpAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SignUpAPIInput.


        :param name: The name of this SignUpAPIInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this SignUpAPIInput.  # noqa: E501


        :return: The password of this SignUpAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SignUpAPIInput.


        :param password: The password of this SignUpAPIInput.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) > 255):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 8):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `8`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this SignUpAPIInput.  # noqa: E501


        :return: The username of this SignUpAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SignUpAPIInput.


        :param username: The username of this SignUpAPIInput.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 255):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, SignUpAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignUpAPIInput):
            return True

        return self.to_dict() != other.to_dict()
