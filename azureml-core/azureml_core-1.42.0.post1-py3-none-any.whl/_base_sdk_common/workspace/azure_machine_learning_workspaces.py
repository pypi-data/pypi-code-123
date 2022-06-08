# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrestazure import AzureConfiguration
from .version import VERSION
from azureml._base_sdk_common import __version__ as SDK_VERSION
from .operations.operations import Operations
from .operations.workspaces_operations import WorkspacesOperations
from .operations.machine_learning_compute_operations import MachineLearningComputeOperations
from .operations.workspace_connections_operations import WorkspaceConnectionsOperations
from .operations.private_link_resources_operations import PrivateLinkResourcesOperations
from .operations.private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from .operations.linked_services_operations import LinkedServicesOperations
from . import models


class AzureMachineLearningWorkspacesConfiguration(AzureConfiguration):
    """Configuration for AzureMachineLearningWorkspaces
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str
    :param compute_type1: Type of compute to filter by.
    :type compute_type1: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, credentials, skiptoken=None, compute_type1=None, base_url=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AzureMachineLearningWorkspacesConfiguration, self).__init__(base_url)

        self.add_user_agent('azuremachinelearningworkspaces/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python/{}'.format(SDK_VERSION))

        self.subscription_id = subscription_id
        self.skiptoken = skiptoken
        self.compute_type1 = compute_type1
        self.credentials = credentials

        # We override a config in the retry policy to throw exceptions after retry.
        # By default this is True. We set it to false to get the full error trace, including url and
        # status code of the last retry. Otherwise, the error message is 'too many 500 error responses',
        # which is not useful.
        self.retry_policy.policy.raise_on_status = False


class AzureMachineLearningWorkspaces(object):
    """These APIs allow end users to operate on Azure Machine Learning Workspace resources.

    :ivar config: Configuration for client.
    :vartype config: AzureMachineLearningWorkspacesConfiguration

    :ivar operations: Operations operations
    :vartype operations: machinelearningservicesswagger.operations.Operations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: machinelearningservicesswagger.operations.WorkspacesOperations
    :ivar machine_learning_compute: MachineLearningCompute operations
    :vartype machine_learning_compute: machinelearningservicesswagger.operations.MachineLearningComputeOperations

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param skiptoken: Continuation token for pagination.
    :type skiptoken: str
    :param compute_type1: Type of compute to filter by.
    :type compute_type1: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, skiptoken=None, compute_type1=None, base_url=None):

        from msrest.service_client import ServiceClient
        from msrest import Serializer, Deserializer

        self.config = AzureMachineLearningWorkspacesConfiguration(subscription_id, credentials,
                                                                  skiptoken, compute_type1, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.machine_learning_compute = MachineLearningComputeOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_connections = WorkspaceConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
