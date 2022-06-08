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


class ResponseKernelClusterInfo(object):
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
        'available_gpus': 'list[str]',
        'config': 'OrmKernelClusterConfig',
        'created_dt': 'datetime',
        'current_system_metrics': 'list[InfluxdbCurrentSystemMetric]',
        'docs_link': 'str',
        'id': 'int',
        'is_cluster_admin': 'bool',
        'is_registered': 'bool',
        'is_savvihub_managed': 'bool',
        'issues': 'list[str]',
        'kubernetes_ingress_endpoint': 'str',
        'kubernetes_namespace': 'str',
        'kubernetes_service_type': 'str',
        'message': 'str',
        'name': 'str',
        'nodes_summary': 'dict(str, int)',
        'provider': 'str',
        'region': 'str',
        'status': 'str',
        'updated_dt': 'datetime',
        'workloads_summary': 'OrmWorkloadsSummary'
    }

    attribute_map = {
        'available_gpus': 'available_gpus',
        'config': 'config',
        'created_dt': 'created_dt',
        'current_system_metrics': 'current_system_metrics',
        'docs_link': 'docs_link',
        'id': 'id',
        'is_cluster_admin': 'is_cluster_admin',
        'is_registered': 'is_registered',
        'is_savvihub_managed': 'is_savvihub_managed',
        'issues': 'issues',
        'kubernetes_ingress_endpoint': 'kubernetes_ingress_endpoint',
        'kubernetes_namespace': 'kubernetes_namespace',
        'kubernetes_service_type': 'kubernetes_service_type',
        'message': 'message',
        'name': 'name',
        'nodes_summary': 'nodes_summary',
        'provider': 'provider',
        'region': 'region',
        'status': 'status',
        'updated_dt': 'updated_dt',
        'workloads_summary': 'workloads_summary'
    }

    def __init__(self, available_gpus=None, config=None, created_dt=None, current_system_metrics=None, docs_link=None, id=None, is_cluster_admin=None, is_registered=None, is_savvihub_managed=None, issues=None, kubernetes_ingress_endpoint=None, kubernetes_namespace=None, kubernetes_service_type=None, message=None, name=None, nodes_summary=None, provider=None, region=None, status=None, updated_dt=None, workloads_summary=None, local_vars_configuration=None):  # noqa: E501
        """ResponseKernelClusterInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._available_gpus = None
        self._config = None
        self._created_dt = None
        self._current_system_metrics = None
        self._docs_link = None
        self._id = None
        self._is_cluster_admin = None
        self._is_registered = None
        self._is_savvihub_managed = None
        self._issues = None
        self._kubernetes_ingress_endpoint = None
        self._kubernetes_namespace = None
        self._kubernetes_service_type = None
        self._message = None
        self._name = None
        self._nodes_summary = None
        self._provider = None
        self._region = None
        self._status = None
        self._updated_dt = None
        self._workloads_summary = None
        self.discriminator = None

        if available_gpus is not None:
            self.available_gpus = available_gpus
        if config is not None:
            self.config = config
        self.created_dt = created_dt
        if current_system_metrics is not None:
            self.current_system_metrics = current_system_metrics
        self.docs_link = docs_link
        self.id = id
        if is_cluster_admin is not None:
            self.is_cluster_admin = is_cluster_admin
        if is_registered is not None:
            self.is_registered = is_registered
        self.is_savvihub_managed = is_savvihub_managed
        if issues is not None:
            self.issues = issues
        self.kubernetes_ingress_endpoint = kubernetes_ingress_endpoint
        self.kubernetes_namespace = kubernetes_namespace
        self.kubernetes_service_type = kubernetes_service_type
        self.message = message
        self.name = name
        if nodes_summary is not None:
            self.nodes_summary = nodes_summary
        self.provider = provider
        self.region = region
        self.status = status
        self.updated_dt = updated_dt
        if workloads_summary is not None:
            self.workloads_summary = workloads_summary

    @property
    def available_gpus(self):
        """Gets the available_gpus of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The available_gpus of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_gpus

    @available_gpus.setter
    def available_gpus(self, available_gpus):
        """Sets the available_gpus of this ResponseKernelClusterInfo.


        :param available_gpus: The available_gpus of this ResponseKernelClusterInfo.  # noqa: E501
        :type available_gpus: list[str]
        """

        self._available_gpus = available_gpus

    @property
    def config(self):
        """Gets the config of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The config of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: OrmKernelClusterConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ResponseKernelClusterInfo.


        :param config: The config of this ResponseKernelClusterInfo.  # noqa: E501
        :type config: OrmKernelClusterConfig
        """

        self._config = config

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The created_dt of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseKernelClusterInfo.


        :param created_dt: The created_dt of this ResponseKernelClusterInfo.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def current_system_metrics(self):
        """Gets the current_system_metrics of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The current_system_metrics of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: list[InfluxdbCurrentSystemMetric]
        """
        return self._current_system_metrics

    @current_system_metrics.setter
    def current_system_metrics(self, current_system_metrics):
        """Sets the current_system_metrics of this ResponseKernelClusterInfo.


        :param current_system_metrics: The current_system_metrics of this ResponseKernelClusterInfo.  # noqa: E501
        :type current_system_metrics: list[InfluxdbCurrentSystemMetric]
        """

        self._current_system_metrics = current_system_metrics

    @property
    def docs_link(self):
        """Gets the docs_link of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The docs_link of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._docs_link

    @docs_link.setter
    def docs_link(self, docs_link):
        """Sets the docs_link of this ResponseKernelClusterInfo.


        :param docs_link: The docs_link of this ResponseKernelClusterInfo.  # noqa: E501
        :type docs_link: str
        """

        self._docs_link = docs_link

    @property
    def id(self):
        """Gets the id of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The id of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseKernelClusterInfo.


        :param id: The id of this ResponseKernelClusterInfo.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_cluster_admin(self):
        """Gets the is_cluster_admin of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The is_cluster_admin of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_cluster_admin

    @is_cluster_admin.setter
    def is_cluster_admin(self, is_cluster_admin):
        """Sets the is_cluster_admin of this ResponseKernelClusterInfo.


        :param is_cluster_admin: The is_cluster_admin of this ResponseKernelClusterInfo.  # noqa: E501
        :type is_cluster_admin: bool
        """

        self._is_cluster_admin = is_cluster_admin

    @property
    def is_registered(self):
        """Gets the is_registered of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The is_registered of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_registered

    @is_registered.setter
    def is_registered(self, is_registered):
        """Sets the is_registered of this ResponseKernelClusterInfo.


        :param is_registered: The is_registered of this ResponseKernelClusterInfo.  # noqa: E501
        :type is_registered: bool
        """

        self._is_registered = is_registered

    @property
    def is_savvihub_managed(self):
        """Gets the is_savvihub_managed of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The is_savvihub_managed of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_savvihub_managed

    @is_savvihub_managed.setter
    def is_savvihub_managed(self, is_savvihub_managed):
        """Sets the is_savvihub_managed of this ResponseKernelClusterInfo.


        :param is_savvihub_managed: The is_savvihub_managed of this ResponseKernelClusterInfo.  # noqa: E501
        :type is_savvihub_managed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_savvihub_managed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_savvihub_managed`, must not be `None`")  # noqa: E501

        self._is_savvihub_managed = is_savvihub_managed

    @property
    def issues(self):
        """Gets the issues of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The issues of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this ResponseKernelClusterInfo.


        :param issues: The issues of this ResponseKernelClusterInfo.  # noqa: E501
        :type issues: list[str]
        """

        self._issues = issues

    @property
    def kubernetes_ingress_endpoint(self):
        """Gets the kubernetes_ingress_endpoint of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The kubernetes_ingress_endpoint of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_ingress_endpoint

    @kubernetes_ingress_endpoint.setter
    def kubernetes_ingress_endpoint(self, kubernetes_ingress_endpoint):
        """Sets the kubernetes_ingress_endpoint of this ResponseKernelClusterInfo.


        :param kubernetes_ingress_endpoint: The kubernetes_ingress_endpoint of this ResponseKernelClusterInfo.  # noqa: E501
        :type kubernetes_ingress_endpoint: str
        """

        self._kubernetes_ingress_endpoint = kubernetes_ingress_endpoint

    @property
    def kubernetes_namespace(self):
        """Gets the kubernetes_namespace of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The kubernetes_namespace of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_namespace

    @kubernetes_namespace.setter
    def kubernetes_namespace(self, kubernetes_namespace):
        """Sets the kubernetes_namespace of this ResponseKernelClusterInfo.


        :param kubernetes_namespace: The kubernetes_namespace of this ResponseKernelClusterInfo.  # noqa: E501
        :type kubernetes_namespace: str
        """

        self._kubernetes_namespace = kubernetes_namespace

    @property
    def kubernetes_service_type(self):
        """Gets the kubernetes_service_type of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The kubernetes_service_type of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_service_type

    @kubernetes_service_type.setter
    def kubernetes_service_type(self, kubernetes_service_type):
        """Sets the kubernetes_service_type of this ResponseKernelClusterInfo.


        :param kubernetes_service_type: The kubernetes_service_type of this ResponseKernelClusterInfo.  # noqa: E501
        :type kubernetes_service_type: str
        """
        if self.local_vars_configuration.client_side_validation and kubernetes_service_type is None:  # noqa: E501
            raise ValueError("Invalid value for `kubernetes_service_type`, must not be `None`")  # noqa: E501

        self._kubernetes_service_type = kubernetes_service_type

    @property
    def message(self):
        """Gets the message of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The message of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseKernelClusterInfo.


        :param message: The message of this ResponseKernelClusterInfo.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def name(self):
        """Gets the name of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The name of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseKernelClusterInfo.


        :param name: The name of this ResponseKernelClusterInfo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nodes_summary(self):
        """Gets the nodes_summary of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The nodes_summary of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._nodes_summary

    @nodes_summary.setter
    def nodes_summary(self, nodes_summary):
        """Sets the nodes_summary of this ResponseKernelClusterInfo.


        :param nodes_summary: The nodes_summary of this ResponseKernelClusterInfo.  # noqa: E501
        :type nodes_summary: dict(str, int)
        """

        self._nodes_summary = nodes_summary

    @property
    def provider(self):
        """Gets the provider of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The provider of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ResponseKernelClusterInfo.


        :param provider: The provider of this ResponseKernelClusterInfo.  # noqa: E501
        :type provider: str
        """
        if self.local_vars_configuration.client_side_validation and provider is None:  # noqa: E501
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["VESSL", "AWS", "GCP", "Azure", "on-premise"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and provider not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def region(self):
        """Gets the region of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The region of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ResponseKernelClusterInfo.


        :param region: The region of this ResponseKernelClusterInfo.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def status(self):
        """Gets the status of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The status of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseKernelClusterInfo.


        :param status: The status of this ResponseKernelClusterInfo.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["connected", "not-connected", "permission-required", "agent-not-available", "prometheus-not-available", "modifying"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The updated_dt of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseKernelClusterInfo.


        :param updated_dt: The updated_dt of this ResponseKernelClusterInfo.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

    @property
    def workloads_summary(self):
        """Gets the workloads_summary of this ResponseKernelClusterInfo.  # noqa: E501


        :return: The workloads_summary of this ResponseKernelClusterInfo.  # noqa: E501
        :rtype: OrmWorkloadsSummary
        """
        return self._workloads_summary

    @workloads_summary.setter
    def workloads_summary(self, workloads_summary):
        """Sets the workloads_summary of this ResponseKernelClusterInfo.


        :param workloads_summary: The workloads_summary of this ResponseKernelClusterInfo.  # noqa: E501
        :type workloads_summary: OrmWorkloadsSummary
        """

        self._workloads_summary = workloads_summary

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
        if not isinstance(other, ResponseKernelClusterInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseKernelClusterInfo):
            return True

        return self.to_dict() != other.to_dict()
