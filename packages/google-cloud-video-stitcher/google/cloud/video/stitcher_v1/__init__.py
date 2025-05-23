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
from google.cloud.video.stitcher_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.video_stitcher_service import (
    VideoStitcherServiceAsyncClient,
    VideoStitcherServiceClient,
)
from .types.ad_tag_details import (
    AdRequest,
    LiveAdTagDetail,
    RequestMetadata,
    ResponseMetadata,
    VodAdTagDetail,
)
from .types.cdn_keys import AkamaiCdnKey, CdnKey, GoogleCdnKey, MediaCdnKey
from .types.companions import (
    Companion,
    CompanionAds,
    HtmlAdResource,
    IframeAdResource,
    StaticAdResource,
)
from .types.events import Event, ProgressEvent
from .types.fetch_options import FetchOptions
from .types.live_configs import AdTracking, GamLiveConfig, LiveConfig, PrefetchConfig
from .types.sessions import (
    Interstitials,
    LiveSession,
    ManifestOptions,
    RenditionFilter,
    VodSession,
    VodSessionAd,
    VodSessionAdBreak,
    VodSessionContent,
)
from .types.slates import Slate
from .types.stitch_details import AdStitchDetail, VodStitchDetail
from .types.video_stitcher_service import (
    CreateCdnKeyRequest,
    CreateLiveConfigRequest,
    CreateLiveSessionRequest,
    CreateSlateRequest,
    CreateVodConfigRequest,
    CreateVodSessionRequest,
    DeleteCdnKeyRequest,
    DeleteLiveConfigRequest,
    DeleteSlateRequest,
    DeleteVodConfigRequest,
    GetCdnKeyRequest,
    GetLiveAdTagDetailRequest,
    GetLiveConfigRequest,
    GetLiveSessionRequest,
    GetSlateRequest,
    GetVodAdTagDetailRequest,
    GetVodConfigRequest,
    GetVodSessionRequest,
    GetVodStitchDetailRequest,
    ListCdnKeysRequest,
    ListCdnKeysResponse,
    ListLiveAdTagDetailsRequest,
    ListLiveAdTagDetailsResponse,
    ListLiveConfigsRequest,
    ListLiveConfigsResponse,
    ListSlatesRequest,
    ListSlatesResponse,
    ListVodAdTagDetailsRequest,
    ListVodAdTagDetailsResponse,
    ListVodConfigsRequest,
    ListVodConfigsResponse,
    ListVodStitchDetailsRequest,
    ListVodStitchDetailsResponse,
    OperationMetadata,
    UpdateCdnKeyRequest,
    UpdateLiveConfigRequest,
    UpdateSlateRequest,
    UpdateVodConfigRequest,
)
from .types.vod_configs import GamVodConfig, VodConfig

__all__ = (
    "VideoStitcherServiceAsyncClient",
    "AdRequest",
    "AdStitchDetail",
    "AdTracking",
    "AkamaiCdnKey",
    "CdnKey",
    "Companion",
    "CompanionAds",
    "CreateCdnKeyRequest",
    "CreateLiveConfigRequest",
    "CreateLiveSessionRequest",
    "CreateSlateRequest",
    "CreateVodConfigRequest",
    "CreateVodSessionRequest",
    "DeleteCdnKeyRequest",
    "DeleteLiveConfigRequest",
    "DeleteSlateRequest",
    "DeleteVodConfigRequest",
    "Event",
    "FetchOptions",
    "GamLiveConfig",
    "GamVodConfig",
    "GetCdnKeyRequest",
    "GetLiveAdTagDetailRequest",
    "GetLiveConfigRequest",
    "GetLiveSessionRequest",
    "GetSlateRequest",
    "GetVodAdTagDetailRequest",
    "GetVodConfigRequest",
    "GetVodSessionRequest",
    "GetVodStitchDetailRequest",
    "GoogleCdnKey",
    "HtmlAdResource",
    "IframeAdResource",
    "Interstitials",
    "ListCdnKeysRequest",
    "ListCdnKeysResponse",
    "ListLiveAdTagDetailsRequest",
    "ListLiveAdTagDetailsResponse",
    "ListLiveConfigsRequest",
    "ListLiveConfigsResponse",
    "ListSlatesRequest",
    "ListSlatesResponse",
    "ListVodAdTagDetailsRequest",
    "ListVodAdTagDetailsResponse",
    "ListVodConfigsRequest",
    "ListVodConfigsResponse",
    "ListVodStitchDetailsRequest",
    "ListVodStitchDetailsResponse",
    "LiveAdTagDetail",
    "LiveConfig",
    "LiveSession",
    "ManifestOptions",
    "MediaCdnKey",
    "OperationMetadata",
    "PrefetchConfig",
    "ProgressEvent",
    "RenditionFilter",
    "RequestMetadata",
    "ResponseMetadata",
    "Slate",
    "StaticAdResource",
    "UpdateCdnKeyRequest",
    "UpdateLiveConfigRequest",
    "UpdateSlateRequest",
    "UpdateVodConfigRequest",
    "VideoStitcherServiceClient",
    "VodAdTagDetail",
    "VodConfig",
    "VodSession",
    "VodSessionAd",
    "VodSessionAdBreak",
    "VodSessionContent",
    "VodStitchDetail",
)
