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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import google.protobuf

from google.cloud.compute_v1beta import gapic_version as package_version
from google.cloud.compute_v1beta.services import global_operations
from google.cloud.compute_v1beta.types import compute

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)

if hasattr(DEFAULT_CLIENT_INFO, "protobuf_runtime_version"):  # pragma: NO COVER
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ProjectsTransport(abc.ABC):
    """Abstract transport class for Projects."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/compute",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    DEFAULT_HOST: str = "compute.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'compute.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        self._extended_operations_services: Dict[str, Any] = {}

        scopes_kwargs = {"scopes": scopes, "default_scopes": self.AUTH_SCOPES}

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.disable_xpn_host: gapic_v1.method.wrap_method(
                self.disable_xpn_host,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_xpn_resource: gapic_v1.method.wrap_method(
                self.disable_xpn_resource,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_xpn_host: gapic_v1.method.wrap_method(
                self.enable_xpn_host,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_xpn_resource: gapic_v1.method.wrap_method(
                self.enable_xpn_resource,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get: gapic_v1.method.wrap_method(
                self.get,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_xpn_host: gapic_v1.method.wrap_method(
                self.get_xpn_host,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_xpn_resources: gapic_v1.method.wrap_method(
                self.get_xpn_resources,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_xpn_hosts: gapic_v1.method.wrap_method(
                self.list_xpn_hosts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_disk: gapic_v1.method.wrap_method(
                self.move_disk,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_instance: gapic_v1.method.wrap_method(
                self.move_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_cloud_armor_tier: gapic_v1.method.wrap_method(
                self.set_cloud_armor_tier,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_common_instance_metadata: gapic_v1.method.wrap_method(
                self.set_common_instance_metadata,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_default_network_tier: gapic_v1.method.wrap_method(
                self.set_default_network_tier,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_managed_protection_tier: gapic_v1.method.wrap_method(
                self.set_managed_protection_tier,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_usage_export_bucket: gapic_v1.method.wrap_method(
                self.set_usage_export_bucket,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def disable_xpn_host(
        self,
    ) -> Callable[
        [compute.DisableXpnHostProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def disable_xpn_resource(
        self,
    ) -> Callable[
        [compute.DisableXpnResourceProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def enable_xpn_host(
        self,
    ) -> Callable[
        [compute.EnableXpnHostProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def enable_xpn_resource(
        self,
    ) -> Callable[
        [compute.EnableXpnResourceProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get(
        self,
    ) -> Callable[
        [compute.GetProjectRequest], Union[compute.Project, Awaitable[compute.Project]]
    ]:
        raise NotImplementedError()

    @property
    def get_xpn_host(
        self,
    ) -> Callable[
        [compute.GetXpnHostProjectRequest],
        Union[compute.Project, Awaitable[compute.Project]],
    ]:
        raise NotImplementedError()

    @property
    def get_xpn_resources(
        self,
    ) -> Callable[
        [compute.GetXpnResourcesProjectsRequest],
        Union[
            compute.ProjectsGetXpnResources, Awaitable[compute.ProjectsGetXpnResources]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_xpn_hosts(
        self,
    ) -> Callable[
        [compute.ListXpnHostsProjectsRequest],
        Union[compute.XpnHostList, Awaitable[compute.XpnHostList]],
    ]:
        raise NotImplementedError()

    @property
    def move_disk(
        self,
    ) -> Callable[
        [compute.MoveDiskProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def move_instance(
        self,
    ) -> Callable[
        [compute.MoveInstanceProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_cloud_armor_tier(
        self,
    ) -> Callable[
        [compute.SetCloudArmorTierProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_common_instance_metadata(
        self,
    ) -> Callable[
        [compute.SetCommonInstanceMetadataProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_default_network_tier(
        self,
    ) -> Callable[
        [compute.SetDefaultNetworkTierProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_managed_protection_tier(
        self,
    ) -> Callable[
        [compute.SetManagedProtectionTierProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_usage_export_bucket(
        self,
    ) -> Callable[
        [compute.SetUsageExportBucketProjectRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()

    @property
    def _global_operations_client(self) -> global_operations.GlobalOperationsClient:
        ex_op_service = self._extended_operations_services.get("global_operations")
        if not ex_op_service:
            ex_op_service = global_operations.GlobalOperationsClient(
                credentials=self._credentials,
                transport=self.kind,
            )
            self._extended_operations_services["global_operations"] = ex_op_service

        return ex_op_service


__all__ = ("ProjectsTransport",)
