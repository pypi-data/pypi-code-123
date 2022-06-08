# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operations import build_check_name_availability_request, build_list_request, build_regional_check_name_availability_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class Operations:
    """Operations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.appconfiguration.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def check_name_availability(
        self,
        check_name_availability_parameters: "_models.CheckNameAvailabilityParameters",
        **kwargs: Any
    ) -> "_models.NameAvailabilityStatus":
        """Checks whether the configuration store name is available for use.

        :param check_name_availability_parameters: The object containing information for the
         availability request.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.models.CheckNameAvailabilityParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus, or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.NameAvailabilityStatus"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(check_name_availability_parameters, 'CheckNameAvailabilityParameters')

        request = build_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.check_name_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('NameAvailabilityStatus', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/checkNameAvailability"}  # type: ignore


    @distributed_trace
    def list(
        self,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.OperationDefinitionListResult"]:
        """Lists the operations available from this provider.

        :param skip_token: A skip token is used to continue retrieving items after an operation returns
         a partial result. If a previous response contains a nextLink element, the value of the nextLink
         element will include a skipToken parameter that specifies a starting point to use for
         subsequent calls. Default value is None.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OperationDefinitionListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.appconfiguration.models.OperationDefinitionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-05-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.OperationDefinitionListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    api_version=api_version,
                    skip_token=skip_token,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    api_version=api_version,
                    skip_token=skip_token,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("OperationDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/providers/Microsoft.AppConfiguration/operations"}  # type: ignore

    @distributed_trace_async
    async def regional_check_name_availability(
        self,
        location: str,
        check_name_availability_parameters: "_models.CheckNameAvailabilityParameters",
        **kwargs: Any
    ) -> "_models.NameAvailabilityStatus":
        """Checks whether the configuration store name is available for use.

        :param location: The location in which uniqueness will be verified.
        :type location: str
        :param check_name_availability_parameters: The object containing information for the
         availability request.
        :type check_name_availability_parameters:
         ~azure.mgmt.appconfiguration.models.CheckNameAvailabilityParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NameAvailabilityStatus, or the result of cls(response)
        :rtype: ~azure.mgmt.appconfiguration.models.NameAvailabilityStatus
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.NameAvailabilityStatus"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(check_name_availability_parameters, 'CheckNameAvailabilityParameters')

        request = build_regional_check_name_availability_request(
            subscription_id=self._config.subscription_id,
            location=location,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.regional_check_name_availability.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('NameAvailabilityStatus', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regional_check_name_availability.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/locations/{location}/checkNameAvailability"}  # type: ignore

