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


class OrmKernelClusterNode(object):
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
        'availability_zone': 'str',
        'cpu_allocatable': 'float',
        'cpu_limits': 'float',
        'cpu_requests': 'float',
        'created_dt': 'datetime',
        'edges': 'OrmKernelClusterNodeEdges',
        'ephemeral_storage_allocatable': 'int',
        'ephemeral_storage_limits': 'int',
        'ephemeral_storage_requests': 'int',
        'gpu_allocatable': 'int',
        'gpu_limits': 'int',
        'gpu_product_name': 'str',
        'gpu_requests': 'int',
        'id': 'int',
        'immutable_slug': 'str',
        'internal_ip': 'str',
        'kernel_cluster_node_kernel_cluster': 'int',
        'memory_allocatable': 'int',
        'memory_limits': 'int',
        'memory_requests': 'int',
        'name': 'str',
        'status': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'cpu_allocatable': 'cpu_allocatable',
        'cpu_limits': 'cpu_limits',
        'cpu_requests': 'cpu_requests',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'ephemeral_storage_allocatable': 'ephemeral_storage_allocatable',
        'ephemeral_storage_limits': 'ephemeral_storage_limits',
        'ephemeral_storage_requests': 'ephemeral_storage_requests',
        'gpu_allocatable': 'gpu_allocatable',
        'gpu_limits': 'gpu_limits',
        'gpu_product_name': 'gpu_product_name',
        'gpu_requests': 'gpu_requests',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'internal_ip': 'internal_ip',
        'kernel_cluster_node_kernel_cluster': 'kernel_cluster_node_kernel_cluster',
        'memory_allocatable': 'memory_allocatable',
        'memory_limits': 'memory_limits',
        'memory_requests': 'memory_requests',
        'name': 'name',
        'status': 'status',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, availability_zone=None, cpu_allocatable=None, cpu_limits=None, cpu_requests=None, created_dt=None, edges=None, ephemeral_storage_allocatable=None, ephemeral_storage_limits=None, ephemeral_storage_requests=None, gpu_allocatable=None, gpu_limits=None, gpu_product_name=None, gpu_requests=None, id=None, immutable_slug=None, internal_ip=None, kernel_cluster_node_kernel_cluster=None, memory_allocatable=None, memory_limits=None, memory_requests=None, name=None, status=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmKernelClusterNode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._availability_zone = None
        self._cpu_allocatable = None
        self._cpu_limits = None
        self._cpu_requests = None
        self._created_dt = None
        self._edges = None
        self._ephemeral_storage_allocatable = None
        self._ephemeral_storage_limits = None
        self._ephemeral_storage_requests = None
        self._gpu_allocatable = None
        self._gpu_limits = None
        self._gpu_product_name = None
        self._gpu_requests = None
        self._id = None
        self._immutable_slug = None
        self._internal_ip = None
        self._kernel_cluster_node_kernel_cluster = None
        self._memory_allocatable = None
        self._memory_limits = None
        self._memory_requests = None
        self._name = None
        self._status = None
        self._updated_dt = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.cpu_allocatable = cpu_allocatable
        self.cpu_limits = cpu_limits
        self.cpu_requests = cpu_requests
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        self.ephemeral_storage_allocatable = ephemeral_storage_allocatable
        self.ephemeral_storage_limits = ephemeral_storage_limits
        self.ephemeral_storage_requests = ephemeral_storage_requests
        self.gpu_allocatable = gpu_allocatable
        self.gpu_limits = gpu_limits
        self.gpu_product_name = gpu_product_name
        self.gpu_requests = gpu_requests
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        self.internal_ip = internal_ip
        if kernel_cluster_node_kernel_cluster is not None:
            self.kernel_cluster_node_kernel_cluster = kernel_cluster_node_kernel_cluster
        self.memory_allocatable = memory_allocatable
        self.memory_limits = memory_limits
        self.memory_requests = memory_requests
        if name is not None:
            self.name = name
        self.status = status
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def availability_zone(self):
        """Gets the availability_zone of this OrmKernelClusterNode.  # noqa: E501


        :return: The availability_zone of this OrmKernelClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this OrmKernelClusterNode.


        :param availability_zone: The availability_zone of this OrmKernelClusterNode.  # noqa: E501
        :type availability_zone: str
        """

        self._availability_zone = availability_zone

    @property
    def cpu_allocatable(self):
        """Gets the cpu_allocatable of this OrmKernelClusterNode.  # noqa: E501


        :return: The cpu_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :rtype: float
        """
        return self._cpu_allocatable

    @cpu_allocatable.setter
    def cpu_allocatable(self, cpu_allocatable):
        """Sets the cpu_allocatable of this OrmKernelClusterNode.


        :param cpu_allocatable: The cpu_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :type cpu_allocatable: float
        """

        self._cpu_allocatable = cpu_allocatable

    @property
    def cpu_limits(self):
        """Gets the cpu_limits of this OrmKernelClusterNode.  # noqa: E501


        :return: The cpu_limits of this OrmKernelClusterNode.  # noqa: E501
        :rtype: float
        """
        return self._cpu_limits

    @cpu_limits.setter
    def cpu_limits(self, cpu_limits):
        """Sets the cpu_limits of this OrmKernelClusterNode.


        :param cpu_limits: The cpu_limits of this OrmKernelClusterNode.  # noqa: E501
        :type cpu_limits: float
        """

        self._cpu_limits = cpu_limits

    @property
    def cpu_requests(self):
        """Gets the cpu_requests of this OrmKernelClusterNode.  # noqa: E501


        :return: The cpu_requests of this OrmKernelClusterNode.  # noqa: E501
        :rtype: float
        """
        return self._cpu_requests

    @cpu_requests.setter
    def cpu_requests(self, cpu_requests):
        """Sets the cpu_requests of this OrmKernelClusterNode.


        :param cpu_requests: The cpu_requests of this OrmKernelClusterNode.  # noqa: E501
        :type cpu_requests: float
        """

        self._cpu_requests = cpu_requests

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmKernelClusterNode.  # noqa: E501


        :return: The created_dt of this OrmKernelClusterNode.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmKernelClusterNode.


        :param created_dt: The created_dt of this OrmKernelClusterNode.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmKernelClusterNode.  # noqa: E501


        :return: The edges of this OrmKernelClusterNode.  # noqa: E501
        :rtype: OrmKernelClusterNodeEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmKernelClusterNode.


        :param edges: The edges of this OrmKernelClusterNode.  # noqa: E501
        :type edges: OrmKernelClusterNodeEdges
        """

        self._edges = edges

    @property
    def ephemeral_storage_allocatable(self):
        """Gets the ephemeral_storage_allocatable of this OrmKernelClusterNode.  # noqa: E501


        :return: The ephemeral_storage_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._ephemeral_storage_allocatable

    @ephemeral_storage_allocatable.setter
    def ephemeral_storage_allocatable(self, ephemeral_storage_allocatable):
        """Sets the ephemeral_storage_allocatable of this OrmKernelClusterNode.


        :param ephemeral_storage_allocatable: The ephemeral_storage_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :type ephemeral_storage_allocatable: int
        """

        self._ephemeral_storage_allocatable = ephemeral_storage_allocatable

    @property
    def ephemeral_storage_limits(self):
        """Gets the ephemeral_storage_limits of this OrmKernelClusterNode.  # noqa: E501


        :return: The ephemeral_storage_limits of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._ephemeral_storage_limits

    @ephemeral_storage_limits.setter
    def ephemeral_storage_limits(self, ephemeral_storage_limits):
        """Sets the ephemeral_storage_limits of this OrmKernelClusterNode.


        :param ephemeral_storage_limits: The ephemeral_storage_limits of this OrmKernelClusterNode.  # noqa: E501
        :type ephemeral_storage_limits: int
        """

        self._ephemeral_storage_limits = ephemeral_storage_limits

    @property
    def ephemeral_storage_requests(self):
        """Gets the ephemeral_storage_requests of this OrmKernelClusterNode.  # noqa: E501


        :return: The ephemeral_storage_requests of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._ephemeral_storage_requests

    @ephemeral_storage_requests.setter
    def ephemeral_storage_requests(self, ephemeral_storage_requests):
        """Sets the ephemeral_storage_requests of this OrmKernelClusterNode.


        :param ephemeral_storage_requests: The ephemeral_storage_requests of this OrmKernelClusterNode.  # noqa: E501
        :type ephemeral_storage_requests: int
        """

        self._ephemeral_storage_requests = ephemeral_storage_requests

    @property
    def gpu_allocatable(self):
        """Gets the gpu_allocatable of this OrmKernelClusterNode.  # noqa: E501


        :return: The gpu_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._gpu_allocatable

    @gpu_allocatable.setter
    def gpu_allocatable(self, gpu_allocatable):
        """Sets the gpu_allocatable of this OrmKernelClusterNode.


        :param gpu_allocatable: The gpu_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :type gpu_allocatable: int
        """

        self._gpu_allocatable = gpu_allocatable

    @property
    def gpu_limits(self):
        """Gets the gpu_limits of this OrmKernelClusterNode.  # noqa: E501


        :return: The gpu_limits of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._gpu_limits

    @gpu_limits.setter
    def gpu_limits(self, gpu_limits):
        """Sets the gpu_limits of this OrmKernelClusterNode.


        :param gpu_limits: The gpu_limits of this OrmKernelClusterNode.  # noqa: E501
        :type gpu_limits: int
        """

        self._gpu_limits = gpu_limits

    @property
    def gpu_product_name(self):
        """Gets the gpu_product_name of this OrmKernelClusterNode.  # noqa: E501


        :return: The gpu_product_name of this OrmKernelClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._gpu_product_name

    @gpu_product_name.setter
    def gpu_product_name(self, gpu_product_name):
        """Sets the gpu_product_name of this OrmKernelClusterNode.


        :param gpu_product_name: The gpu_product_name of this OrmKernelClusterNode.  # noqa: E501
        :type gpu_product_name: str
        """

        self._gpu_product_name = gpu_product_name

    @property
    def gpu_requests(self):
        """Gets the gpu_requests of this OrmKernelClusterNode.  # noqa: E501


        :return: The gpu_requests of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._gpu_requests

    @gpu_requests.setter
    def gpu_requests(self, gpu_requests):
        """Sets the gpu_requests of this OrmKernelClusterNode.


        :param gpu_requests: The gpu_requests of this OrmKernelClusterNode.  # noqa: E501
        :type gpu_requests: int
        """

        self._gpu_requests = gpu_requests

    @property
    def id(self):
        """Gets the id of this OrmKernelClusterNode.  # noqa: E501


        :return: The id of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmKernelClusterNode.


        :param id: The id of this OrmKernelClusterNode.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmKernelClusterNode.  # noqa: E501


        :return: The immutable_slug of this OrmKernelClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmKernelClusterNode.


        :param immutable_slug: The immutable_slug of this OrmKernelClusterNode.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def internal_ip(self):
        """Gets the internal_ip of this OrmKernelClusterNode.  # noqa: E501


        :return: The internal_ip of this OrmKernelClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this OrmKernelClusterNode.


        :param internal_ip: The internal_ip of this OrmKernelClusterNode.  # noqa: E501
        :type internal_ip: str
        """

        self._internal_ip = internal_ip

    @property
    def kernel_cluster_node_kernel_cluster(self):
        """Gets the kernel_cluster_node_kernel_cluster of this OrmKernelClusterNode.  # noqa: E501


        :return: The kernel_cluster_node_kernel_cluster of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._kernel_cluster_node_kernel_cluster

    @kernel_cluster_node_kernel_cluster.setter
    def kernel_cluster_node_kernel_cluster(self, kernel_cluster_node_kernel_cluster):
        """Sets the kernel_cluster_node_kernel_cluster of this OrmKernelClusterNode.


        :param kernel_cluster_node_kernel_cluster: The kernel_cluster_node_kernel_cluster of this OrmKernelClusterNode.  # noqa: E501
        :type kernel_cluster_node_kernel_cluster: int
        """

        self._kernel_cluster_node_kernel_cluster = kernel_cluster_node_kernel_cluster

    @property
    def memory_allocatable(self):
        """Gets the memory_allocatable of this OrmKernelClusterNode.  # noqa: E501


        :return: The memory_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._memory_allocatable

    @memory_allocatable.setter
    def memory_allocatable(self, memory_allocatable):
        """Sets the memory_allocatable of this OrmKernelClusterNode.


        :param memory_allocatable: The memory_allocatable of this OrmKernelClusterNode.  # noqa: E501
        :type memory_allocatable: int
        """

        self._memory_allocatable = memory_allocatable

    @property
    def memory_limits(self):
        """Gets the memory_limits of this OrmKernelClusterNode.  # noqa: E501


        :return: The memory_limits of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._memory_limits

    @memory_limits.setter
    def memory_limits(self, memory_limits):
        """Sets the memory_limits of this OrmKernelClusterNode.


        :param memory_limits: The memory_limits of this OrmKernelClusterNode.  # noqa: E501
        :type memory_limits: int
        """

        self._memory_limits = memory_limits

    @property
    def memory_requests(self):
        """Gets the memory_requests of this OrmKernelClusterNode.  # noqa: E501


        :return: The memory_requests of this OrmKernelClusterNode.  # noqa: E501
        :rtype: int
        """
        return self._memory_requests

    @memory_requests.setter
    def memory_requests(self, memory_requests):
        """Sets the memory_requests of this OrmKernelClusterNode.


        :param memory_requests: The memory_requests of this OrmKernelClusterNode.  # noqa: E501
        :type memory_requests: int
        """

        self._memory_requests = memory_requests

    @property
    def name(self):
        """Gets the name of this OrmKernelClusterNode.  # noqa: E501


        :return: The name of this OrmKernelClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrmKernelClusterNode.


        :param name: The name of this OrmKernelClusterNode.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this OrmKernelClusterNode.  # noqa: E501


        :return: The status of this OrmKernelClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrmKernelClusterNode.


        :param status: The status of this OrmKernelClusterNode.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmKernelClusterNode.  # noqa: E501


        :return: The updated_dt of this OrmKernelClusterNode.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmKernelClusterNode.


        :param updated_dt: The updated_dt of this OrmKernelClusterNode.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

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
        if not isinstance(other, OrmKernelClusterNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmKernelClusterNode):
            return True

        return self.to_dict() != other.to_dict()
