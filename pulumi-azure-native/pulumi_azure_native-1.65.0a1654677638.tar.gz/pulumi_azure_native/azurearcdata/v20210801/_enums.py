# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ArcSqlManagedInstanceLicenseType',
    'ArcSqlServerLicenseType',
    'ConnectionStatus',
    'DefenderStatus',
    'EditionType',
    'ExtendedLocationTypes',
    'Infrastructure',
    'SqlManagedInstanceSkuTier',
    'SqlVersion',
]


class ArcSqlManagedInstanceLicenseType(str, Enum):
    """
    The license type to apply for this managed instance.
    """
    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"


class ArcSqlServerLicenseType(str, Enum):
    """
    SQL Server license type.
    """
    PAID = "Paid"
    FREE = "Free"
    HADR = "HADR"
    UNDEFINED = "Undefined"


class ConnectionStatus(str, Enum):
    """
    The cloud connectivity status.
    """
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    UNKNOWN = "Unknown"


class DefenderStatus(str, Enum):
    """
    Status of Azure Defender.
    """
    PROTECTED = "Protected"
    UNPROTECTED = "Unprotected"
    UNKNOWN = "Unknown"


class EditionType(str, Enum):
    """
    SQL Server edition.
    """
    EVALUATION = "Evaluation"
    ENTERPRISE = "Enterprise"
    STANDARD = "Standard"
    WEB = "Web"
    DEVELOPER = "Developer"
    EXPRESS = "Express"


class ExtendedLocationTypes(str, Enum):
    """
    The type of the extended location.
    """
    CUSTOM_LOCATION = "CustomLocation"


class Infrastructure(str, Enum):
    """
    The infrastructure the data controller is running on.
    """
    AZURE = "azure"
    GCP = "gcp"
    AWS = "aws"
    ALIBABA = "alibaba"
    ONPREMISES = "onpremises"
    OTHER = "other"


class SqlManagedInstanceSkuTier(str, Enum):
    """
    The pricing tier for the instance.
    """
    GENERAL_PURPOSE = "GeneralPurpose"
    BUSINESS_CRITICAL = "BusinessCritical"


class SqlVersion(str, Enum):
    """
    SQL Server version.
    """
    SQ_L_SERVER_2019 = "SQL Server 2019"
    SQ_L_SERVER_2017 = "SQL Server 2017"
    SQ_L_SERVER_2016 = "SQL Server 2016"
