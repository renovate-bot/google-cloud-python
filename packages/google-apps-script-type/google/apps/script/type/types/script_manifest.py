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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

from google.protobuf import struct_pb2  # type: ignore
import proto  # type: ignore

from google.apps.script.type.types import addon_widget_set, extension_point

__protobuf__ = proto.module(
    package="google.apps.script.type",
    manifest={
        "HttpAuthorizationHeader",
        "CommonAddOnManifest",
        "LayoutProperties",
        "HttpOptions",
    },
)


class HttpAuthorizationHeader(proto.Enum):
    r"""Authorization header sent in add-on HTTP requests

    Values:
        HTTP_AUTHORIZATION_HEADER_UNSPECIFIED (0):
            Default value, equivalent to ``SYSTEM_ID_TOKEN``
        SYSTEM_ID_TOKEN (1):
            Send an ID token for the project-specific
            Google Workspace add-ons system service account
            (default)
        USER_ID_TOKEN (2):
            Send an ID token for the end user
        NONE (3):
            Do not send an Authentication header
    """
    HTTP_AUTHORIZATION_HEADER_UNSPECIFIED = 0
    SYSTEM_ID_TOKEN = 1
    USER_ID_TOKEN = 2
    NONE = 3


class CommonAddOnManifest(proto.Message):
    r"""Add-on configuration that is shared across all add-on host
    applications.

    Attributes:
        name (str):
            Required. The display name of the add-on.
        logo_url (str):
            Required. The URL for the logo image shown in
            the add-on toolbar.
        layout_properties (google.apps.script.type.types.LayoutProperties):
            Common layout properties for the add-on
            cards.
        add_on_widget_set (google.apps.script.type.types.AddOnWidgetSet):
            The widgets used in the add-on. If this field
            is not specified, it indicates that default set
            is used.
        use_locale_from_app (bool):
            Whether to pass locale information from host
            app.
        homepage_trigger (google.apps.script.type.types.HomepageExtensionPoint):
            Defines an endpoint that will be executed in
            any context, in any host. Any cards generated by
            this function will always be available to the
            user, but may be eclipsed by contextual content
            when this add-on declares more targeted
            triggers.
        universal_actions (MutableSequence[google.apps.script.type.types.UniversalActionExtensionPoint]):
            Defines a list of extension points in the
            universal action menu which serves as a setting
            menu for the add-on. The extension point can be
            link URL to open or an endpoint to execute as a
            form submission.
        open_link_url_prefixes (google.protobuf.struct_pb2.ListValue):
            An OpenLink action can only use a URL with an HTTPS, MAILTO
            or TEL scheme. For HTTPS links, the URL must also
            `match </gmail/add-ons/concepts/manifests#whitelisting_urls>`__
            one of the prefixes specified in this whitelist. If the
            prefix omits the scheme, HTTPS is assumed. Notice that HTTP
            links are automatically rewritten to HTTPS links.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    logo_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    layout_properties: "LayoutProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LayoutProperties",
    )
    add_on_widget_set: addon_widget_set.AddOnWidgetSet = proto.Field(
        proto.MESSAGE,
        number=4,
        message=addon_widget_set.AddOnWidgetSet,
    )
    use_locale_from_app: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    homepage_trigger: extension_point.HomepageExtensionPoint = proto.Field(
        proto.MESSAGE,
        number=6,
        message=extension_point.HomepageExtensionPoint,
    )
    universal_actions: MutableSequence[
        extension_point.UniversalActionExtensionPoint
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=extension_point.UniversalActionExtensionPoint,
    )
    open_link_url_prefixes: struct_pb2.ListValue = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.ListValue,
    )


class LayoutProperties(proto.Message):
    r"""Card layout properties shared across all add-on host
    applications.

    Attributes:
        primary_color (str):
            The primary color of the add-on. It sets the
            color of toolbar. If no primary color is set
            explicitly, the default value provided by the
            framework is used.
        secondary_color (str):
            The secondary color of the add-on. It sets
            the color of buttons. If primary color is set
            but no secondary color is set, the secondary
            color is the same as the primary color. If
            neither primary color nor secondary color is
            set, the default value provided by the framework
            is used.
    """

    primary_color: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secondary_color: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HttpOptions(proto.Message):
    r"""Options for sending requests to add-on HTTP endpoints

    Attributes:
        authorization_header (google.apps.script.type.types.HttpAuthorizationHeader):
            Configuration for the token sent in the HTTP
            Authorization header
    """

    authorization_header: "HttpAuthorizationHeader" = proto.Field(
        proto.ENUM,
        number=1,
        enum="HttpAuthorizationHeader",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
