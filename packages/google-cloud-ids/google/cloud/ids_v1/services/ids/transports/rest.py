# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import dataclasses
import json  # type: ignore
import logging
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
import google.protobuf
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.ids_v1.types import ids

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseIDSRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

if hasattr(DEFAULT_CLIENT_INFO, "protobuf_runtime_version"):  # pragma: NO COVER
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class IDSRestInterceptor:
    """Interceptor for IDS.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IDSRestTransport.

    .. code-block:: python
        class MyCustomIDSInterceptor(IDSRestInterceptor):
            def pre_create_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_endpoint(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_endpoint(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_endpoints(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_endpoints(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = IDSRestTransport(interceptor=MyCustomIDSInterceptor())
        client = IDSClient(transport=transport)


    """

    def pre_create_endpoint(
        self,
        request: ids.CreateEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ids.CreateEndpointRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IDS server.
        """
        return request, metadata

    def post_create_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_endpoint

        DEPRECATED. Please use the `post_create_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IDS server but before
        it is returned to user code. This `post_create_endpoint` interceptor runs
        before the `post_create_endpoint_with_metadata` interceptor.
        """
        return response

    def post_create_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IDS server but before it is returned to user code.

        We recommend only using this `post_create_endpoint_with_metadata`
        interceptor in new development instead of the `post_create_endpoint` interceptor.
        When both interceptors are used, this `post_create_endpoint_with_metadata` interceptor runs after the
        `post_create_endpoint` interceptor. The (possibly modified) response returned by
        `post_create_endpoint` will be passed to
        `post_create_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_delete_endpoint(
        self,
        request: ids.DeleteEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ids.DeleteEndpointRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IDS server.
        """
        return request, metadata

    def post_delete_endpoint(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_endpoint

        DEPRECATED. Please use the `post_delete_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IDS server but before
        it is returned to user code. This `post_delete_endpoint` interceptor runs
        before the `post_delete_endpoint_with_metadata` interceptor.
        """
        return response

    def post_delete_endpoint_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IDS server but before it is returned to user code.

        We recommend only using this `post_delete_endpoint_with_metadata`
        interceptor in new development instead of the `post_delete_endpoint` interceptor.
        When both interceptors are used, this `post_delete_endpoint_with_metadata` interceptor runs after the
        `post_delete_endpoint` interceptor. The (possibly modified) response returned by
        `post_delete_endpoint` will be passed to
        `post_delete_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_get_endpoint(
        self,
        request: ids.GetEndpointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ids.GetEndpointRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_endpoint

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IDS server.
        """
        return request, metadata

    def post_get_endpoint(self, response: ids.Endpoint) -> ids.Endpoint:
        """Post-rpc interceptor for get_endpoint

        DEPRECATED. Please use the `post_get_endpoint_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IDS server but before
        it is returned to user code. This `post_get_endpoint` interceptor runs
        before the `post_get_endpoint_with_metadata` interceptor.
        """
        return response

    def post_get_endpoint_with_metadata(
        self, response: ids.Endpoint, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[ids.Endpoint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_endpoint

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IDS server but before it is returned to user code.

        We recommend only using this `post_get_endpoint_with_metadata`
        interceptor in new development instead of the `post_get_endpoint` interceptor.
        When both interceptors are used, this `post_get_endpoint_with_metadata` interceptor runs after the
        `post_get_endpoint` interceptor. The (possibly modified) response returned by
        `post_get_endpoint` will be passed to
        `post_get_endpoint_with_metadata`.
        """
        return response, metadata

    def pre_list_endpoints(
        self,
        request: ids.ListEndpointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ids.ListEndpointsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_endpoints

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IDS server.
        """
        return request, metadata

    def post_list_endpoints(
        self, response: ids.ListEndpointsResponse
    ) -> ids.ListEndpointsResponse:
        """Post-rpc interceptor for list_endpoints

        DEPRECATED. Please use the `post_list_endpoints_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the IDS server but before
        it is returned to user code. This `post_list_endpoints` interceptor runs
        before the `post_list_endpoints_with_metadata` interceptor.
        """
        return response

    def post_list_endpoints_with_metadata(
        self,
        response: ids.ListEndpointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ids.ListEndpointsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_endpoints

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the IDS server but before it is returned to user code.

        We recommend only using this `post_list_endpoints_with_metadata`
        interceptor in new development instead of the `post_list_endpoints` interceptor.
        When both interceptors are used, this `post_list_endpoints_with_metadata` interceptor runs after the
        `post_list_endpoints` interceptor. The (possibly modified) response returned by
        `post_list_endpoints` will be passed to
        `post_list_endpoints_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class IDSRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IDSRestInterceptor


class IDSRestTransport(_BaseIDSRestTransport):
    """REST backend synchronous transport for IDS.

    The IDS Service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "ids.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[IDSRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'ids.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or IDSRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateEndpoint(_BaseIDSRestTransport._BaseCreateEndpoint, IDSRestStub):
        def __hash__(self):
            return hash("IDSRestTransport.CreateEndpoint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: ids.CreateEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create endpoint method over HTTP.

            Args:
                request (~.ids.CreateEndpointRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseIDSRestTransport._BaseCreateEndpoint._get_http_options()

            request, metadata = self._interceptor.pre_create_endpoint(request, metadata)
            transcoded_request = (
                _BaseIDSRestTransport._BaseCreateEndpoint._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseIDSRestTransport._BaseCreateEndpoint._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseIDSRestTransport._BaseCreateEndpoint._get_query_params_json(
                    transcoded_request
                )
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.ids_v1.IDSClient.CreateEndpoint",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "CreateEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IDSRestTransport._CreateEndpoint._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_endpoint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ids_v1.IDSClient.create_endpoint",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "CreateEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEndpoint(_BaseIDSRestTransport._BaseDeleteEndpoint, IDSRestStub):
        def __hash__(self):
            return hash("IDSRestTransport.DeleteEndpoint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: ids.DeleteEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete endpoint method over HTTP.

            Args:
                request (~.ids.DeleteEndpointRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseIDSRestTransport._BaseDeleteEndpoint._get_http_options()

            request, metadata = self._interceptor.pre_delete_endpoint(request, metadata)
            transcoded_request = (
                _BaseIDSRestTransport._BaseDeleteEndpoint._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseIDSRestTransport._BaseDeleteEndpoint._get_query_params_json(
                    transcoded_request
                )
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.ids_v1.IDSClient.DeleteEndpoint",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "DeleteEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IDSRestTransport._DeleteEndpoint._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_endpoint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ids_v1.IDSClient.delete_endpoint",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "DeleteEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEndpoint(_BaseIDSRestTransport._BaseGetEndpoint, IDSRestStub):
        def __hash__(self):
            return hash("IDSRestTransport.GetEndpoint")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: ids.GetEndpointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ids.Endpoint:
            r"""Call the get endpoint method over HTTP.

            Args:
                request (~.ids.GetEndpointRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ids.Endpoint:
                    Endpoint describes a single IDS
                endpoint. It defines a forwarding rule
                to which packets can be sent for IDS
                inspection.

            """

            http_options = _BaseIDSRestTransport._BaseGetEndpoint._get_http_options()

            request, metadata = self._interceptor.pre_get_endpoint(request, metadata)
            transcoded_request = (
                _BaseIDSRestTransport._BaseGetEndpoint._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseIDSRestTransport._BaseGetEndpoint._get_query_params_json(
                    transcoded_request
                )
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.ids_v1.IDSClient.GetEndpoint",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "GetEndpoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IDSRestTransport._GetEndpoint._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = ids.Endpoint()
            pb_resp = ids.Endpoint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_endpoint(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_endpoint_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ids.Endpoint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ids_v1.IDSClient.get_endpoint",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "GetEndpoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEndpoints(_BaseIDSRestTransport._BaseListEndpoints, IDSRestStub):
        def __hash__(self):
            return hash("IDSRestTransport.ListEndpoints")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: ids.ListEndpointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ids.ListEndpointsResponse:
            r"""Call the list endpoints method over HTTP.

            Args:
                request (~.ids.ListEndpointsRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ids.ListEndpointsResponse:

            """

            http_options = _BaseIDSRestTransport._BaseListEndpoints._get_http_options()

            request, metadata = self._interceptor.pre_list_endpoints(request, metadata)
            transcoded_request = (
                _BaseIDSRestTransport._BaseListEndpoints._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseIDSRestTransport._BaseListEndpoints._get_query_params_json(
                    transcoded_request
                )
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.ids_v1.IDSClient.ListEndpoints",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "ListEndpoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = IDSRestTransport._ListEndpoints._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = ids.ListEndpointsResponse()
            pb_resp = ids.ListEndpointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_endpoints(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_endpoints_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ids.ListEndpointsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.ids_v1.IDSClient.list_endpoints",
                    extra={
                        "serviceName": "google.cloud.ids.v1.IDS",
                        "rpcName": "ListEndpoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_endpoint(
        self,
    ) -> Callable[[ids.CreateEndpointRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEndpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_endpoint(
        self,
    ) -> Callable[[ids.DeleteEndpointRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEndpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_endpoint(self) -> Callable[[ids.GetEndpointRequest], ids.Endpoint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEndpoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_endpoints(
        self,
    ) -> Callable[[ids.ListEndpointsRequest], ids.ListEndpointsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEndpoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("IDSRestTransport",)
