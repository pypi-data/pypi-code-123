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

__all__ = [
    'GetPlaybackConfigurationResult',
    'AwaitableGetPlaybackConfigurationResult',
    'get_playback_configuration',
    'get_playback_configuration_output',
]

@pulumi.output_type
class GetPlaybackConfigurationResult:
    def __init__(__self__, ad_decision_server_url=None, avail_suppression=None, bumper=None, cdn_configuration=None, configuration_aliases=None, dash_configuration=None, hls_configuration=None, live_pre_roll_configuration=None, manifest_processing_rules=None, personalization_threshold_seconds=None, playback_configuration_arn=None, playback_endpoint_prefix=None, session_initialization_endpoint_prefix=None, slate_ad_url=None, tags=None, transcode_profile_name=None, video_content_source_url=None):
        if ad_decision_server_url and not isinstance(ad_decision_server_url, str):
            raise TypeError("Expected argument 'ad_decision_server_url' to be a str")
        pulumi.set(__self__, "ad_decision_server_url", ad_decision_server_url)
        if avail_suppression and not isinstance(avail_suppression, dict):
            raise TypeError("Expected argument 'avail_suppression' to be a dict")
        pulumi.set(__self__, "avail_suppression", avail_suppression)
        if bumper and not isinstance(bumper, dict):
            raise TypeError("Expected argument 'bumper' to be a dict")
        pulumi.set(__self__, "bumper", bumper)
        if cdn_configuration and not isinstance(cdn_configuration, dict):
            raise TypeError("Expected argument 'cdn_configuration' to be a dict")
        pulumi.set(__self__, "cdn_configuration", cdn_configuration)
        if configuration_aliases and not isinstance(configuration_aliases, dict):
            raise TypeError("Expected argument 'configuration_aliases' to be a dict")
        pulumi.set(__self__, "configuration_aliases", configuration_aliases)
        if dash_configuration and not isinstance(dash_configuration, dict):
            raise TypeError("Expected argument 'dash_configuration' to be a dict")
        pulumi.set(__self__, "dash_configuration", dash_configuration)
        if hls_configuration and not isinstance(hls_configuration, dict):
            raise TypeError("Expected argument 'hls_configuration' to be a dict")
        pulumi.set(__self__, "hls_configuration", hls_configuration)
        if live_pre_roll_configuration and not isinstance(live_pre_roll_configuration, dict):
            raise TypeError("Expected argument 'live_pre_roll_configuration' to be a dict")
        pulumi.set(__self__, "live_pre_roll_configuration", live_pre_roll_configuration)
        if manifest_processing_rules and not isinstance(manifest_processing_rules, dict):
            raise TypeError("Expected argument 'manifest_processing_rules' to be a dict")
        pulumi.set(__self__, "manifest_processing_rules", manifest_processing_rules)
        if personalization_threshold_seconds and not isinstance(personalization_threshold_seconds, int):
            raise TypeError("Expected argument 'personalization_threshold_seconds' to be a int")
        pulumi.set(__self__, "personalization_threshold_seconds", personalization_threshold_seconds)
        if playback_configuration_arn and not isinstance(playback_configuration_arn, str):
            raise TypeError("Expected argument 'playback_configuration_arn' to be a str")
        pulumi.set(__self__, "playback_configuration_arn", playback_configuration_arn)
        if playback_endpoint_prefix and not isinstance(playback_endpoint_prefix, str):
            raise TypeError("Expected argument 'playback_endpoint_prefix' to be a str")
        pulumi.set(__self__, "playback_endpoint_prefix", playback_endpoint_prefix)
        if session_initialization_endpoint_prefix and not isinstance(session_initialization_endpoint_prefix, str):
            raise TypeError("Expected argument 'session_initialization_endpoint_prefix' to be a str")
        pulumi.set(__self__, "session_initialization_endpoint_prefix", session_initialization_endpoint_prefix)
        if slate_ad_url and not isinstance(slate_ad_url, str):
            raise TypeError("Expected argument 'slate_ad_url' to be a str")
        pulumi.set(__self__, "slate_ad_url", slate_ad_url)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if transcode_profile_name and not isinstance(transcode_profile_name, str):
            raise TypeError("Expected argument 'transcode_profile_name' to be a str")
        pulumi.set(__self__, "transcode_profile_name", transcode_profile_name)
        if video_content_source_url and not isinstance(video_content_source_url, str):
            raise TypeError("Expected argument 'video_content_source_url' to be a str")
        pulumi.set(__self__, "video_content_source_url", video_content_source_url)

    @property
    @pulumi.getter(name="adDecisionServerUrl")
    def ad_decision_server_url(self) -> Optional[str]:
        """
        The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.
        """
        return pulumi.get(self, "ad_decision_server_url")

    @property
    @pulumi.getter(name="availSuppression")
    def avail_suppression(self) -> Optional['outputs.PlaybackConfigurationAvailSuppression']:
        """
        The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see Ad Suppression (https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
        """
        return pulumi.get(self, "avail_suppression")

    @property
    @pulumi.getter
    def bumper(self) -> Optional['outputs.PlaybackConfigurationBumper']:
        """
        The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see Bumpers (https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html).
        """
        return pulumi.get(self, "bumper")

    @property
    @pulumi.getter(name="cdnConfiguration")
    def cdn_configuration(self) -> Optional['outputs.PlaybackConfigurationCdnConfiguration']:
        """
        The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.
        """
        return pulumi.get(self, "cdn_configuration")

    @property
    @pulumi.getter(name="configurationAliases")
    def configuration_aliases(self) -> Optional['outputs.PlaybackConfigurationConfigurationAliases']:
        """
        The player parameters and aliases used as dynamic variables during session initialization. For more information, see Domain Variables. 
        """
        return pulumi.get(self, "configuration_aliases")

    @property
    @pulumi.getter(name="dashConfiguration")
    def dash_configuration(self) -> Optional['outputs.PlaybackConfigurationDashConfiguration']:
        """
        The configuration for DASH content.
        """
        return pulumi.get(self, "dash_configuration")

    @property
    @pulumi.getter(name="hlsConfiguration")
    def hls_configuration(self) -> Optional['outputs.PlaybackConfigurationHlsConfiguration']:
        """
        The configuration for HLS content.
        """
        return pulumi.get(self, "hls_configuration")

    @property
    @pulumi.getter(name="livePreRollConfiguration")
    def live_pre_roll_configuration(self) -> Optional['outputs.PlaybackConfigurationLivePreRollConfiguration']:
        """
        The configuration for pre-roll ad insertion.
        """
        return pulumi.get(self, "live_pre_roll_configuration")

    @property
    @pulumi.getter(name="manifestProcessingRules")
    def manifest_processing_rules(self) -> Optional['outputs.PlaybackConfigurationManifestProcessingRules']:
        """
        The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.
        """
        return pulumi.get(self, "manifest_processing_rules")

    @property
    @pulumi.getter(name="personalizationThresholdSeconds")
    def personalization_threshold_seconds(self) -> Optional[int]:
        """
        Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to ad replacement in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see Ad Behavior in AWS Elemental MediaTailor (https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).
        """
        return pulumi.get(self, "personalization_threshold_seconds")

    @property
    @pulumi.getter(name="playbackConfigurationArn")
    def playback_configuration_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the playback configuration.
        """
        return pulumi.get(self, "playback_configuration_arn")

    @property
    @pulumi.getter(name="playbackEndpointPrefix")
    def playback_endpoint_prefix(self) -> Optional[str]:
        """
        The URL that the player accesses to get a manifest from MediaTailor. This session will use server-side reporting.
        """
        return pulumi.get(self, "playback_endpoint_prefix")

    @property
    @pulumi.getter(name="sessionInitializationEndpointPrefix")
    def session_initialization_endpoint_prefix(self) -> Optional[str]:
        """
        The URL that the player uses to initialize a session that uses client-side reporting.
        """
        return pulumi.get(self, "session_initialization_endpoint_prefix")

    @property
    @pulumi.getter(name="slateAdUrl")
    def slate_ad_url(self) -> Optional[str]:
        """
        The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.
        """
        return pulumi.get(self, "slate_ad_url")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.PlaybackConfigurationTag']]:
        """
        The tags to assign to the playback configuration.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transcodeProfileName")
    def transcode_profile_name(self) -> Optional[str]:
        """
        The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.
        """
        return pulumi.get(self, "transcode_profile_name")

    @property
    @pulumi.getter(name="videoContentSourceUrl")
    def video_content_source_url(self) -> Optional[str]:
        """
        The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.
        """
        return pulumi.get(self, "video_content_source_url")


class AwaitableGetPlaybackConfigurationResult(GetPlaybackConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlaybackConfigurationResult(
            ad_decision_server_url=self.ad_decision_server_url,
            avail_suppression=self.avail_suppression,
            bumper=self.bumper,
            cdn_configuration=self.cdn_configuration,
            configuration_aliases=self.configuration_aliases,
            dash_configuration=self.dash_configuration,
            hls_configuration=self.hls_configuration,
            live_pre_roll_configuration=self.live_pre_roll_configuration,
            manifest_processing_rules=self.manifest_processing_rules,
            personalization_threshold_seconds=self.personalization_threshold_seconds,
            playback_configuration_arn=self.playback_configuration_arn,
            playback_endpoint_prefix=self.playback_endpoint_prefix,
            session_initialization_endpoint_prefix=self.session_initialization_endpoint_prefix,
            slate_ad_url=self.slate_ad_url,
            tags=self.tags,
            transcode_profile_name=self.transcode_profile_name,
            video_content_source_url=self.video_content_source_url)


def get_playback_configuration(name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlaybackConfigurationResult:
    """
    Resource schema for AWS::MediaTailor::PlaybackConfiguration


    :param str name: The identifier for the playback configuration.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:mediatailor:getPlaybackConfiguration', __args__, opts=opts, typ=GetPlaybackConfigurationResult).value

    return AwaitableGetPlaybackConfigurationResult(
        ad_decision_server_url=__ret__.ad_decision_server_url,
        avail_suppression=__ret__.avail_suppression,
        bumper=__ret__.bumper,
        cdn_configuration=__ret__.cdn_configuration,
        configuration_aliases=__ret__.configuration_aliases,
        dash_configuration=__ret__.dash_configuration,
        hls_configuration=__ret__.hls_configuration,
        live_pre_roll_configuration=__ret__.live_pre_roll_configuration,
        manifest_processing_rules=__ret__.manifest_processing_rules,
        personalization_threshold_seconds=__ret__.personalization_threshold_seconds,
        playback_configuration_arn=__ret__.playback_configuration_arn,
        playback_endpoint_prefix=__ret__.playback_endpoint_prefix,
        session_initialization_endpoint_prefix=__ret__.session_initialization_endpoint_prefix,
        slate_ad_url=__ret__.slate_ad_url,
        tags=__ret__.tags,
        transcode_profile_name=__ret__.transcode_profile_name,
        video_content_source_url=__ret__.video_content_source_url)


@_utilities.lift_output_func(get_playback_configuration)
def get_playback_configuration_output(name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlaybackConfigurationResult]:
    """
    Resource schema for AWS::MediaTailor::PlaybackConfiguration


    :param str name: The identifier for the playback configuration.
    """
    ...
