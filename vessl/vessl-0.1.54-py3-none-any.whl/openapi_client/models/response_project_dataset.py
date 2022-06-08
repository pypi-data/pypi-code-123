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


class ResponseProjectDataset(object):
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
        'dataset': 'ResponseDatasetInfo',
        'id': 'int',
        'mount_path': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'id': 'id',
        'mount_path': 'mount_path'
    }

    def __init__(self, dataset=None, id=None, mount_path=None, local_vars_configuration=None):  # noqa: E501
        """ResponseProjectDataset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dataset = None
        self._id = None
        self._mount_path = None
        self.discriminator = None

        self.dataset = dataset
        self.id = id
        self.mount_path = mount_path

    @property
    def dataset(self):
        """Gets the dataset of this ResponseProjectDataset.  # noqa: E501


        :return: The dataset of this ResponseProjectDataset.  # noqa: E501
        :rtype: ResponseDatasetInfo
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this ResponseProjectDataset.


        :param dataset: The dataset of this ResponseProjectDataset.  # noqa: E501
        :type dataset: ResponseDatasetInfo
        """
        if self.local_vars_configuration.client_side_validation and dataset is None:  # noqa: E501
            raise ValueError("Invalid value for `dataset`, must not be `None`")  # noqa: E501

        self._dataset = dataset

    @property
    def id(self):
        """Gets the id of this ResponseProjectDataset.  # noqa: E501


        :return: The id of this ResponseProjectDataset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseProjectDataset.


        :param id: The id of this ResponseProjectDataset.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def mount_path(self):
        """Gets the mount_path of this ResponseProjectDataset.  # noqa: E501


        :return: The mount_path of this ResponseProjectDataset.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this ResponseProjectDataset.


        :param mount_path: The mount_path of this ResponseProjectDataset.  # noqa: E501
        :type mount_path: str
        """
        if self.local_vars_configuration.client_side_validation and mount_path is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_path`, must not be `None`")  # noqa: E501

        self._mount_path = mount_path

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
        if not isinstance(other, ResponseProjectDataset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseProjectDataset):
            return True

        return self.to_dict() != other.to_dict()
