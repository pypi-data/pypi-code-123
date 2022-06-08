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


class ResponseOrganizationMember(object):
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
        'created_dt': 'datetime',
        'deleted_dt': 'datetime',
        'display_name': 'str',
        'email': 'str',
        'id': 'int',
        'joined_dt': 'datetime',
        'permission': 'str',
        'status': 'str',
        'updated_dt': 'datetime',
        'username': 'str'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'deleted_dt': 'deleted_dt',
        'display_name': 'display_name',
        'email': 'email',
        'id': 'id',
        'joined_dt': 'joined_dt',
        'permission': 'permission',
        'status': 'status',
        'updated_dt': 'updated_dt',
        'username': 'username'
    }

    def __init__(self, created_dt=None, deleted_dt=None, display_name=None, email=None, id=None, joined_dt=None, permission=None, status=None, updated_dt=None, username=None, local_vars_configuration=None):  # noqa: E501
        """ResponseOrganizationMember - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._deleted_dt = None
        self._display_name = None
        self._email = None
        self._id = None
        self._joined_dt = None
        self._permission = None
        self._status = None
        self._updated_dt = None
        self._username = None
        self.discriminator = None

        self.created_dt = created_dt
        self.deleted_dt = deleted_dt
        self.display_name = display_name
        self.email = email
        self.id = id
        self.joined_dt = joined_dt
        self.permission = permission
        self.status = status
        self.updated_dt = updated_dt
        self.username = username

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseOrganizationMember.  # noqa: E501


        :return: The created_dt of this ResponseOrganizationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseOrganizationMember.


        :param created_dt: The created_dt of this ResponseOrganizationMember.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def deleted_dt(self):
        """Gets the deleted_dt of this ResponseOrganizationMember.  # noqa: E501


        :return: The deleted_dt of this ResponseOrganizationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_dt

    @deleted_dt.setter
    def deleted_dt(self, deleted_dt):
        """Sets the deleted_dt of this ResponseOrganizationMember.


        :param deleted_dt: The deleted_dt of this ResponseOrganizationMember.  # noqa: E501
        :type deleted_dt: datetime
        """

        self._deleted_dt = deleted_dt

    @property
    def display_name(self):
        """Gets the display_name of this ResponseOrganizationMember.  # noqa: E501


        :return: The display_name of this ResponseOrganizationMember.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResponseOrganizationMember.


        :param display_name: The display_name of this ResponseOrganizationMember.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this ResponseOrganizationMember.  # noqa: E501


        :return: The email of this ResponseOrganizationMember.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResponseOrganizationMember.


        :param email: The email of this ResponseOrganizationMember.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def id(self):
        """Gets the id of this ResponseOrganizationMember.  # noqa: E501


        :return: The id of this ResponseOrganizationMember.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseOrganizationMember.


        :param id: The id of this ResponseOrganizationMember.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def joined_dt(self):
        """Gets the joined_dt of this ResponseOrganizationMember.  # noqa: E501


        :return: The joined_dt of this ResponseOrganizationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._joined_dt

    @joined_dt.setter
    def joined_dt(self, joined_dt):
        """Sets the joined_dt of this ResponseOrganizationMember.


        :param joined_dt: The joined_dt of this ResponseOrganizationMember.  # noqa: E501
        :type joined_dt: datetime
        """

        self._joined_dt = joined_dt

    @property
    def permission(self):
        """Gets the permission of this ResponseOrganizationMember.  # noqa: E501


        :return: The permission of this ResponseOrganizationMember.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ResponseOrganizationMember.


        :param permission: The permission of this ResponseOrganizationMember.  # noqa: E501
        :type permission: str
        """
        if self.local_vars_configuration.client_side_validation and permission is None:  # noqa: E501
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def status(self):
        """Gets the status of this ResponseOrganizationMember.  # noqa: E501


        :return: The status of this ResponseOrganizationMember.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseOrganizationMember.


        :param status: The status of this ResponseOrganizationMember.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseOrganizationMember.  # noqa: E501


        :return: The updated_dt of this ResponseOrganizationMember.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseOrganizationMember.


        :param updated_dt: The updated_dt of this ResponseOrganizationMember.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def username(self):
        """Gets the username of this ResponseOrganizationMember.  # noqa: E501


        :return: The username of this ResponseOrganizationMember.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ResponseOrganizationMember.


        :param username: The username of this ResponseOrganizationMember.  # noqa: E501
        :type username: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ResponseOrganizationMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseOrganizationMember):
            return True

        return self.to_dict() != other.to_dict()
