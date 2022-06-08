# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from .get_suppression import *
from .suppression import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.advisor.v20160712preview as __v20160712preview
    v20160712preview = __v20160712preview
    import pulumi_azure_native.advisor.v20170331 as __v20170331
    v20170331 = __v20170331
    import pulumi_azure_native.advisor.v20170419 as __v20170419
    v20170419 = __v20170419
    import pulumi_azure_native.advisor.v20200101 as __v20200101
    v20200101 = __v20200101
else:
    v20160712preview = _utilities.lazy_import('pulumi_azure_native.advisor.v20160712preview')
    v20170331 = _utilities.lazy_import('pulumi_azure_native.advisor.v20170331')
    v20170419 = _utilities.lazy_import('pulumi_azure_native.advisor.v20170419')
    v20200101 = _utilities.lazy_import('pulumi_azure_native.advisor.v20200101')

