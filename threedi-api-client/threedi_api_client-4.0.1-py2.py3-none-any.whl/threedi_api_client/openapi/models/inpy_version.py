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

class InpyVersion(object):
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
        'threedi_version': 'str',
        'threedicore_version': 'str',
        'slug': 'str',
        'id': 'int',
        'active': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'threedi_version': 'threedi_version',
        'threedicore_version': 'threedicore_version',
        'slug': 'slug',
        'id': 'id',
        'active': 'active'
    }

    def __init__(self, url=None, threedi_version=None, threedicore_version=None, slug=None, id=None, active=None, local_vars_configuration=None, fetched_from_api=False):  # noqa: E501
        """InpyVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        # True if data is coming from API
        self._fetched_from_api = fetched_from_api

        self._url = None
        self._threedi_version = None
        self._threedicore_version = None
        self._slug = None
        self._id = None
        self._active = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.threedi_version = threedi_version
        self.threedicore_version = threedicore_version
        if slug is not None:
            self.slug = slug
        if id is not None:
            self.id = id
        if active is not None:
            self.active = active

    @property
    def url(self):
        """Gets the url of this InpyVersion.  # noqa: E501


        :return: The url of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InpyVersion.


        :param url: The url of this InpyVersion.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def threedi_version(self):
        """Gets the threedi_version of this InpyVersion.  # noqa: E501


        :return: The threedi_version of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._threedi_version

    @threedi_version.setter
    def threedi_version(self, threedi_version):
        """Sets the threedi_version of this InpyVersion.


        :param threedi_version: The threedi_version of this InpyVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and threedi_version is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `threedi_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threedi_version is not None and len(threedi_version) > 80):
            self.__handle_validation_error("Invalid value for `threedi_version`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threedi_version is not None and len(threedi_version) < 1):
            self.__handle_validation_error("Invalid value for `threedi_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._threedi_version = threedi_version

    @property
    def threedicore_version(self):
        """Gets the threedicore_version of this InpyVersion.  # noqa: E501


        :return: The threedicore_version of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._threedicore_version

    @threedicore_version.setter
    def threedicore_version(self, threedicore_version):
        """Sets the threedicore_version of this InpyVersion.


        :param threedicore_version: The threedicore_version of this InpyVersion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and threedicore_version is None:  # noqa: E501
            self.__handle_validation_error("Invalid value for `threedicore_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threedicore_version is not None and len(threedicore_version) > 80):
            self.__handle_validation_error("Invalid value for `threedicore_version`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threedicore_version is not None and len(threedicore_version) < 1):
            self.__handle_validation_error("Invalid value for `threedicore_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._threedicore_version = threedicore_version

    @property
    def slug(self):
        """Gets the slug of this InpyVersion.  # noqa: E501


        :return: The slug of this InpyVersion.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this InpyVersion.


        :param slug: The slug of this InpyVersion.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                slug is not None and len(slug) < 1):
            self.__handle_validation_error("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501

        self._slug = slug

    @property
    def id(self):
        """Gets the id of this InpyVersion.  # noqa: E501


        :return: The id of this InpyVersion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InpyVersion.


        :param id: The id of this InpyVersion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this InpyVersion.  # noqa: E501


        :return: The active of this InpyVersion.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InpyVersion.


        :param active: The active of this InpyVersion.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if not isinstance(other, InpyVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InpyVersion):
            return True

        return self.to_dict() != other.to_dict()
