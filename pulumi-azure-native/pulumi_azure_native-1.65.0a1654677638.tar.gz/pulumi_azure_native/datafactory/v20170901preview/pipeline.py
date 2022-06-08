# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 factory_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 activities: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AzureMLBatchExecutionActivityArgs', 'AzureMLUpdateResourceActivityArgs', 'ControlActivityArgs', 'CopyActivityArgs', 'CustomActivityArgs', 'DataLakeAnalyticsUSQLActivityArgs', 'DatabricksNotebookActivityArgs', 'ExecutePipelineActivityArgs', 'ExecuteSSISPackageActivityArgs', 'ExecutionActivityArgs', 'FilterActivityArgs', 'ForEachActivityArgs', 'GetMetadataActivityArgs', 'HDInsightHiveActivityArgs', 'HDInsightMapReduceActivityArgs', 'HDInsightPigActivityArgs', 'HDInsightSparkActivityArgs', 'HDInsightStreamingActivityArgs', 'IfConditionActivityArgs', 'LookupActivityArgs', 'SqlServerStoredProcedureActivityArgs', 'UntilActivityArgs', 'WaitActivityArgs', 'WebActivityArgs']]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[Any]]] = None,
                 concurrency: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterSpecificationArgs']]]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Sequence[pulumi.Input[Union['AzureMLBatchExecutionActivityArgs', 'AzureMLUpdateResourceActivityArgs', 'ControlActivityArgs', 'CopyActivityArgs', 'CustomActivityArgs', 'DataLakeAnalyticsUSQLActivityArgs', 'DatabricksNotebookActivityArgs', 'ExecutePipelineActivityArgs', 'ExecuteSSISPackageActivityArgs', 'ExecutionActivityArgs', 'FilterActivityArgs', 'ForEachActivityArgs', 'GetMetadataActivityArgs', 'HDInsightHiveActivityArgs', 'HDInsightMapReduceActivityArgs', 'HDInsightPigActivityArgs', 'HDInsightSparkActivityArgs', 'HDInsightStreamingActivityArgs', 'IfConditionActivityArgs', 'LookupActivityArgs', 'SqlServerStoredProcedureActivityArgs', 'UntilActivityArgs', 'WaitActivityArgs', 'WebActivityArgs']]]] activities: List of activities in pipeline.
        :param pulumi.Input[Sequence[Any]] annotations: List of tags that can be used for describing the Pipeline.
        :param pulumi.Input[int] concurrency: The max number of concurrent runs for the pipeline.
        :param pulumi.Input[str] description: The description of the pipeline.
        :param pulumi.Input[Mapping[str, pulumi.Input['ParameterSpecificationArgs']]] parameters: List of parameters for pipeline.
        :param pulumi.Input[str] pipeline_name: The pipeline name.
        """
        pulumi.set(__self__, "factory_name", factory_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if activities is not None:
            pulumi.set(__self__, "activities", activities)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if concurrency is not None:
            pulumi.set(__self__, "concurrency", concurrency)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if pipeline_name is not None:
            pulumi.set(__self__, "pipeline_name", pipeline_name)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[str]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def activities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['AzureMLBatchExecutionActivityArgs', 'AzureMLUpdateResourceActivityArgs', 'ControlActivityArgs', 'CopyActivityArgs', 'CustomActivityArgs', 'DataLakeAnalyticsUSQLActivityArgs', 'DatabricksNotebookActivityArgs', 'ExecutePipelineActivityArgs', 'ExecuteSSISPackageActivityArgs', 'ExecutionActivityArgs', 'FilterActivityArgs', 'ForEachActivityArgs', 'GetMetadataActivityArgs', 'HDInsightHiveActivityArgs', 'HDInsightMapReduceActivityArgs', 'HDInsightPigActivityArgs', 'HDInsightSparkActivityArgs', 'HDInsightStreamingActivityArgs', 'IfConditionActivityArgs', 'LookupActivityArgs', 'SqlServerStoredProcedureActivityArgs', 'UntilActivityArgs', 'WaitActivityArgs', 'WebActivityArgs']]]]]:
        """
        List of activities in pipeline.
        """
        return pulumi.get(self, "activities")

    @activities.setter
    def activities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['AzureMLBatchExecutionActivityArgs', 'AzureMLUpdateResourceActivityArgs', 'ControlActivityArgs', 'CopyActivityArgs', 'CustomActivityArgs', 'DataLakeAnalyticsUSQLActivityArgs', 'DatabricksNotebookActivityArgs', 'ExecutePipelineActivityArgs', 'ExecuteSSISPackageActivityArgs', 'ExecutionActivityArgs', 'FilterActivityArgs', 'ForEachActivityArgs', 'GetMetadataActivityArgs', 'HDInsightHiveActivityArgs', 'HDInsightMapReduceActivityArgs', 'HDInsightPigActivityArgs', 'HDInsightSparkActivityArgs', 'HDInsightStreamingActivityArgs', 'IfConditionActivityArgs', 'LookupActivityArgs', 'SqlServerStoredProcedureActivityArgs', 'UntilActivityArgs', 'WaitActivityArgs', 'WebActivityArgs']]]]]):
        pulumi.set(self, "activities", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        """
        List of tags that can be used for describing the Pipeline.
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter
    def concurrency(self) -> Optional[pulumi.Input[int]]:
        """
        The max number of concurrent runs for the pipeline.
        """
        return pulumi.get(self, "concurrency")

    @concurrency.setter
    def concurrency(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "concurrency", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the pipeline.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterSpecificationArgs']]]]:
        """
        List of parameters for pipeline.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ParameterSpecificationArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        The pipeline name.
        """
        return pulumi.get(self, "pipeline_name")

    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_name", value)


warnings.warn("""Version v20170901preview will be removed in the next major version of the provider. Upgrade to version v20180601 or later.""", DeprecationWarning)


class Pipeline(pulumi.CustomResource):
    warnings.warn("""Version v20170901preview will be removed in the next major version of the provider. Upgrade to version v20180601 or later.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AzureMLBatchExecutionActivityArgs'], pulumi.InputType['AzureMLUpdateResourceActivityArgs'], pulumi.InputType['ControlActivityArgs'], pulumi.InputType['CopyActivityArgs'], pulumi.InputType['CustomActivityArgs'], pulumi.InputType['DataLakeAnalyticsUSQLActivityArgs'], pulumi.InputType['DatabricksNotebookActivityArgs'], pulumi.InputType['ExecutePipelineActivityArgs'], pulumi.InputType['ExecuteSSISPackageActivityArgs'], pulumi.InputType['ExecutionActivityArgs'], pulumi.InputType['FilterActivityArgs'], pulumi.InputType['ForEachActivityArgs'], pulumi.InputType['GetMetadataActivityArgs'], pulumi.InputType['HDInsightHiveActivityArgs'], pulumi.InputType['HDInsightMapReduceActivityArgs'], pulumi.InputType['HDInsightPigActivityArgs'], pulumi.InputType['HDInsightSparkActivityArgs'], pulumi.InputType['HDInsightStreamingActivityArgs'], pulumi.InputType['IfConditionActivityArgs'], pulumi.InputType['LookupActivityArgs'], pulumi.InputType['SqlServerStoredProcedureActivityArgs'], pulumi.InputType['UntilActivityArgs'], pulumi.InputType['WaitActivityArgs'], pulumi.InputType['WebActivityArgs']]]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[Any]]] = None,
                 concurrency: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterSpecificationArgs']]]]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Pipeline resource type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AzureMLBatchExecutionActivityArgs'], pulumi.InputType['AzureMLUpdateResourceActivityArgs'], pulumi.InputType['ControlActivityArgs'], pulumi.InputType['CopyActivityArgs'], pulumi.InputType['CustomActivityArgs'], pulumi.InputType['DataLakeAnalyticsUSQLActivityArgs'], pulumi.InputType['DatabricksNotebookActivityArgs'], pulumi.InputType['ExecutePipelineActivityArgs'], pulumi.InputType['ExecuteSSISPackageActivityArgs'], pulumi.InputType['ExecutionActivityArgs'], pulumi.InputType['FilterActivityArgs'], pulumi.InputType['ForEachActivityArgs'], pulumi.InputType['GetMetadataActivityArgs'], pulumi.InputType['HDInsightHiveActivityArgs'], pulumi.InputType['HDInsightMapReduceActivityArgs'], pulumi.InputType['HDInsightPigActivityArgs'], pulumi.InputType['HDInsightSparkActivityArgs'], pulumi.InputType['HDInsightStreamingActivityArgs'], pulumi.InputType['IfConditionActivityArgs'], pulumi.InputType['LookupActivityArgs'], pulumi.InputType['SqlServerStoredProcedureActivityArgs'], pulumi.InputType['UntilActivityArgs'], pulumi.InputType['WaitActivityArgs'], pulumi.InputType['WebActivityArgs']]]]] activities: List of activities in pipeline.
        :param pulumi.Input[Sequence[Any]] annotations: List of tags that can be used for describing the Pipeline.
        :param pulumi.Input[int] concurrency: The max number of concurrent runs for the pipeline.
        :param pulumi.Input[str] description: The description of the pipeline.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterSpecificationArgs']]]] parameters: List of parameters for pipeline.
        :param pulumi.Input[str] pipeline_name: The pipeline name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Pipeline resource type.

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['AzureMLBatchExecutionActivityArgs'], pulumi.InputType['AzureMLUpdateResourceActivityArgs'], pulumi.InputType['ControlActivityArgs'], pulumi.InputType['CopyActivityArgs'], pulumi.InputType['CustomActivityArgs'], pulumi.InputType['DataLakeAnalyticsUSQLActivityArgs'], pulumi.InputType['DatabricksNotebookActivityArgs'], pulumi.InputType['ExecutePipelineActivityArgs'], pulumi.InputType['ExecuteSSISPackageActivityArgs'], pulumi.InputType['ExecutionActivityArgs'], pulumi.InputType['FilterActivityArgs'], pulumi.InputType['ForEachActivityArgs'], pulumi.InputType['GetMetadataActivityArgs'], pulumi.InputType['HDInsightHiveActivityArgs'], pulumi.InputType['HDInsightMapReduceActivityArgs'], pulumi.InputType['HDInsightPigActivityArgs'], pulumi.InputType['HDInsightSparkActivityArgs'], pulumi.InputType['HDInsightStreamingActivityArgs'], pulumi.InputType['IfConditionActivityArgs'], pulumi.InputType['LookupActivityArgs'], pulumi.InputType['SqlServerStoredProcedureActivityArgs'], pulumi.InputType['UntilActivityArgs'], pulumi.InputType['WaitActivityArgs'], pulumi.InputType['WebActivityArgs']]]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[Any]]] = None,
                 concurrency: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterSpecificationArgs']]]]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Pipeline is deprecated: Version v20170901preview will be removed in the next major version of the provider. Upgrade to version v20180601 or later.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["activities"] = activities
            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["concurrency"] = concurrency
            __props__.__dict__["description"] = description
            if factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'factory_name'")
            __props__.__dict__["factory_name"] = factory_name
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["pipeline_name"] = pipeline_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory:Pipeline"), pulumi.Alias(type_="azure-native:datafactory/v20180601:Pipeline")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pipeline, __self__).__init__(
            'azure-native:datafactory/v20170901preview:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineArgs.__new__(PipelineArgs)

        __props__.__dict__["activities"] = None
        __props__.__dict__["annotations"] = None
        __props__.__dict__["concurrency"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["type"] = None
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def activities(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        List of activities in pipeline.
        """
        return pulumi.get(self, "activities")

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        List of tags that can be used for describing the Pipeline.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def concurrency(self) -> pulumi.Output[Optional[int]]:
        """
        The max number of concurrent runs for the pipeline.
        """
        return pulumi.get(self, "concurrency")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.ParameterSpecificationResponse']]]:
        """
        List of parameters for pipeline.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

