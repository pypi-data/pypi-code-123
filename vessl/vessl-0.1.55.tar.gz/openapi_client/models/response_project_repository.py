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


class ResponseProjectRepository(object):
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
        'git_default_branch': 'str',
        'git_owner': 'str',
        'git_provider': 'str',
        'git_repo': 'str',
        'id': 'int',
        'is_connected': 'bool',
        'organization_credentials_id': 'int'
    }

    attribute_map = {
        'git_default_branch': 'git_default_branch',
        'git_owner': 'git_owner',
        'git_provider': 'git_provider',
        'git_repo': 'git_repo',
        'id': 'id',
        'is_connected': 'is_connected',
        'organization_credentials_id': 'organization_credentials_id'
    }

    def __init__(self, git_default_branch=None, git_owner=None, git_provider=None, git_repo=None, id=None, is_connected=None, organization_credentials_id=None, local_vars_configuration=None):  # noqa: E501
        """ResponseProjectRepository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._git_default_branch = None
        self._git_owner = None
        self._git_provider = None
        self._git_repo = None
        self._id = None
        self._is_connected = None
        self._organization_credentials_id = None
        self.discriminator = None

        self.git_default_branch = git_default_branch
        self.git_owner = git_owner
        self.git_provider = git_provider
        self.git_repo = git_repo
        self.id = id
        self.is_connected = is_connected
        self.organization_credentials_id = organization_credentials_id

    @property
    def git_default_branch(self):
        """Gets the git_default_branch of this ResponseProjectRepository.  # noqa: E501


        :return: The git_default_branch of this ResponseProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_default_branch

    @git_default_branch.setter
    def git_default_branch(self, git_default_branch):
        """Sets the git_default_branch of this ResponseProjectRepository.


        :param git_default_branch: The git_default_branch of this ResponseProjectRepository.  # noqa: E501
        :type git_default_branch: str
        """
        if self.local_vars_configuration.client_side_validation and git_default_branch is None:  # noqa: E501
            raise ValueError("Invalid value for `git_default_branch`, must not be `None`")  # noqa: E501

        self._git_default_branch = git_default_branch

    @property
    def git_owner(self):
        """Gets the git_owner of this ResponseProjectRepository.  # noqa: E501


        :return: The git_owner of this ResponseProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_owner

    @git_owner.setter
    def git_owner(self, git_owner):
        """Sets the git_owner of this ResponseProjectRepository.


        :param git_owner: The git_owner of this ResponseProjectRepository.  # noqa: E501
        :type git_owner: str
        """
        if self.local_vars_configuration.client_side_validation and git_owner is None:  # noqa: E501
            raise ValueError("Invalid value for `git_owner`, must not be `None`")  # noqa: E501

        self._git_owner = git_owner

    @property
    def git_provider(self):
        """Gets the git_provider of this ResponseProjectRepository.  # noqa: E501


        :return: The git_provider of this ResponseProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_provider

    @git_provider.setter
    def git_provider(self, git_provider):
        """Sets the git_provider of this ResponseProjectRepository.


        :param git_provider: The git_provider of this ResponseProjectRepository.  # noqa: E501
        :type git_provider: str
        """
        if self.local_vars_configuration.client_side_validation and git_provider is None:  # noqa: E501
            raise ValueError("Invalid value for `git_provider`, must not be `None`")  # noqa: E501

        self._git_provider = git_provider

    @property
    def git_repo(self):
        """Gets the git_repo of this ResponseProjectRepository.  # noqa: E501


        :return: The git_repo of this ResponseProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_repo

    @git_repo.setter
    def git_repo(self, git_repo):
        """Sets the git_repo of this ResponseProjectRepository.


        :param git_repo: The git_repo of this ResponseProjectRepository.  # noqa: E501
        :type git_repo: str
        """
        if self.local_vars_configuration.client_side_validation and git_repo is None:  # noqa: E501
            raise ValueError("Invalid value for `git_repo`, must not be `None`")  # noqa: E501

        self._git_repo = git_repo

    @property
    def id(self):
        """Gets the id of this ResponseProjectRepository.  # noqa: E501


        :return: The id of this ResponseProjectRepository.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseProjectRepository.


        :param id: The id of this ResponseProjectRepository.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_connected(self):
        """Gets the is_connected of this ResponseProjectRepository.  # noqa: E501


        :return: The is_connected of this ResponseProjectRepository.  # noqa: E501
        :rtype: bool
        """
        return self._is_connected

    @is_connected.setter
    def is_connected(self, is_connected):
        """Sets the is_connected of this ResponseProjectRepository.


        :param is_connected: The is_connected of this ResponseProjectRepository.  # noqa: E501
        :type is_connected: bool
        """
        if self.local_vars_configuration.client_side_validation and is_connected is None:  # noqa: E501
            raise ValueError("Invalid value for `is_connected`, must not be `None`")  # noqa: E501

        self._is_connected = is_connected

    @property
    def organization_credentials_id(self):
        """Gets the organization_credentials_id of this ResponseProjectRepository.  # noqa: E501


        :return: The organization_credentials_id of this ResponseProjectRepository.  # noqa: E501
        :rtype: int
        """
        return self._organization_credentials_id

    @organization_credentials_id.setter
    def organization_credentials_id(self, organization_credentials_id):
        """Sets the organization_credentials_id of this ResponseProjectRepository.


        :param organization_credentials_id: The organization_credentials_id of this ResponseProjectRepository.  # noqa: E501
        :type organization_credentials_id: int
        """

        self._organization_credentials_id = organization_credentials_id

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
        if not isinstance(other, ResponseProjectRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseProjectRepository):
            return True

        return self.to_dict() != other.to_dict()
