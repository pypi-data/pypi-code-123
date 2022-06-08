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


class LocalExperimentCreateAPIInput(object):
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
        'execution_environment': 'OrmExecutionEnvironment',
        'hyperparameters': 'list[OrmHyperparameter]',
        'message': 'str'
    }

    attribute_map = {
        'execution_environment': 'execution_environment',
        'hyperparameters': 'hyperparameters',
        'message': 'message'
    }

    def __init__(self, execution_environment=None, hyperparameters=None, message=None, local_vars_configuration=None):  # noqa: E501
        """LocalExperimentCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._execution_environment = None
        self._hyperparameters = None
        self._message = None
        self.discriminator = None

        if execution_environment is not None:
            self.execution_environment = execution_environment
        if hyperparameters is not None:
            self.hyperparameters = hyperparameters
        self.message = message

    @property
    def execution_environment(self):
        """Gets the execution_environment of this LocalExperimentCreateAPIInput.  # noqa: E501


        :return: The execution_environment of this LocalExperimentCreateAPIInput.  # noqa: E501
        :rtype: OrmExecutionEnvironment
        """
        return self._execution_environment

    @execution_environment.setter
    def execution_environment(self, execution_environment):
        """Sets the execution_environment of this LocalExperimentCreateAPIInput.


        :param execution_environment: The execution_environment of this LocalExperimentCreateAPIInput.  # noqa: E501
        :type execution_environment: OrmExecutionEnvironment
        """

        self._execution_environment = execution_environment

    @property
    def hyperparameters(self):
        """Gets the hyperparameters of this LocalExperimentCreateAPIInput.  # noqa: E501


        :return: The hyperparameters of this LocalExperimentCreateAPIInput.  # noqa: E501
        :rtype: list[OrmHyperparameter]
        """
        return self._hyperparameters

    @hyperparameters.setter
    def hyperparameters(self, hyperparameters):
        """Sets the hyperparameters of this LocalExperimentCreateAPIInput.


        :param hyperparameters: The hyperparameters of this LocalExperimentCreateAPIInput.  # noqa: E501
        :type hyperparameters: list[OrmHyperparameter]
        """

        self._hyperparameters = hyperparameters

    @property
    def message(self):
        """Gets the message of this LocalExperimentCreateAPIInput.  # noqa: E501


        :return: The message of this LocalExperimentCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LocalExperimentCreateAPIInput.


        :param message: The message of this LocalExperimentCreateAPIInput.  # noqa: E501
        :type message: str
        """
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) > 255):
            raise ValueError("Invalid value for `message`, length must be less than or equal to `255`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, LocalExperimentCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalExperimentCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
