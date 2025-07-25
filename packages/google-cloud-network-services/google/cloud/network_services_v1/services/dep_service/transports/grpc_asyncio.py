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
import inspect
import json
import logging as std_logging
import pickle
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
import google.protobuf.message
import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore
import proto  # type: ignore

from google.cloud.network_services_v1.types import dep

from .base import DEFAULT_CLIENT_INFO, DepServiceTransport
from .grpc import DepServiceGrpcTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientAIOInterceptor(
    grpc.aio.UnaryUnaryClientInterceptor
):  # pragma: NO COVER
    async def intercept_unary_unary(self, continuation, client_call_details, request):
        logging_enabled = CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        )
        if logging_enabled:  # pragma: NO COVER
            request_metadata = client_call_details.metadata
            if isinstance(request, proto.Message):
                request_payload = type(request).to_json(request)
            elif isinstance(request, google.protobuf.message.Message):
                request_payload = MessageToJson(request)
            else:
                request_payload = f"{type(request).__name__}: {pickle.dumps(request)}"

            request_metadata = {
                key: value.decode("utf-8") if isinstance(value, bytes) else value
                for key, value in request_metadata
            }
            grpc_request = {
                "payload": request_payload,
                "requestMethod": "grpc",
                "metadata": dict(request_metadata),
            }
            _LOGGER.debug(
                f"Sending request for {client_call_details.method}",
                extra={
                    "serviceName": "google.cloud.networkservices.v1.DepService",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = await continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = await response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = (
                dict([(k, str(v)) for k, v in response_metadata])
                if response_metadata
                else None
            )
            result = await response
            if isinstance(result, proto.Message):
                response_payload = type(result).to_json(result)
            elif isinstance(result, google.protobuf.message.Message):
                response_payload = MessageToJson(result)
            else:
                response_payload = f"{type(result).__name__}: {pickle.dumps(result)}"
            grpc_response = {
                "payload": response_payload,
                "metadata": metadata,
                "status": "OK",
            }
            _LOGGER.debug(
                f"Received response to rpc {client_call_details.method}.",
                extra={
                    "serviceName": "google.cloud.networkservices.v1.DepService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DepServiceGrpcAsyncIOTransport(DepServiceTransport):
    """gRPC AsyncIO backend transport for DepService.

    Service describing handlers for resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "networkservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "networkservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networkservices.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, aio.Channel):
            # Ignore credentials if a channel was passed.
            credentials = None
            self._ignore_credentials = True
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            # initialize with the provided callable or the default channel
            channel_init = channel or type(self).create_channel
            self._grpc_channel = channel_init(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._interceptor = _LoggingClientAIOInterceptor()
        self._grpc_channel._unary_unary_interceptors.append(self._interceptor)
        self._logged_channel = self._grpc_channel
        self._wrap_with_kind = (
            "kind" in inspect.signature(gapic_v1.method_async.wrap_method).parameters
        )
        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_lb_traffic_extensions(
        self,
    ) -> Callable[
        [dep.ListLbTrafficExtensionsRequest],
        Awaitable[dep.ListLbTrafficExtensionsResponse],
    ]:
        r"""Return a callable for the list lb traffic extensions method over gRPC.

        Lists ``LbTrafficExtension`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListLbTrafficExtensionsRequest],
                    Awaitable[~.ListLbTrafficExtensionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_lb_traffic_extensions" not in self._stubs:
            self._stubs[
                "list_lb_traffic_extensions"
            ] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/ListLbTrafficExtensions",
                request_serializer=dep.ListLbTrafficExtensionsRequest.serialize,
                response_deserializer=dep.ListLbTrafficExtensionsResponse.deserialize,
            )
        return self._stubs["list_lb_traffic_extensions"]

    @property
    def get_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.GetLbTrafficExtensionRequest], Awaitable[dep.LbTrafficExtension]
    ]:
        r"""Return a callable for the get lb traffic extension method over gRPC.

        Gets details of the specified ``LbTrafficExtension`` resource.

        Returns:
            Callable[[~.GetLbTrafficExtensionRequest],
                    Awaitable[~.LbTrafficExtension]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_lb_traffic_extension" not in self._stubs:
            self._stubs["get_lb_traffic_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/GetLbTrafficExtension",
                request_serializer=dep.GetLbTrafficExtensionRequest.serialize,
                response_deserializer=dep.LbTrafficExtension.deserialize,
            )
        return self._stubs["get_lb_traffic_extension"]

    @property
    def create_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.CreateLbTrafficExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create lb traffic extension method over gRPC.

        Creates a new ``LbTrafficExtension`` resource in a given project
        and location.

        Returns:
            Callable[[~.CreateLbTrafficExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_lb_traffic_extension" not in self._stubs:
            self._stubs[
                "create_lb_traffic_extension"
            ] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/CreateLbTrafficExtension",
                request_serializer=dep.CreateLbTrafficExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_lb_traffic_extension"]

    @property
    def update_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.UpdateLbTrafficExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update lb traffic extension method over gRPC.

        Updates the parameters of the specified ``LbTrafficExtension``
        resource.

        Returns:
            Callable[[~.UpdateLbTrafficExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_lb_traffic_extension" not in self._stubs:
            self._stubs[
                "update_lb_traffic_extension"
            ] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/UpdateLbTrafficExtension",
                request_serializer=dep.UpdateLbTrafficExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_lb_traffic_extension"]

    @property
    def delete_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.DeleteLbTrafficExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete lb traffic extension method over gRPC.

        Deletes the specified ``LbTrafficExtension`` resource.

        Returns:
            Callable[[~.DeleteLbTrafficExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_lb_traffic_extension" not in self._stubs:
            self._stubs[
                "delete_lb_traffic_extension"
            ] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/DeleteLbTrafficExtension",
                request_serializer=dep.DeleteLbTrafficExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_lb_traffic_extension"]

    @property
    def list_lb_route_extensions(
        self,
    ) -> Callable[
        [dep.ListLbRouteExtensionsRequest], Awaitable[dep.ListLbRouteExtensionsResponse]
    ]:
        r"""Return a callable for the list lb route extensions method over gRPC.

        Lists ``LbRouteExtension`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListLbRouteExtensionsRequest],
                    Awaitable[~.ListLbRouteExtensionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_lb_route_extensions" not in self._stubs:
            self._stubs["list_lb_route_extensions"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/ListLbRouteExtensions",
                request_serializer=dep.ListLbRouteExtensionsRequest.serialize,
                response_deserializer=dep.ListLbRouteExtensionsResponse.deserialize,
            )
        return self._stubs["list_lb_route_extensions"]

    @property
    def get_lb_route_extension(
        self,
    ) -> Callable[[dep.GetLbRouteExtensionRequest], Awaitable[dep.LbRouteExtension]]:
        r"""Return a callable for the get lb route extension method over gRPC.

        Gets details of the specified ``LbRouteExtension`` resource.

        Returns:
            Callable[[~.GetLbRouteExtensionRequest],
                    Awaitable[~.LbRouteExtension]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_lb_route_extension" not in self._stubs:
            self._stubs["get_lb_route_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/GetLbRouteExtension",
                request_serializer=dep.GetLbRouteExtensionRequest.serialize,
                response_deserializer=dep.LbRouteExtension.deserialize,
            )
        return self._stubs["get_lb_route_extension"]

    @property
    def create_lb_route_extension(
        self,
    ) -> Callable[
        [dep.CreateLbRouteExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create lb route extension method over gRPC.

        Creates a new ``LbRouteExtension`` resource in a given project
        and location.

        Returns:
            Callable[[~.CreateLbRouteExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_lb_route_extension" not in self._stubs:
            self._stubs["create_lb_route_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/CreateLbRouteExtension",
                request_serializer=dep.CreateLbRouteExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_lb_route_extension"]

    @property
    def update_lb_route_extension(
        self,
    ) -> Callable[
        [dep.UpdateLbRouteExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update lb route extension method over gRPC.

        Updates the parameters of the specified ``LbRouteExtension``
        resource.

        Returns:
            Callable[[~.UpdateLbRouteExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_lb_route_extension" not in self._stubs:
            self._stubs["update_lb_route_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/UpdateLbRouteExtension",
                request_serializer=dep.UpdateLbRouteExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_lb_route_extension"]

    @property
    def delete_lb_route_extension(
        self,
    ) -> Callable[
        [dep.DeleteLbRouteExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete lb route extension method over gRPC.

        Deletes the specified ``LbRouteExtension`` resource.

        Returns:
            Callable[[~.DeleteLbRouteExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_lb_route_extension" not in self._stubs:
            self._stubs["delete_lb_route_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/DeleteLbRouteExtension",
                request_serializer=dep.DeleteLbRouteExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_lb_route_extension"]

    @property
    def list_authz_extensions(
        self,
    ) -> Callable[
        [dep.ListAuthzExtensionsRequest], Awaitable[dep.ListAuthzExtensionsResponse]
    ]:
        r"""Return a callable for the list authz extensions method over gRPC.

        Lists ``AuthzExtension`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListAuthzExtensionsRequest],
                    Awaitable[~.ListAuthzExtensionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_authz_extensions" not in self._stubs:
            self._stubs["list_authz_extensions"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/ListAuthzExtensions",
                request_serializer=dep.ListAuthzExtensionsRequest.serialize,
                response_deserializer=dep.ListAuthzExtensionsResponse.deserialize,
            )
        return self._stubs["list_authz_extensions"]

    @property
    def get_authz_extension(
        self,
    ) -> Callable[[dep.GetAuthzExtensionRequest], Awaitable[dep.AuthzExtension]]:
        r"""Return a callable for the get authz extension method over gRPC.

        Gets details of the specified ``AuthzExtension`` resource.

        Returns:
            Callable[[~.GetAuthzExtensionRequest],
                    Awaitable[~.AuthzExtension]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_authz_extension" not in self._stubs:
            self._stubs["get_authz_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/GetAuthzExtension",
                request_serializer=dep.GetAuthzExtensionRequest.serialize,
                response_deserializer=dep.AuthzExtension.deserialize,
            )
        return self._stubs["get_authz_extension"]

    @property
    def create_authz_extension(
        self,
    ) -> Callable[
        [dep.CreateAuthzExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create authz extension method over gRPC.

        Creates a new ``AuthzExtension`` resource in a given project and
        location.

        Returns:
            Callable[[~.CreateAuthzExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_authz_extension" not in self._stubs:
            self._stubs["create_authz_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/CreateAuthzExtension",
                request_serializer=dep.CreateAuthzExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_authz_extension"]

    @property
    def update_authz_extension(
        self,
    ) -> Callable[
        [dep.UpdateAuthzExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update authz extension method over gRPC.

        Updates the parameters of the specified ``AuthzExtension``
        resource.

        Returns:
            Callable[[~.UpdateAuthzExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_authz_extension" not in self._stubs:
            self._stubs["update_authz_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/UpdateAuthzExtension",
                request_serializer=dep.UpdateAuthzExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_authz_extension"]

    @property
    def delete_authz_extension(
        self,
    ) -> Callable[
        [dep.DeleteAuthzExtensionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete authz extension method over gRPC.

        Deletes the specified ``AuthzExtension`` resource.

        Returns:
            Callable[[~.DeleteAuthzExtensionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_authz_extension" not in self._stubs:
            self._stubs["delete_authz_extension"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.DepService/DeleteAuthzExtension",
                request_serializer=dep.DeleteAuthzExtensionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_authz_extension"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_lb_traffic_extensions: self._wrap_method(
                self.list_lb_traffic_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lb_traffic_extension: self._wrap_method(
                self.get_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_lb_traffic_extension: self._wrap_method(
                self.create_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_lb_traffic_extension: self._wrap_method(
                self.update_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_lb_traffic_extension: self._wrap_method(
                self.delete_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_lb_route_extensions: self._wrap_method(
                self.list_lb_route_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lb_route_extension: self._wrap_method(
                self.get_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_lb_route_extension: self._wrap_method(
                self.create_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_lb_route_extension: self._wrap_method(
                self.update_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_lb_route_extension: self._wrap_method(
                self.delete_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_authz_extensions: self._wrap_method(
                self.list_authz_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_authz_extension: self._wrap_method(
                self.get_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_authz_extension: self._wrap_method(
                self.create_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_authz_extension: self._wrap_method(
                self.update_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_authz_extension: self._wrap_method(
                self.delete_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def close(self):
        return self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc_asyncio"

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse
    ]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self._logged_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self._logged_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.
        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.
        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.
        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.
        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.
        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.
        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]


__all__ = ("DepServiceGrpcAsyncIOTransport",)
