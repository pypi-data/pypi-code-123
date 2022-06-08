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


class Repository(object):
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
        "url": "str",
        "id": "int",
        "organisation": "str",
        "slug": "str",
        "revision": "list[str]",
    }

    attribute_map = {
        "url": "url",
        "id": "id",
        "organisation": "organisation",
        "slug": "slug",
        "revision": "revision",
    }

    def __init__(
        self,
        url=None,
        id=None,
        organisation=None,
        slug=None,
        revision=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Repository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._id = None
        self._organisation = None
        self._slug = None
        self._revision = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if organisation is not None:
            self.organisation = organisation
        self.slug = slug
        if revision is not None:
            self.revision = revision

    @property
    def url(self):
        """Gets the url of this Repository.  # noqa: E501


        :return: The url of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Repository.


        :param url: The url of this Repository.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this Repository.  # noqa: E501


        :return: The id of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Repository.


        :param id: The id of this Repository.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organisation(self):
        """Gets the organisation of this Repository.  # noqa: E501

        The unique_id of an organisation  # noqa: E501

        :return: The organisation of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this Repository.

        The unique_id of an organisation  # noqa: E501

        :param organisation: The organisation of this Repository.  # noqa: E501
        :type: str
        """

        self._organisation = organisation

    @property
    def slug(self):
        """Gets the slug of this Repository.  # noqa: E501

        do not change  # noqa: E501

        :return: The slug of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Repository.

        do not change  # noqa: E501

        :param slug: The slug of this Repository.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and slug is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `slug`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and slug is not None
            and len(slug) > 255
        ):
            raise ValueError(
                "Invalid value for `slug`, length must be less than or equal to `255`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and slug is not None
            and len(slug) < 1
        ):
            raise ValueError(
                "Invalid value for `slug`, length must be greater than or equal to `1`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and slug is not None
            and not re.search(r"^[-a-zA-Z0-9_]+$", slug)
        ):  # noqa: E501
            raise ValueError(
                r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`"
            )  # noqa: E501

        self._slug = slug

    @property
    def revision(self):
        """Gets the revision of this Repository.  # noqa: E501


        :return: The revision of this Repository.  # noqa: E501
        :rtype: list[str]
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Repository.


        :param revision: The revision of this Repository.  # noqa: E501
        :type: list[str]
        """

        self._revision = revision

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
        if not isinstance(other, Repository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Repository):
            return True

        return self.to_dict() != other.to_dict()
