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


class ResponseModelDetail(object):
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
        'artifact_volume_id': 'int',
        'created_by': 'ResponseUser',
        'created_dt': 'datetime',
        'experiment': 'ResponseSimpleExperiment',
        'generated_experiments': 'list[ResponseSimpleExperiment]',
        'id': 'int',
        'is_servable': 'bool',
        'metrics_summary': 'OrmExperimentMetricsSummary',
        'model_repository': 'ResponseModelRepositoryDetail',
        'name': 'str',
        'number': 'int',
        'service': 'ResponseSimpleServiceInfo',
        'status': 'str',
        'status_reason': 'str',
        'tags': 'list[ResponseTagResponse]',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'artifact_volume_id': 'artifact_volume_id',
        'created_by': 'created_by',
        'created_dt': 'created_dt',
        'experiment': 'experiment',
        'generated_experiments': 'generated_experiments',
        'id': 'id',
        'is_servable': 'is_servable',
        'metrics_summary': 'metrics_summary',
        'model_repository': 'model_repository',
        'name': 'name',
        'number': 'number',
        'service': 'service',
        'status': 'status',
        'status_reason': 'status_reason',
        'tags': 'tags',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, artifact_volume_id=None, created_by=None, created_dt=None, experiment=None, generated_experiments=None, id=None, is_servable=None, metrics_summary=None, model_repository=None, name=None, number=None, service=None, status=None, status_reason=None, tags=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ResponseModelDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._artifact_volume_id = None
        self._created_by = None
        self._created_dt = None
        self._experiment = None
        self._generated_experiments = None
        self._id = None
        self._is_servable = None
        self._metrics_summary = None
        self._model_repository = None
        self._name = None
        self._number = None
        self._service = None
        self._status = None
        self._status_reason = None
        self._tags = None
        self._updated_dt = None
        self.discriminator = None

        self.artifact_volume_id = artifact_volume_id
        self.created_by = created_by
        self.created_dt = created_dt
        if experiment is not None:
            self.experiment = experiment
        self.generated_experiments = generated_experiments
        self.id = id
        self.is_servable = is_servable
        if metrics_summary is not None:
            self.metrics_summary = metrics_summary
        self.model_repository = model_repository
        self.name = name
        self.number = number
        if service is not None:
            self.service = service
        self.status = status
        self.status_reason = status_reason
        self.tags = tags
        self.updated_dt = updated_dt

    @property
    def artifact_volume_id(self):
        """Gets the artifact_volume_id of this ResponseModelDetail.  # noqa: E501


        :return: The artifact_volume_id of this ResponseModelDetail.  # noqa: E501
        :rtype: int
        """
        return self._artifact_volume_id

    @artifact_volume_id.setter
    def artifact_volume_id(self, artifact_volume_id):
        """Sets the artifact_volume_id of this ResponseModelDetail.


        :param artifact_volume_id: The artifact_volume_id of this ResponseModelDetail.  # noqa: E501
        :type artifact_volume_id: int
        """
        if self.local_vars_configuration.client_side_validation and artifact_volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `artifact_volume_id`, must not be `None`")  # noqa: E501

        self._artifact_volume_id = artifact_volume_id

    @property
    def created_by(self):
        """Gets the created_by of this ResponseModelDetail.  # noqa: E501


        :return: The created_by of this ResponseModelDetail.  # noqa: E501
        :rtype: ResponseUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ResponseModelDetail.


        :param created_by: The created_by of this ResponseModelDetail.  # noqa: E501
        :type created_by: ResponseUser
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseModelDetail.  # noqa: E501


        :return: The created_dt of this ResponseModelDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseModelDetail.


        :param created_dt: The created_dt of this ResponseModelDetail.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def experiment(self):
        """Gets the experiment of this ResponseModelDetail.  # noqa: E501


        :return: The experiment of this ResponseModelDetail.  # noqa: E501
        :rtype: ResponseSimpleExperiment
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ResponseModelDetail.


        :param experiment: The experiment of this ResponseModelDetail.  # noqa: E501
        :type experiment: ResponseSimpleExperiment
        """

        self._experiment = experiment

    @property
    def generated_experiments(self):
        """Gets the generated_experiments of this ResponseModelDetail.  # noqa: E501


        :return: The generated_experiments of this ResponseModelDetail.  # noqa: E501
        :rtype: list[ResponseSimpleExperiment]
        """
        return self._generated_experiments

    @generated_experiments.setter
    def generated_experiments(self, generated_experiments):
        """Sets the generated_experiments of this ResponseModelDetail.


        :param generated_experiments: The generated_experiments of this ResponseModelDetail.  # noqa: E501
        :type generated_experiments: list[ResponseSimpleExperiment]
        """
        if self.local_vars_configuration.client_side_validation and generated_experiments is None:  # noqa: E501
            raise ValueError("Invalid value for `generated_experiments`, must not be `None`")  # noqa: E501

        self._generated_experiments = generated_experiments

    @property
    def id(self):
        """Gets the id of this ResponseModelDetail.  # noqa: E501


        :return: The id of this ResponseModelDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseModelDetail.


        :param id: The id of this ResponseModelDetail.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_servable(self):
        """Gets the is_servable of this ResponseModelDetail.  # noqa: E501


        :return: The is_servable of this ResponseModelDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_servable

    @is_servable.setter
    def is_servable(self, is_servable):
        """Sets the is_servable of this ResponseModelDetail.


        :param is_servable: The is_servable of this ResponseModelDetail.  # noqa: E501
        :type is_servable: bool
        """
        if self.local_vars_configuration.client_side_validation and is_servable is None:  # noqa: E501
            raise ValueError("Invalid value for `is_servable`, must not be `None`")  # noqa: E501

        self._is_servable = is_servable

    @property
    def metrics_summary(self):
        """Gets the metrics_summary of this ResponseModelDetail.  # noqa: E501


        :return: The metrics_summary of this ResponseModelDetail.  # noqa: E501
        :rtype: OrmExperimentMetricsSummary
        """
        return self._metrics_summary

    @metrics_summary.setter
    def metrics_summary(self, metrics_summary):
        """Sets the metrics_summary of this ResponseModelDetail.


        :param metrics_summary: The metrics_summary of this ResponseModelDetail.  # noqa: E501
        :type metrics_summary: OrmExperimentMetricsSummary
        """

        self._metrics_summary = metrics_summary

    @property
    def model_repository(self):
        """Gets the model_repository of this ResponseModelDetail.  # noqa: E501


        :return: The model_repository of this ResponseModelDetail.  # noqa: E501
        :rtype: ResponseModelRepositoryDetail
        """
        return self._model_repository

    @model_repository.setter
    def model_repository(self, model_repository):
        """Sets the model_repository of this ResponseModelDetail.


        :param model_repository: The model_repository of this ResponseModelDetail.  # noqa: E501
        :type model_repository: ResponseModelRepositoryDetail
        """
        if self.local_vars_configuration.client_side_validation and model_repository is None:  # noqa: E501
            raise ValueError("Invalid value for `model_repository`, must not be `None`")  # noqa: E501

        self._model_repository = model_repository

    @property
    def name(self):
        """Gets the name of this ResponseModelDetail.  # noqa: E501


        :return: The name of this ResponseModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseModelDetail.


        :param name: The name of this ResponseModelDetail.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this ResponseModelDetail.  # noqa: E501


        :return: The number of this ResponseModelDetail.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ResponseModelDetail.


        :param number: The number of this ResponseModelDetail.  # noqa: E501
        :type number: int
        """
        if self.local_vars_configuration.client_side_validation and number is None:  # noqa: E501
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def service(self):
        """Gets the service of this ResponseModelDetail.  # noqa: E501


        :return: The service of this ResponseModelDetail.  # noqa: E501
        :rtype: ResponseSimpleServiceInfo
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ResponseModelDetail.


        :param service: The service of this ResponseModelDetail.  # noqa: E501
        :type service: ResponseSimpleServiceInfo
        """

        self._service = service

    @property
    def status(self):
        """Gets the status of this ResponseModelDetail.  # noqa: E501


        :return: The status of this ResponseModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseModelDetail.


        :param status: The status of this ResponseModelDetail.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this ResponseModelDetail.  # noqa: E501


        :return: The status_reason of this ResponseModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this ResponseModelDetail.


        :param status_reason: The status_reason of this ResponseModelDetail.  # noqa: E501
        :type status_reason: str
        """
        if self.local_vars_configuration.client_side_validation and status_reason is None:  # noqa: E501
            raise ValueError("Invalid value for `status_reason`, must not be `None`")  # noqa: E501

        self._status_reason = status_reason

    @property
    def tags(self):
        """Gets the tags of this ResponseModelDetail.  # noqa: E501


        :return: The tags of this ResponseModelDetail.  # noqa: E501
        :rtype: list[ResponseTagResponse]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResponseModelDetail.


        :param tags: The tags of this ResponseModelDetail.  # noqa: E501
        :type tags: list[ResponseTagResponse]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseModelDetail.  # noqa: E501


        :return: The updated_dt of this ResponseModelDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseModelDetail.


        :param updated_dt: The updated_dt of this ResponseModelDetail.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ResponseModelDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseModelDetail):
            return True

        return self.to_dict() != other.to_dict()
