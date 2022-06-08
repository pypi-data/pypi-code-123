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


class ResponseCodeRepository(object):
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
        'git_diff_file': 'str',
        'git_owner': 'str',
        'git_provider': 'str',
        'git_ref': 'str',
        'git_repo': 'str',
        'organization_credentials_id': 'int',
        'url': 'str'
    }

    attribute_map = {
        'git_diff_file': 'git_diff_file',
        'git_owner': 'git_owner',
        'git_provider': 'git_provider',
        'git_ref': 'git_ref',
        'git_repo': 'git_repo',
        'organization_credentials_id': 'organization_credentials_id',
        'url': 'url'
    }

    def __init__(self, git_diff_file=None, git_owner=None, git_provider=None, git_ref=None, git_repo=None, organization_credentials_id=None, url=None, local_vars_configuration=None):  # noqa: E501
        """ResponseCodeRepository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._git_diff_file = None
        self._git_owner = None
        self._git_provider = None
        self._git_ref = None
        self._git_repo = None
        self._organization_credentials_id = None
        self._url = None
        self.discriminator = None

        if git_diff_file is not None:
            self.git_diff_file = git_diff_file
        if git_owner is not None:
            self.git_owner = git_owner
        if git_provider is not None:
            self.git_provider = git_provider
        if git_ref is not None:
            self.git_ref = git_ref
        if git_repo is not None:
            self.git_repo = git_repo
        self.organization_credentials_id = organization_credentials_id
        if url is not None:
            self.url = url

    @property
    def git_diff_file(self):
        """Gets the git_diff_file of this ResponseCodeRepository.  # noqa: E501


        :return: The git_diff_file of this ResponseCodeRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_diff_file

    @git_diff_file.setter
    def git_diff_file(self, git_diff_file):
        """Sets the git_diff_file of this ResponseCodeRepository.


        :param git_diff_file: The git_diff_file of this ResponseCodeRepository.  # noqa: E501
        :type git_diff_file: str
        """

        self._git_diff_file = git_diff_file

    @property
    def git_owner(self):
        """Gets the git_owner of this ResponseCodeRepository.  # noqa: E501


        :return: The git_owner of this ResponseCodeRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_owner

    @git_owner.setter
    def git_owner(self, git_owner):
        """Sets the git_owner of this ResponseCodeRepository.


        :param git_owner: The git_owner of this ResponseCodeRepository.  # noqa: E501
        :type git_owner: str
        """

        self._git_owner = git_owner

    @property
    def git_provider(self):
        """Gets the git_provider of this ResponseCodeRepository.  # noqa: E501


        :return: The git_provider of this ResponseCodeRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_provider

    @git_provider.setter
    def git_provider(self, git_provider):
        """Sets the git_provider of this ResponseCodeRepository.


        :param git_provider: The git_provider of this ResponseCodeRepository.  # noqa: E501
        :type git_provider: str
        """

        self._git_provider = git_provider

    @property
    def git_ref(self):
        """Gets the git_ref of this ResponseCodeRepository.  # noqa: E501


        :return: The git_ref of this ResponseCodeRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_ref

    @git_ref.setter
    def git_ref(self, git_ref):
        """Sets the git_ref of this ResponseCodeRepository.


        :param git_ref: The git_ref of this ResponseCodeRepository.  # noqa: E501
        :type git_ref: str
        """

        self._git_ref = git_ref

    @property
    def git_repo(self):
        """Gets the git_repo of this ResponseCodeRepository.  # noqa: E501


        :return: The git_repo of this ResponseCodeRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_repo

    @git_repo.setter
    def git_repo(self, git_repo):
        """Sets the git_repo of this ResponseCodeRepository.


        :param git_repo: The git_repo of this ResponseCodeRepository.  # noqa: E501
        :type git_repo: str
        """

        self._git_repo = git_repo

    @property
    def organization_credentials_id(self):
        """Gets the organization_credentials_id of this ResponseCodeRepository.  # noqa: E501


        :return: The organization_credentials_id of this ResponseCodeRepository.  # noqa: E501
        :rtype: int
        """
        return self._organization_credentials_id

    @organization_credentials_id.setter
    def organization_credentials_id(self, organization_credentials_id):
        """Sets the organization_credentials_id of this ResponseCodeRepository.


        :param organization_credentials_id: The organization_credentials_id of this ResponseCodeRepository.  # noqa: E501
        :type organization_credentials_id: int
        """

        self._organization_credentials_id = organization_credentials_id

    @property
    def url(self):
        """Gets the url of this ResponseCodeRepository.  # noqa: E501


        :return: The url of this ResponseCodeRepository.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ResponseCodeRepository.


        :param url: The url of this ResponseCodeRepository.  # noqa: E501
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
        if not isinstance(other, ResponseCodeRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseCodeRepository):
            return True

        return self.to_dict() != other.to_dict()
