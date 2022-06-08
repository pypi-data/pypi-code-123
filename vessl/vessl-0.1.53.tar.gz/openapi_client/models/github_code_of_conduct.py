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


class GithubCodeOfConduct(object):
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
        'body': 'str',
        'key': 'str',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'body': 'body',
        'key': 'key',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, body=None, key=None, name=None, url=None, local_vars_configuration=None):  # noqa: E501
        """GithubCodeOfConduct - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self._key = None
        self._name = None
        self._url = None
        self.discriminator = None

        self.body = body
        self.key = key
        self.name = name
        self.url = url

    @property
    def body(self):
        """Gets the body of this GithubCodeOfConduct.  # noqa: E501


        :return: The body of this GithubCodeOfConduct.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this GithubCodeOfConduct.


        :param body: The body of this GithubCodeOfConduct.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def key(self):
        """Gets the key of this GithubCodeOfConduct.  # noqa: E501


        :return: The key of this GithubCodeOfConduct.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GithubCodeOfConduct.


        :param key: The key of this GithubCodeOfConduct.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this GithubCodeOfConduct.  # noqa: E501


        :return: The name of this GithubCodeOfConduct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GithubCodeOfConduct.


        :param name: The name of this GithubCodeOfConduct.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this GithubCodeOfConduct.  # noqa: E501


        :return: The url of this GithubCodeOfConduct.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GithubCodeOfConduct.


        :param url: The url of this GithubCodeOfConduct.  # noqa: E501
        :type url: str
        """

        self._url = url

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
        if not isinstance(other, GithubCodeOfConduct):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GithubCodeOfConduct):
            return True

        return self.to_dict() != other.to_dict()
