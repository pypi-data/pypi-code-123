# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AddressType',
    'ClassDiscriminator',
    'DataDestinationType',
    'NotificationStageName',
    'SkuName',
]


class AddressType(str, Enum):
    """
    Type of address.
    """
    NONE = "None"
    """
    Address type not known.
    """
    RESIDENTIAL = "Residential"
    """
    Residential Address.
    """
    COMMERCIAL = "Commercial"
    """
    Commercial Address.
    """


class ClassDiscriminator(str, Enum):
    """
    Indicates the type of job details.
    """
    DATA_BOX = "DataBox"
    """
    DataBox orders.
    """
    DATA_BOX_DISK = "DataBoxDisk"
    """
    DataBoxDisk orders.
    """
    DATA_BOX_HEAVY = "DataBoxHeavy"
    """
    DataBoxHeavy orders.
    """


class DataDestinationType(str, Enum):
    """
    Data Destination Type.
    """
    UNKNOWN_TYPE = "UnknownType"
    """
    Unknown type.
    """
    STORAGE_ACCOUNT = "StorageAccount"
    """
    Storage Accounts .
    """
    MANAGED_DISK = "ManagedDisk"
    """
    Azure Managed disk storage.
    """


class NotificationStageName(str, Enum):
    """
    Name of the stage.
    """
    DEVICE_PREPARED = "DevicePrepared"
    """
    Notification at device prepared stage.
    """
    DISPATCHED = "Dispatched"
    """
    Notification at device dispatched stage.
    """
    DELIVERED = "Delivered"
    """
    Notification at device delivered stage.
    """
    PICKED_UP = "PickedUp"
    """
    Notification at device picked up from user stage.
    """
    AT_AZURE_DC = "AtAzureDC"
    """
    Notification at device received at azure datacenter stage.
    """
    DATA_COPY = "DataCopy"
    """
    Notification at data copy started stage.
    """


class SkuName(str, Enum):
    """
    The sku name.
    """
    DATA_BOX = "DataBox"
    """
    DataBox.
    """
    DATA_BOX_DISK = "DataBoxDisk"
    """
    DataBoxDisk.
    """
    DATA_BOX_HEAVY = "DataBoxHeavy"
    """
    DataBoxHeavy.
    """
