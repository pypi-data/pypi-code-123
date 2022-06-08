# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PaginatedProfileResponseList(Model):
    """A paginated list of ProfileResponses.

    :param value: An array of objects of type ProfileResponse.
    :type value: list[~_restclient.models.ProfileResponse]
    :param continuation_token: The token used in retrieving the next page. If
     null, there are no additional pages.
    :type continuation_token: str
    :param next_link: A continuation link (absolute URI) to the next page of
     results in the list.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ProfileResponse]'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, continuation_token=None, next_link=None):
        super(PaginatedProfileResponseList, self).__init__()
        self.value = value
        self.continuation_token = continuation_token
        self.next_link = next_link
