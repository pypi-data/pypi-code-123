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


class InitialWaterlevel(object):
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
        "threedimodel": "str",
        "file": "FileReadOnly",
        "source_raster": "str",
        "id": "int",
        "source_raster_id": "str",
    }

    attribute_map = {
        "url": "url",
        "threedimodel": "threedimodel",
        "file": "file",
        "source_raster": "source_raster",
        "id": "id",
        "source_raster_id": "source_raster_id",
    }

    def __init__(
        self,
        url=None,
        threedimodel=None,
        file=None,
        source_raster=None,
        id=None,
        source_raster_id=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """InitialWaterlevel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._threedimodel = None
        self._file = None
        self._source_raster = None
        self._id = None
        self._source_raster_id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if threedimodel is not None:
            self.threedimodel = threedimodel
        if file is not None:
            self.file = file
        self.source_raster = source_raster
        if id is not None:
            self.id = id
        if source_raster_id is not None:
            self.source_raster_id = source_raster_id

    @property
    def url(self):
        """Gets the url of this InitialWaterlevel.  # noqa: E501


        :return: The url of this InitialWaterlevel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InitialWaterlevel.


        :param url: The url of this InitialWaterlevel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def threedimodel(self):
        """Gets the threedimodel of this InitialWaterlevel.  # noqa: E501


        :return: The threedimodel of this InitialWaterlevel.  # noqa: E501
        :rtype: str
        """
        return self._threedimodel

    @threedimodel.setter
    def threedimodel(self, threedimodel):
        """Sets the threedimodel of this InitialWaterlevel.


        :param threedimodel: The threedimodel of this InitialWaterlevel.  # noqa: E501
        :type: str
        """

        self._threedimodel = threedimodel

    @property
    def file(self):
        """Gets the file of this InitialWaterlevel.  # noqa: E501


        :return: The file of this InitialWaterlevel.  # noqa: E501
        :rtype: FileReadOnly
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InitialWaterlevel.


        :param file: The file of this InitialWaterlevel.  # noqa: E501
        :type: FileReadOnly
        """

        self._file = file

    @property
    def source_raster(self):
        """Gets the source_raster of this InitialWaterlevel.  # noqa: E501


        :return: The source_raster of this InitialWaterlevel.  # noqa: E501
        :rtype: str
        """
        return self._source_raster

    @source_raster.setter
    def source_raster(self, source_raster):
        """Sets the source_raster of this InitialWaterlevel.


        :param source_raster: The source_raster of this InitialWaterlevel.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and source_raster is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `source_raster`, must not be `None`"
            )  # noqa: E501

        self._source_raster = source_raster

    @property
    def id(self):
        """Gets the id of this InitialWaterlevel.  # noqa: E501


        :return: The id of this InitialWaterlevel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InitialWaterlevel.


        :param id: The id of this InitialWaterlevel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def source_raster_id(self):
        """Gets the source_raster_id of this InitialWaterlevel.  # noqa: E501


        :return: The source_raster_id of this InitialWaterlevel.  # noqa: E501
        :rtype: str
        """
        return self._source_raster_id

    @source_raster_id.setter
    def source_raster_id(self, source_raster_id):
        """Sets the source_raster_id of this InitialWaterlevel.


        :param source_raster_id: The source_raster_id of this InitialWaterlevel.  # noqa: E501
        :type: str
        """

        self._source_raster_id = source_raster_id

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
        if not isinstance(other, InitialWaterlevel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InitialWaterlevel):
            return True

        return self.to_dict() != other.to_dict()
