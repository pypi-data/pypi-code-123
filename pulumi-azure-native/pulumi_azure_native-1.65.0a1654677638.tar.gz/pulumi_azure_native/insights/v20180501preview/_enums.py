# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationType',
    'FlowType',
    'IngestionMode',
    'PublicNetworkAccessType',
    'RequestSource',
    'WebTestKind',
    'WebTestKindEnum',
]


class ApplicationType(str, Enum):
    """
    Type of application being monitored.
    """
    WEB = "web"
    OTHER = "other"


class FlowType(str, Enum):
    """
    Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API.
    """
    BLUEFIELD = "Bluefield"


class IngestionMode(str, Enum):
    """
    Indicates the flow of the ingestion.
    """
    APPLICATION_INSIGHTS = "ApplicationInsights"
    APPLICATION_INSIGHTS_WITH_DIAGNOSTIC_SETTINGS = "ApplicationInsightsWithDiagnosticSettings"
    LOG_ANALYTICS = "LogAnalytics"


class PublicNetworkAccessType(str, Enum):
    """
    The network access type for accessing Application Insights query.
    """
    ENABLED = "Enabled"
    """
    Enables connectivity to Application Insights through public DNS.
    """
    DISABLED = "Disabled"
    """
    Disables public connectivity to Application Insights through public DNS.
    """


class RequestSource(str, Enum):
    """
    Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'.
    """
    REST = "rest"


class WebTestKind(str, Enum):
    """
    The kind of WebTest that this web test watches. Choices are ping and multistep.
    """
    PING = "ping"
    MULTISTEP = "multistep"


class WebTestKindEnum(str, Enum):
    """
    The kind of web test this is, valid choices are ping, multistep, basic, and standard.
    """
    PING = "ping"
    MULTISTEP = "multistep"
    BASIC = "basic"
    STANDARD = "standard"
