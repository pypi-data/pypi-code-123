# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ChownMode',
    'EncryptionType',
    'EndpointType',
    'QosType',
    'ReplicationSchedule',
    'SecurityStyle',
    'ServiceLevel',
]


class ChownMode(str, Enum):
    """
    This parameter specifies who is authorized to change the ownership of a file. restricted - Only root user can change the ownership of the file. unrestricted - Non-root users can change ownership of files that they own.
    """
    RESTRICTED = "Restricted"
    UNRESTRICTED = "Unrestricted"


class EncryptionType(str, Enum):
    """
    Encryption type of the capacity pool, set encryption type for data at rest for this pool and all volumes in it. This value can only be set when creating new pool.
    """
    SINGLE = "Single"
    """
    EncryptionType Single, volumes will use single encryption at rest
    """
    DOUBLE = "Double"
    """
    EncryptionType Double, volumes will use double encryption at rest
    """


class EndpointType(str, Enum):
    """
    Indicates whether the local volume is the source or destination for the Volume Replication
    """
    SRC = "src"
    DST = "dst"


class QosType(str, Enum):
    """
    The qos type of the pool
    """
    AUTO = "Auto"
    """
    qos type Auto
    """
    MANUAL = "Manual"
    """
    qos type Manual
    """


class ReplicationSchedule(str, Enum):
    """
    Schedule
    """
    REPLICATION_SCHEDULE_10MINUTELY = "_10minutely"
    HOURLY = "hourly"
    DAILY = "daily"


class SecurityStyle(str, Enum):
    """
    The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol
    """
    NTFS = "ntfs"
    UNIX = "unix"


class ServiceLevel(str, Enum):
    """
    The service level of the file system
    """
    STANDARD = "Standard"
    """
    Standard service level
    """
    PREMIUM = "Premium"
    """
    Premium service level
    """
    ULTRA = "Ultra"
    """
    Ultra service level
    """
