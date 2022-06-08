# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['StreamProcessorArgs', 'StreamProcessor']

@pulumi.input_type
class StreamProcessorArgs:
    def __init__(__self__, *,
                 kinesis_video_stream: pulumi.Input['StreamProcessorKinesisVideoStreamArgs'],
                 role_arn: pulumi.Input[str],
                 bounding_box_regions_of_interest: Optional[pulumi.Input[Sequence[pulumi.Input['StreamProcessorBoundingBoxArgs']]]] = None,
                 connected_home_settings: Optional[pulumi.Input['StreamProcessorConnectedHomeSettingsArgs']] = None,
                 data_sharing_preference: Optional[pulumi.Input['StreamProcessorDataSharingPreferenceArgs']] = None,
                 face_search_settings: Optional[pulumi.Input['StreamProcessorFaceSearchSettingsArgs']] = None,
                 kinesis_data_stream: Optional[pulumi.Input['StreamProcessorKinesisDataStreamArgs']] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_channel: Optional[pulumi.Input['StreamProcessorNotificationChannelArgs']] = None,
                 polygon_regions_of_interest: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['StreamProcessorPointArgs']]]]]] = None,
                 s3_destination: Optional[pulumi.Input['StreamProcessorS3DestinationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StreamProcessorTagArgs']]]] = None):
        """
        The set of arguments for constructing a StreamProcessor resource.
        :param pulumi.Input[str] role_arn: ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
        :param pulumi.Input[Sequence[pulumi.Input['StreamProcessorBoundingBoxArgs']]] bounding_box_regions_of_interest: The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
        :param pulumi.Input[str] kms_key_id: The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
        :param pulumi.Input[str] name: Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
        :param pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['StreamProcessorPointArgs']]]]] polygon_regions_of_interest: The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
        :param pulumi.Input[Sequence[pulumi.Input['StreamProcessorTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "kinesis_video_stream", kinesis_video_stream)
        pulumi.set(__self__, "role_arn", role_arn)
        if bounding_box_regions_of_interest is not None:
            pulumi.set(__self__, "bounding_box_regions_of_interest", bounding_box_regions_of_interest)
        if connected_home_settings is not None:
            pulumi.set(__self__, "connected_home_settings", connected_home_settings)
        if data_sharing_preference is not None:
            pulumi.set(__self__, "data_sharing_preference", data_sharing_preference)
        if face_search_settings is not None:
            pulumi.set(__self__, "face_search_settings", face_search_settings)
        if kinesis_data_stream is not None:
            pulumi.set(__self__, "kinesis_data_stream", kinesis_data_stream)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if notification_channel is not None:
            pulumi.set(__self__, "notification_channel", notification_channel)
        if polygon_regions_of_interest is not None:
            pulumi.set(__self__, "polygon_regions_of_interest", polygon_regions_of_interest)
        if s3_destination is not None:
            pulumi.set(__self__, "s3_destination", s3_destination)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="kinesisVideoStream")
    def kinesis_video_stream(self) -> pulumi.Input['StreamProcessorKinesisVideoStreamArgs']:
        return pulumi.get(self, "kinesis_video_stream")

    @kinesis_video_stream.setter
    def kinesis_video_stream(self, value: pulumi.Input['StreamProcessorKinesisVideoStreamArgs']):
        pulumi.set(self, "kinesis_video_stream", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="boundingBoxRegionsOfInterest")
    def bounding_box_regions_of_interest(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StreamProcessorBoundingBoxArgs']]]]:
        """
        The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
        """
        return pulumi.get(self, "bounding_box_regions_of_interest")

    @bounding_box_regions_of_interest.setter
    def bounding_box_regions_of_interest(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StreamProcessorBoundingBoxArgs']]]]):
        pulumi.set(self, "bounding_box_regions_of_interest", value)

    @property
    @pulumi.getter(name="connectedHomeSettings")
    def connected_home_settings(self) -> Optional[pulumi.Input['StreamProcessorConnectedHomeSettingsArgs']]:
        return pulumi.get(self, "connected_home_settings")

    @connected_home_settings.setter
    def connected_home_settings(self, value: Optional[pulumi.Input['StreamProcessorConnectedHomeSettingsArgs']]):
        pulumi.set(self, "connected_home_settings", value)

    @property
    @pulumi.getter(name="dataSharingPreference")
    def data_sharing_preference(self) -> Optional[pulumi.Input['StreamProcessorDataSharingPreferenceArgs']]:
        return pulumi.get(self, "data_sharing_preference")

    @data_sharing_preference.setter
    def data_sharing_preference(self, value: Optional[pulumi.Input['StreamProcessorDataSharingPreferenceArgs']]):
        pulumi.set(self, "data_sharing_preference", value)

    @property
    @pulumi.getter(name="faceSearchSettings")
    def face_search_settings(self) -> Optional[pulumi.Input['StreamProcessorFaceSearchSettingsArgs']]:
        return pulumi.get(self, "face_search_settings")

    @face_search_settings.setter
    def face_search_settings(self, value: Optional[pulumi.Input['StreamProcessorFaceSearchSettingsArgs']]):
        pulumi.set(self, "face_search_settings", value)

    @property
    @pulumi.getter(name="kinesisDataStream")
    def kinesis_data_stream(self) -> Optional[pulumi.Input['StreamProcessorKinesisDataStreamArgs']]:
        return pulumi.get(self, "kinesis_data_stream")

    @kinesis_data_stream.setter
    def kinesis_data_stream(self, value: Optional[pulumi.Input['StreamProcessorKinesisDataStreamArgs']]):
        pulumi.set(self, "kinesis_data_stream", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notificationChannel")
    def notification_channel(self) -> Optional[pulumi.Input['StreamProcessorNotificationChannelArgs']]:
        return pulumi.get(self, "notification_channel")

    @notification_channel.setter
    def notification_channel(self, value: Optional[pulumi.Input['StreamProcessorNotificationChannelArgs']]):
        pulumi.set(self, "notification_channel", value)

    @property
    @pulumi.getter(name="polygonRegionsOfInterest")
    def polygon_regions_of_interest(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['StreamProcessorPointArgs']]]]]]:
        """
        The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
        """
        return pulumi.get(self, "polygon_regions_of_interest")

    @polygon_regions_of_interest.setter
    def polygon_regions_of_interest(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input['StreamProcessorPointArgs']]]]]]):
        pulumi.set(self, "polygon_regions_of_interest", value)

    @property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> Optional[pulumi.Input['StreamProcessorS3DestinationArgs']]:
        return pulumi.get(self, "s3_destination")

    @s3_destination.setter
    def s3_destination(self, value: Optional[pulumi.Input['StreamProcessorS3DestinationArgs']]):
        pulumi.set(self, "s3_destination", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StreamProcessorTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StreamProcessorTagArgs']]]]):
        pulumi.set(self, "tags", value)


class StreamProcessor(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bounding_box_regions_of_interest: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorBoundingBoxArgs']]]]] = None,
                 connected_home_settings: Optional[pulumi.Input[pulumi.InputType['StreamProcessorConnectedHomeSettingsArgs']]] = None,
                 data_sharing_preference: Optional[pulumi.Input[pulumi.InputType['StreamProcessorDataSharingPreferenceArgs']]] = None,
                 face_search_settings: Optional[pulumi.Input[pulumi.InputType['StreamProcessorFaceSearchSettingsArgs']]] = None,
                 kinesis_data_stream: Optional[pulumi.Input[pulumi.InputType['StreamProcessorKinesisDataStreamArgs']]] = None,
                 kinesis_video_stream: Optional[pulumi.Input[pulumi.InputType['StreamProcessorKinesisVideoStreamArgs']]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_channel: Optional[pulumi.Input[pulumi.InputType['StreamProcessorNotificationChannelArgs']]] = None,
                 polygon_regions_of_interest: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorPointArgs']]]]]]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 s3_destination: Optional[pulumi.Input[pulumi.InputType['StreamProcessorS3DestinationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorBoundingBoxArgs']]]] bounding_box_regions_of_interest: The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
        :param pulumi.Input[str] kms_key_id: The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
        :param pulumi.Input[str] name: Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
        :param pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorPointArgs']]]]]] polygon_regions_of_interest: The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
        :param pulumi.Input[str] role_arn: ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StreamProcessorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Rekognition::StreamProcessor type is used to create an Amazon Rekognition StreamProcessor that you can use to analyze streaming videos.

        :param str resource_name: The name of the resource.
        :param StreamProcessorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamProcessorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bounding_box_regions_of_interest: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorBoundingBoxArgs']]]]] = None,
                 connected_home_settings: Optional[pulumi.Input[pulumi.InputType['StreamProcessorConnectedHomeSettingsArgs']]] = None,
                 data_sharing_preference: Optional[pulumi.Input[pulumi.InputType['StreamProcessorDataSharingPreferenceArgs']]] = None,
                 face_search_settings: Optional[pulumi.Input[pulumi.InputType['StreamProcessorFaceSearchSettingsArgs']]] = None,
                 kinesis_data_stream: Optional[pulumi.Input[pulumi.InputType['StreamProcessorKinesisDataStreamArgs']]] = None,
                 kinesis_video_stream: Optional[pulumi.Input[pulumi.InputType['StreamProcessorKinesisVideoStreamArgs']]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_channel: Optional[pulumi.Input[pulumi.InputType['StreamProcessorNotificationChannelArgs']]] = None,
                 polygon_regions_of_interest: Optional[pulumi.Input[Sequence[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorPointArgs']]]]]]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 s3_destination: Optional[pulumi.Input[pulumi.InputType['StreamProcessorS3DestinationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StreamProcessorTagArgs']]]]] = None,
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
            __props__ = StreamProcessorArgs.__new__(StreamProcessorArgs)

            __props__.__dict__["bounding_box_regions_of_interest"] = bounding_box_regions_of_interest
            __props__.__dict__["connected_home_settings"] = connected_home_settings
            __props__.__dict__["data_sharing_preference"] = data_sharing_preference
            __props__.__dict__["face_search_settings"] = face_search_settings
            __props__.__dict__["kinesis_data_stream"] = kinesis_data_stream
            if kinesis_video_stream is None and not opts.urn:
                raise TypeError("Missing required property 'kinesis_video_stream'")
            __props__.__dict__["kinesis_video_stream"] = kinesis_video_stream
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["name"] = name
            __props__.__dict__["notification_channel"] = notification_channel
            __props__.__dict__["polygon_regions_of_interest"] = polygon_regions_of_interest
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["s3_destination"] = s3_destination
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
        super(StreamProcessor, __self__).__init__(
            'aws-native:rekognition:StreamProcessor',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StreamProcessor':
        """
        Get an existing StreamProcessor resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StreamProcessorArgs.__new__(StreamProcessorArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["bounding_box_regions_of_interest"] = None
        __props__.__dict__["connected_home_settings"] = None
        __props__.__dict__["data_sharing_preference"] = None
        __props__.__dict__["face_search_settings"] = None
        __props__.__dict__["kinesis_data_stream"] = None
        __props__.__dict__["kinesis_video_stream"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notification_channel"] = None
        __props__.__dict__["polygon_regions_of_interest"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["s3_destination"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["tags"] = None
        return StreamProcessor(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="boundingBoxRegionsOfInterest")
    def bounding_box_regions_of_interest(self) -> pulumi.Output[Optional[Sequence['outputs.StreamProcessorBoundingBox']]]:
        """
        The BoundingBoxRegionsOfInterest specifies an array of bounding boxes of interest in the video frames to analyze, as part of connected home feature. If an object is partially in a region of interest, Rekognition will tag it as detected if the overlap of the object with the region-of-interest is greater than 20%.
        """
        return pulumi.get(self, "bounding_box_regions_of_interest")

    @property
    @pulumi.getter(name="connectedHomeSettings")
    def connected_home_settings(self) -> pulumi.Output[Optional['outputs.StreamProcessorConnectedHomeSettings']]:
        return pulumi.get(self, "connected_home_settings")

    @property
    @pulumi.getter(name="dataSharingPreference")
    def data_sharing_preference(self) -> pulumi.Output[Optional['outputs.StreamProcessorDataSharingPreference']]:
        return pulumi.get(self, "data_sharing_preference")

    @property
    @pulumi.getter(name="faceSearchSettings")
    def face_search_settings(self) -> pulumi.Output[Optional['outputs.StreamProcessorFaceSearchSettings']]:
        return pulumi.get(self, "face_search_settings")

    @property
    @pulumi.getter(name="kinesisDataStream")
    def kinesis_data_stream(self) -> pulumi.Output[Optional['outputs.StreamProcessorKinesisDataStream']]:
        return pulumi.get(self, "kinesis_data_stream")

    @property
    @pulumi.getter(name="kinesisVideoStream")
    def kinesis_video_stream(self) -> pulumi.Output['outputs.StreamProcessorKinesisVideoStream']:
        return pulumi.get(self, "kinesis_video_stream")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The KMS key that is used by Rekognition to encrypt any intermediate customer metadata and store in the customer's S3 bucket.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationChannel")
    def notification_channel(self) -> pulumi.Output[Optional['outputs.StreamProcessorNotificationChannel']]:
        return pulumi.get(self, "notification_channel")

    @property
    @pulumi.getter(name="polygonRegionsOfInterest")
    def polygon_regions_of_interest(self) -> pulumi.Output[Optional[Sequence[Sequence['outputs.StreamProcessorPoint']]]]:
        """
        The PolygonRegionsOfInterest specifies a set of polygon areas of interest in the video frames to analyze, as part of connected home feature. Each polygon is in turn, an ordered list of Point
        """
        return pulumi.get(self, "polygon_regions_of_interest")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        ARN of the IAM role that allows access to the stream processor, and provides Rekognition read permissions for KVS stream and write permissions to S3 bucket and SNS topic.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> pulumi.Output[Optional['outputs.StreamProcessorS3Destination']]:
        return pulumi.get(self, "s3_destination")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Current status of the stream processor.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        Detailed status message about the stream processor.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StreamProcessorTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

