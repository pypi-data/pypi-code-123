# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ModelPackageArgs', 'ModelPackage']

@pulumi.input_type
class ModelPackageArgs:
    def __init__(__self__, *,
                 additional_inference_specification_definition: Optional[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']] = None,
                 additional_inference_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]] = None,
                 additional_inference_specifications_to_add: Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]] = None,
                 approval_description: Optional[pulumi.Input[str]] = None,
                 certify_for_marketplace: Optional[pulumi.Input[bool]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input['ModelPackageCreatedByArgs']] = None,
                 customer_metadata_properties: Optional[pulumi.Input['ModelPackageCustomerMetadataPropertiesArgs']] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 drift_check_baselines: Optional[pulumi.Input['ModelPackageDriftCheckBaselinesArgs']] = None,
                 environment: Optional[pulumi.Input['ModelPackageEnvironmentArgs']] = None,
                 inference_specification: Optional[pulumi.Input['ModelPackageInferenceSpecificationArgs']] = None,
                 last_modified_by: Optional[pulumi.Input['ModelPackageLastModifiedByArgs']] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 metadata_properties: Optional[pulumi.Input['ModelPackageMetadataPropertiesArgs']] = None,
                 model_approval_status: Optional[pulumi.Input['ModelPackageModelApprovalStatus']] = None,
                 model_metrics: Optional[pulumi.Input['ModelPackageModelMetricsArgs']] = None,
                 model_package_description: Optional[pulumi.Input[str]] = None,
                 model_package_group_name: Optional[pulumi.Input[str]] = None,
                 model_package_name: Optional[pulumi.Input[str]] = None,
                 model_package_status_details: Optional[pulumi.Input['ModelPackageStatusDetailsArgs']] = None,
                 model_package_status_item: Optional[pulumi.Input['ModelPackageStatusItemArgs']] = None,
                 model_package_version: Optional[pulumi.Input[int]] = None,
                 sample_payload_url: Optional[pulumi.Input[str]] = None,
                 source_algorithm_specification: Optional[pulumi.Input['ModelPackageSourceAlgorithmSpecificationArgs']] = None,
                 tag: Optional[pulumi.Input['ModelPackageTagArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageTagArgs']]]] = None,
                 task: Optional[pulumi.Input[str]] = None,
                 validation_specification: Optional[pulumi.Input['ModelPackageValidationSpecificationArgs']] = None):
        """
        The set of arguments for constructing a ModelPackage resource.
        :param pulumi.Input[Sequence[pulumi.Input['ModelPackageTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        if additional_inference_specification_definition is not None:
            pulumi.set(__self__, "additional_inference_specification_definition", additional_inference_specification_definition)
        if additional_inference_specifications is not None:
            pulumi.set(__self__, "additional_inference_specifications", additional_inference_specifications)
        if additional_inference_specifications_to_add is not None:
            pulumi.set(__self__, "additional_inference_specifications_to_add", additional_inference_specifications_to_add)
        if approval_description is not None:
            pulumi.set(__self__, "approval_description", approval_description)
        if certify_for_marketplace is not None:
            pulumi.set(__self__, "certify_for_marketplace", certify_for_marketplace)
        if client_token is not None:
            pulumi.set(__self__, "client_token", client_token)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if customer_metadata_properties is not None:
            pulumi.set(__self__, "customer_metadata_properties", customer_metadata_properties)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if drift_check_baselines is not None:
            pulumi.set(__self__, "drift_check_baselines", drift_check_baselines)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if inference_specification is not None:
            pulumi.set(__self__, "inference_specification", inference_specification)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_time is not None:
            pulumi.set(__self__, "last_modified_time", last_modified_time)
        if metadata_properties is not None:
            pulumi.set(__self__, "metadata_properties", metadata_properties)
        if model_approval_status is not None:
            pulumi.set(__self__, "model_approval_status", model_approval_status)
        if model_metrics is not None:
            pulumi.set(__self__, "model_metrics", model_metrics)
        if model_package_description is not None:
            pulumi.set(__self__, "model_package_description", model_package_description)
        if model_package_group_name is not None:
            pulumi.set(__self__, "model_package_group_name", model_package_group_name)
        if model_package_name is not None:
            pulumi.set(__self__, "model_package_name", model_package_name)
        if model_package_status_details is not None:
            pulumi.set(__self__, "model_package_status_details", model_package_status_details)
        if model_package_status_item is not None:
            pulumi.set(__self__, "model_package_status_item", model_package_status_item)
        if model_package_version is not None:
            pulumi.set(__self__, "model_package_version", model_package_version)
        if sample_payload_url is not None:
            pulumi.set(__self__, "sample_payload_url", sample_payload_url)
        if source_algorithm_specification is not None:
            pulumi.set(__self__, "source_algorithm_specification", source_algorithm_specification)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if task is not None:
            pulumi.set(__self__, "task", task)
        if validation_specification is not None:
            pulumi.set(__self__, "validation_specification", validation_specification)

    @property
    @pulumi.getter(name="additionalInferenceSpecificationDefinition")
    def additional_inference_specification_definition(self) -> Optional[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]:
        return pulumi.get(self, "additional_inference_specification_definition")

    @additional_inference_specification_definition.setter
    def additional_inference_specification_definition(self, value: Optional[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]):
        pulumi.set(self, "additional_inference_specification_definition", value)

    @property
    @pulumi.getter(name="additionalInferenceSpecifications")
    def additional_inference_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]:
        return pulumi.get(self, "additional_inference_specifications")

    @additional_inference_specifications.setter
    def additional_inference_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]):
        pulumi.set(self, "additional_inference_specifications", value)

    @property
    @pulumi.getter(name="additionalInferenceSpecificationsToAdd")
    def additional_inference_specifications_to_add(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]:
        return pulumi.get(self, "additional_inference_specifications_to_add")

    @additional_inference_specifications_to_add.setter
    def additional_inference_specifications_to_add(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]):
        pulumi.set(self, "additional_inference_specifications_to_add", value)

    @property
    @pulumi.getter(name="approvalDescription")
    def approval_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "approval_description")

    @approval_description.setter
    def approval_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "approval_description", value)

    @property
    @pulumi.getter(name="certifyForMarketplace")
    def certify_for_marketplace(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "certify_for_marketplace")

    @certify_for_marketplace.setter
    def certify_for_marketplace(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "certify_for_marketplace", value)

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_token")

    @client_token.setter
    def client_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_token", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input['ModelPackageCreatedByArgs']]:
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input['ModelPackageCreatedByArgs']]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="customerMetadataProperties")
    def customer_metadata_properties(self) -> Optional[pulumi.Input['ModelPackageCustomerMetadataPropertiesArgs']]:
        return pulumi.get(self, "customer_metadata_properties")

    @customer_metadata_properties.setter
    def customer_metadata_properties(self, value: Optional[pulumi.Input['ModelPackageCustomerMetadataPropertiesArgs']]):
        pulumi.set(self, "customer_metadata_properties", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="driftCheckBaselines")
    def drift_check_baselines(self) -> Optional[pulumi.Input['ModelPackageDriftCheckBaselinesArgs']]:
        return pulumi.get(self, "drift_check_baselines")

    @drift_check_baselines.setter
    def drift_check_baselines(self, value: Optional[pulumi.Input['ModelPackageDriftCheckBaselinesArgs']]):
        pulumi.set(self, "drift_check_baselines", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input['ModelPackageEnvironmentArgs']]:
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input['ModelPackageEnvironmentArgs']]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="inferenceSpecification")
    def inference_specification(self) -> Optional[pulumi.Input['ModelPackageInferenceSpecificationArgs']]:
        return pulumi.get(self, "inference_specification")

    @inference_specification.setter
    def inference_specification(self, value: Optional[pulumi.Input['ModelPackageInferenceSpecificationArgs']]):
        pulumi.set(self, "inference_specification", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input['ModelPackageLastModifiedByArgs']]:
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input['ModelPackageLastModifiedByArgs']]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "last_modified_time")

    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_time", value)

    @property
    @pulumi.getter(name="metadataProperties")
    def metadata_properties(self) -> Optional[pulumi.Input['ModelPackageMetadataPropertiesArgs']]:
        return pulumi.get(self, "metadata_properties")

    @metadata_properties.setter
    def metadata_properties(self, value: Optional[pulumi.Input['ModelPackageMetadataPropertiesArgs']]):
        pulumi.set(self, "metadata_properties", value)

    @property
    @pulumi.getter(name="modelApprovalStatus")
    def model_approval_status(self) -> Optional[pulumi.Input['ModelPackageModelApprovalStatus']]:
        return pulumi.get(self, "model_approval_status")

    @model_approval_status.setter
    def model_approval_status(self, value: Optional[pulumi.Input['ModelPackageModelApprovalStatus']]):
        pulumi.set(self, "model_approval_status", value)

    @property
    @pulumi.getter(name="modelMetrics")
    def model_metrics(self) -> Optional[pulumi.Input['ModelPackageModelMetricsArgs']]:
        return pulumi.get(self, "model_metrics")

    @model_metrics.setter
    def model_metrics(self, value: Optional[pulumi.Input['ModelPackageModelMetricsArgs']]):
        pulumi.set(self, "model_metrics", value)

    @property
    @pulumi.getter(name="modelPackageDescription")
    def model_package_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_package_description")

    @model_package_description.setter
    def model_package_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_package_description", value)

    @property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_package_group_name")

    @model_package_group_name.setter
    def model_package_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_package_group_name", value)

    @property
    @pulumi.getter(name="modelPackageName")
    def model_package_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_package_name")

    @model_package_name.setter
    def model_package_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_package_name", value)

    @property
    @pulumi.getter(name="modelPackageStatusDetails")
    def model_package_status_details(self) -> Optional[pulumi.Input['ModelPackageStatusDetailsArgs']]:
        return pulumi.get(self, "model_package_status_details")

    @model_package_status_details.setter
    def model_package_status_details(self, value: Optional[pulumi.Input['ModelPackageStatusDetailsArgs']]):
        pulumi.set(self, "model_package_status_details", value)

    @property
    @pulumi.getter(name="modelPackageStatusItem")
    def model_package_status_item(self) -> Optional[pulumi.Input['ModelPackageStatusItemArgs']]:
        return pulumi.get(self, "model_package_status_item")

    @model_package_status_item.setter
    def model_package_status_item(self, value: Optional[pulumi.Input['ModelPackageStatusItemArgs']]):
        pulumi.set(self, "model_package_status_item", value)

    @property
    @pulumi.getter(name="modelPackageVersion")
    def model_package_version(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "model_package_version")

    @model_package_version.setter
    def model_package_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "model_package_version", value)

    @property
    @pulumi.getter(name="samplePayloadUrl")
    def sample_payload_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sample_payload_url")

    @sample_payload_url.setter
    def sample_payload_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sample_payload_url", value)

    @property
    @pulumi.getter(name="sourceAlgorithmSpecification")
    def source_algorithm_specification(self) -> Optional[pulumi.Input['ModelPackageSourceAlgorithmSpecificationArgs']]:
        return pulumi.get(self, "source_algorithm_specification")

    @source_algorithm_specification.setter
    def source_algorithm_specification(self, value: Optional[pulumi.Input['ModelPackageSourceAlgorithmSpecificationArgs']]):
        pulumi.set(self, "source_algorithm_specification", value)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input['ModelPackageTagArgs']]:
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input['ModelPackageTagArgs']]):
        pulumi.set(self, "tag", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ModelPackageTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def task(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "task")

    @task.setter
    def task(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "task", value)

    @property
    @pulumi.getter(name="validationSpecification")
    def validation_specification(self) -> Optional[pulumi.Input['ModelPackageValidationSpecificationArgs']]:
        return pulumi.get(self, "validation_specification")

    @validation_specification.setter
    def validation_specification(self, value: Optional[pulumi.Input['ModelPackageValidationSpecificationArgs']]):
        pulumi.set(self, "validation_specification", value)


class ModelPackage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_inference_specification_definition: Optional[pulumi.Input[pulumi.InputType['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]] = None,
                 additional_inference_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]] = None,
                 additional_inference_specifications_to_add: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]] = None,
                 approval_description: Optional[pulumi.Input[str]] = None,
                 certify_for_marketplace: Optional[pulumi.Input[bool]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[pulumi.InputType['ModelPackageCreatedByArgs']]] = None,
                 customer_metadata_properties: Optional[pulumi.Input[pulumi.InputType['ModelPackageCustomerMetadataPropertiesArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 drift_check_baselines: Optional[pulumi.Input[pulumi.InputType['ModelPackageDriftCheckBaselinesArgs']]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['ModelPackageEnvironmentArgs']]] = None,
                 inference_specification: Optional[pulumi.Input[pulumi.InputType['ModelPackageInferenceSpecificationArgs']]] = None,
                 last_modified_by: Optional[pulumi.Input[pulumi.InputType['ModelPackageLastModifiedByArgs']]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 metadata_properties: Optional[pulumi.Input[pulumi.InputType['ModelPackageMetadataPropertiesArgs']]] = None,
                 model_approval_status: Optional[pulumi.Input['ModelPackageModelApprovalStatus']] = None,
                 model_metrics: Optional[pulumi.Input[pulumi.InputType['ModelPackageModelMetricsArgs']]] = None,
                 model_package_description: Optional[pulumi.Input[str]] = None,
                 model_package_group_name: Optional[pulumi.Input[str]] = None,
                 model_package_name: Optional[pulumi.Input[str]] = None,
                 model_package_status_details: Optional[pulumi.Input[pulumi.InputType['ModelPackageStatusDetailsArgs']]] = None,
                 model_package_status_item: Optional[pulumi.Input[pulumi.InputType['ModelPackageStatusItemArgs']]] = None,
                 model_package_version: Optional[pulumi.Input[int]] = None,
                 sample_payload_url: Optional[pulumi.Input[str]] = None,
                 source_algorithm_specification: Optional[pulumi.Input[pulumi.InputType['ModelPackageSourceAlgorithmSpecificationArgs']]] = None,
                 tag: Optional[pulumi.Input[pulumi.InputType['ModelPackageTagArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageTagArgs']]]]] = None,
                 task: Optional[pulumi.Input[str]] = None,
                 validation_specification: Optional[pulumi.Input[pulumi.InputType['ModelPackageValidationSpecificationArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::ModelPackage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ModelPackageArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::ModelPackage

        :param str resource_name: The name of the resource.
        :param ModelPackageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModelPackageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_inference_specification_definition: Optional[pulumi.Input[pulumi.InputType['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]] = None,
                 additional_inference_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]] = None,
                 additional_inference_specifications_to_add: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageAdditionalInferenceSpecificationDefinitionArgs']]]]] = None,
                 approval_description: Optional[pulumi.Input[str]] = None,
                 certify_for_marketplace: Optional[pulumi.Input[bool]] = None,
                 client_token: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[pulumi.InputType['ModelPackageCreatedByArgs']]] = None,
                 customer_metadata_properties: Optional[pulumi.Input[pulumi.InputType['ModelPackageCustomerMetadataPropertiesArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 drift_check_baselines: Optional[pulumi.Input[pulumi.InputType['ModelPackageDriftCheckBaselinesArgs']]] = None,
                 environment: Optional[pulumi.Input[pulumi.InputType['ModelPackageEnvironmentArgs']]] = None,
                 inference_specification: Optional[pulumi.Input[pulumi.InputType['ModelPackageInferenceSpecificationArgs']]] = None,
                 last_modified_by: Optional[pulumi.Input[pulumi.InputType['ModelPackageLastModifiedByArgs']]] = None,
                 last_modified_time: Optional[pulumi.Input[str]] = None,
                 metadata_properties: Optional[pulumi.Input[pulumi.InputType['ModelPackageMetadataPropertiesArgs']]] = None,
                 model_approval_status: Optional[pulumi.Input['ModelPackageModelApprovalStatus']] = None,
                 model_metrics: Optional[pulumi.Input[pulumi.InputType['ModelPackageModelMetricsArgs']]] = None,
                 model_package_description: Optional[pulumi.Input[str]] = None,
                 model_package_group_name: Optional[pulumi.Input[str]] = None,
                 model_package_name: Optional[pulumi.Input[str]] = None,
                 model_package_status_details: Optional[pulumi.Input[pulumi.InputType['ModelPackageStatusDetailsArgs']]] = None,
                 model_package_status_item: Optional[pulumi.Input[pulumi.InputType['ModelPackageStatusItemArgs']]] = None,
                 model_package_version: Optional[pulumi.Input[int]] = None,
                 sample_payload_url: Optional[pulumi.Input[str]] = None,
                 source_algorithm_specification: Optional[pulumi.Input[pulumi.InputType['ModelPackageSourceAlgorithmSpecificationArgs']]] = None,
                 tag: Optional[pulumi.Input[pulumi.InputType['ModelPackageTagArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ModelPackageTagArgs']]]]] = None,
                 task: Optional[pulumi.Input[str]] = None,
                 validation_specification: Optional[pulumi.Input[pulumi.InputType['ModelPackageValidationSpecificationArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModelPackageArgs.__new__(ModelPackageArgs)

            __props__.__dict__["additional_inference_specification_definition"] = additional_inference_specification_definition
            __props__.__dict__["additional_inference_specifications"] = additional_inference_specifications
            __props__.__dict__["additional_inference_specifications_to_add"] = additional_inference_specifications_to_add
            __props__.__dict__["approval_description"] = approval_description
            __props__.__dict__["certify_for_marketplace"] = certify_for_marketplace
            __props__.__dict__["client_token"] = client_token
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["customer_metadata_properties"] = customer_metadata_properties
            __props__.__dict__["domain"] = domain
            __props__.__dict__["drift_check_baselines"] = drift_check_baselines
            __props__.__dict__["environment"] = environment
            __props__.__dict__["inference_specification"] = inference_specification
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["last_modified_time"] = last_modified_time
            __props__.__dict__["metadata_properties"] = metadata_properties
            __props__.__dict__["model_approval_status"] = model_approval_status
            __props__.__dict__["model_metrics"] = model_metrics
            __props__.__dict__["model_package_description"] = model_package_description
            __props__.__dict__["model_package_group_name"] = model_package_group_name
            __props__.__dict__["model_package_name"] = model_package_name
            __props__.__dict__["model_package_status_details"] = model_package_status_details
            __props__.__dict__["model_package_status_item"] = model_package_status_item
            __props__.__dict__["model_package_version"] = model_package_version
            __props__.__dict__["sample_payload_url"] = sample_payload_url
            __props__.__dict__["source_algorithm_specification"] = source_algorithm_specification
            __props__.__dict__["tag"] = tag
            __props__.__dict__["tags"] = tags
            __props__.__dict__["task"] = task
            __props__.__dict__["validation_specification"] = validation_specification
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["model_package_arn"] = None
            __props__.__dict__["model_package_status"] = None
        super(ModelPackage, __self__).__init__(
            'aws-native:sagemaker:ModelPackage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ModelPackage':
        """
        Get an existing ModelPackage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModelPackageArgs.__new__(ModelPackageArgs)

        __props__.__dict__["additional_inference_specification_definition"] = None
        __props__.__dict__["additional_inference_specifications"] = None
        __props__.__dict__["additional_inference_specifications_to_add"] = None
        __props__.__dict__["approval_description"] = None
        __props__.__dict__["certify_for_marketplace"] = None
        __props__.__dict__["client_token"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["customer_metadata_properties"] = None
        __props__.__dict__["domain"] = None
        __props__.__dict__["drift_check_baselines"] = None
        __props__.__dict__["environment"] = None
        __props__.__dict__["inference_specification"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["metadata_properties"] = None
        __props__.__dict__["model_approval_status"] = None
        __props__.__dict__["model_metrics"] = None
        __props__.__dict__["model_package_arn"] = None
        __props__.__dict__["model_package_description"] = None
        __props__.__dict__["model_package_group_name"] = None
        __props__.__dict__["model_package_name"] = None
        __props__.__dict__["model_package_status"] = None
        __props__.__dict__["model_package_status_details"] = None
        __props__.__dict__["model_package_status_item"] = None
        __props__.__dict__["model_package_version"] = None
        __props__.__dict__["sample_payload_url"] = None
        __props__.__dict__["source_algorithm_specification"] = None
        __props__.__dict__["tag"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["task"] = None
        __props__.__dict__["validation_specification"] = None
        return ModelPackage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalInferenceSpecificationDefinition")
    def additional_inference_specification_definition(self) -> pulumi.Output[Optional['outputs.ModelPackageAdditionalInferenceSpecificationDefinition']]:
        return pulumi.get(self, "additional_inference_specification_definition")

    @property
    @pulumi.getter(name="additionalInferenceSpecifications")
    def additional_inference_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.ModelPackageAdditionalInferenceSpecificationDefinition']]]:
        return pulumi.get(self, "additional_inference_specifications")

    @property
    @pulumi.getter(name="additionalInferenceSpecificationsToAdd")
    def additional_inference_specifications_to_add(self) -> pulumi.Output[Optional[Sequence['outputs.ModelPackageAdditionalInferenceSpecificationDefinition']]]:
        return pulumi.get(self, "additional_inference_specifications_to_add")

    @property
    @pulumi.getter(name="approvalDescription")
    def approval_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "approval_description")

    @property
    @pulumi.getter(name="certifyForMarketplace")
    def certify_for_marketplace(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "certify_for_marketplace")

    @property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "client_token")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional['outputs.ModelPackageCreatedBy']]:
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customerMetadataProperties")
    def customer_metadata_properties(self) -> pulumi.Output[Optional['outputs.ModelPackageCustomerMetadataProperties']]:
        return pulumi.get(self, "customer_metadata_properties")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="driftCheckBaselines")
    def drift_check_baselines(self) -> pulumi.Output[Optional['outputs.ModelPackageDriftCheckBaselines']]:
        return pulumi.get(self, "drift_check_baselines")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional['outputs.ModelPackageEnvironment']]:
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="inferenceSpecification")
    def inference_specification(self) -> pulumi.Output[Optional['outputs.ModelPackageInferenceSpecification']]:
        return pulumi.get(self, "inference_specification")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional['outputs.ModelPackageLastModifiedBy']]:
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="metadataProperties")
    def metadata_properties(self) -> pulumi.Output[Optional['outputs.ModelPackageMetadataProperties']]:
        return pulumi.get(self, "metadata_properties")

    @property
    @pulumi.getter(name="modelApprovalStatus")
    def model_approval_status(self) -> pulumi.Output[Optional['ModelPackageModelApprovalStatus']]:
        return pulumi.get(self, "model_approval_status")

    @property
    @pulumi.getter(name="modelMetrics")
    def model_metrics(self) -> pulumi.Output[Optional['outputs.ModelPackageModelMetrics']]:
        return pulumi.get(self, "model_metrics")

    @property
    @pulumi.getter(name="modelPackageArn")
    def model_package_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "model_package_arn")

    @property
    @pulumi.getter(name="modelPackageDescription")
    def model_package_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_package_description")

    @property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_package_group_name")

    @property
    @pulumi.getter(name="modelPackageName")
    def model_package_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_package_name")

    @property
    @pulumi.getter(name="modelPackageStatus")
    def model_package_status(self) -> pulumi.Output['ModelPackageStatus']:
        return pulumi.get(self, "model_package_status")

    @property
    @pulumi.getter(name="modelPackageStatusDetails")
    def model_package_status_details(self) -> pulumi.Output[Optional['outputs.ModelPackageStatusDetails']]:
        return pulumi.get(self, "model_package_status_details")

    @property
    @pulumi.getter(name="modelPackageStatusItem")
    def model_package_status_item(self) -> pulumi.Output[Optional['outputs.ModelPackageStatusItem']]:
        return pulumi.get(self, "model_package_status_item")

    @property
    @pulumi.getter(name="modelPackageVersion")
    def model_package_version(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "model_package_version")

    @property
    @pulumi.getter(name="samplePayloadUrl")
    def sample_payload_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sample_payload_url")

    @property
    @pulumi.getter(name="sourceAlgorithmSpecification")
    def source_algorithm_specification(self) -> pulumi.Output[Optional['outputs.ModelPackageSourceAlgorithmSpecification']]:
        return pulumi.get(self, "source_algorithm_specification")

    @property
    @pulumi.getter
    def tag(self) -> pulumi.Output[Optional['outputs.ModelPackageTag']]:
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ModelPackageTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def task(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "task")

    @property
    @pulumi.getter(name="validationSpecification")
    def validation_specification(self) -> pulumi.Output[Optional['outputs.ModelPackageValidationSpecification']]:
        return pulumi.get(self, "validation_specification")

