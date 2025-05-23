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
from google.cloud.visionai import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.visionai_v1.services.app_platform.async_client import (
    AppPlatformAsyncClient,
)
from google.cloud.visionai_v1.services.app_platform.client import AppPlatformClient
from google.cloud.visionai_v1.services.health_check_service.async_client import (
    HealthCheckServiceAsyncClient,
)
from google.cloud.visionai_v1.services.health_check_service.client import (
    HealthCheckServiceClient,
)
from google.cloud.visionai_v1.services.live_video_analytics.async_client import (
    LiveVideoAnalyticsAsyncClient,
)
from google.cloud.visionai_v1.services.live_video_analytics.client import (
    LiveVideoAnalyticsClient,
)
from google.cloud.visionai_v1.services.streaming_service.async_client import (
    StreamingServiceAsyncClient,
)
from google.cloud.visionai_v1.services.streaming_service.client import (
    StreamingServiceClient,
)
from google.cloud.visionai_v1.services.streams_service.async_client import (
    StreamsServiceAsyncClient,
)
from google.cloud.visionai_v1.services.streams_service.client import (
    StreamsServiceClient,
)
from google.cloud.visionai_v1.services.warehouse.async_client import (
    WarehouseAsyncClient,
)
from google.cloud.visionai_v1.services.warehouse.client import WarehouseClient
from google.cloud.visionai_v1.types.annotations import (
    AppPlatformCloudFunctionRequest,
    AppPlatformCloudFunctionResponse,
    AppPlatformEventBody,
    AppPlatformMetadata,
    ClassificationPredictionResult,
    ImageObjectDetectionPredictionResult,
    ImageSegmentationPredictionResult,
    NormalizedPolygon,
    NormalizedPolyline,
    NormalizedVertex,
    ObjectDetectionPredictionResult,
    OccupancyCountingPredictionResult,
    PersonalProtectiveEquipmentDetectionOutput,
    StreamAnnotation,
    StreamAnnotations,
    StreamAnnotationType,
    VideoActionRecognitionPredictionResult,
    VideoClassificationPredictionResult,
    VideoObjectTrackingPredictionResult,
)
from google.cloud.visionai_v1.types.common import Cluster, GcsSource, OperationMetadata
from google.cloud.visionai_v1.types.health_service import (
    ClusterInfo,
    HealthCheckRequest,
    HealthCheckResponse,
)
from google.cloud.visionai_v1.types.lva import (
    AnalysisDefinition,
    AnalyzerDefinition,
    AttributeValue,
    OperatorDefinition,
    ResourceSpecification,
    RunMode,
    RunStatus,
)
from google.cloud.visionai_v1.types.lva_resources import Analysis, Operator, Process
from google.cloud.visionai_v1.types.lva_service import (
    BatchRunProcessRequest,
    BatchRunProcessResponse,
    CreateAnalysisRequest,
    CreateOperatorRequest,
    CreateProcessRequest,
    DeleteAnalysisRequest,
    DeleteOperatorRequest,
    DeleteProcessRequest,
    GetAnalysisRequest,
    GetOperatorRequest,
    GetProcessRequest,
    ListAnalysesRequest,
    ListAnalysesResponse,
    ListOperatorsRequest,
    ListOperatorsResponse,
    ListProcessesRequest,
    ListProcessesResponse,
    ListPublicOperatorsRequest,
    ListPublicOperatorsResponse,
    OperatorQuery,
    Registry,
    ResolveOperatorInfoRequest,
    ResolveOperatorInfoResponse,
    UpdateAnalysisRequest,
    UpdateOperatorRequest,
    UpdateProcessRequest,
)
from google.cloud.visionai_v1.types.platform import (
    AcceleratorType,
    AddApplicationStreamInputRequest,
    AddApplicationStreamInputResponse,
    AIEnabledDevicesInputConfig,
    Application,
    ApplicationConfigs,
    ApplicationInstance,
    ApplicationNodeAnnotation,
    ApplicationStreamInput,
    AutoscalingMetricSpec,
    BigQueryConfig,
    CreateApplicationInstancesRequest,
    CreateApplicationInstancesResponse,
    CreateApplicationRequest,
    CreateDraftRequest,
    CreateProcessorRequest,
    CustomProcessorSourceInfo,
    DataType,
    DedicatedResources,
    DeleteApplicationInstancesRequest,
    DeleteApplicationInstancesResponse,
    DeleteApplicationRequest,
    DeleteDraftRequest,
    DeleteProcessorRequest,
    DeployApplicationRequest,
    DeployApplicationResponse,
    Draft,
    GcsOutputConfig,
    GeneralObjectDetectionConfig,
    GetApplicationRequest,
    GetDraftRequest,
    GetInstanceRequest,
    GetProcessorRequest,
    Instance,
    ListApplicationsRequest,
    ListApplicationsResponse,
    ListDraftsRequest,
    ListDraftsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListPrebuiltProcessorsRequest,
    ListPrebuiltProcessorsResponse,
    ListProcessorsRequest,
    ListProcessorsResponse,
    MachineSpec,
    MediaWarehouseConfig,
    ModelType,
    Node,
    OccupancyCountConfig,
    PersonalProtectiveEquipmentDetectionConfig,
    PersonBlurConfig,
    PersonVehicleDetectionConfig,
    Processor,
    ProcessorConfig,
    ProcessorIOSpec,
    ProductRecognizerConfig,
    RemoveApplicationStreamInputRequest,
    RemoveApplicationStreamInputResponse,
    ResourceAnnotations,
    StreamWithAnnotation,
    TagParsingConfig,
    TagRecognizerConfig,
    UndeployApplicationRequest,
    UndeployApplicationResponse,
    UniversalInputConfig,
    UpdateApplicationInstancesRequest,
    UpdateApplicationInstancesResponse,
    UpdateApplicationRequest,
    UpdateApplicationStreamInputRequest,
    UpdateApplicationStreamInputResponse,
    UpdateDraftRequest,
    UpdateProcessorRequest,
    VertexAutoMLVideoConfig,
    VertexAutoMLVisionConfig,
    VertexCustomConfig,
    VideoStreamInputConfig,
)
from google.cloud.visionai_v1.types.streaming_resources import (
    GstreamerBufferDescriptor,
    Packet,
    PacketHeader,
    PacketType,
    RawImageDescriptor,
    SeriesMetadata,
    ServerMetadata,
)
from google.cloud.visionai_v1.types.streaming_service import (
    AcquireLeaseRequest,
    CommitRequest,
    ControlledMode,
    EagerMode,
    EventUpdate,
    Lease,
    LeaseType,
    ReceiveEventsControlResponse,
    ReceiveEventsRequest,
    ReceiveEventsResponse,
    ReceivePacketsControlResponse,
    ReceivePacketsRequest,
    ReceivePacketsResponse,
    ReleaseLeaseRequest,
    ReleaseLeaseResponse,
    RenewLeaseRequest,
    RequestMetadata,
    SendPacketsRequest,
    SendPacketsResponse,
)
from google.cloud.visionai_v1.types.streams_resources import (
    Channel,
    Event,
    Series,
    Stream,
)
from google.cloud.visionai_v1.types.streams_service import (
    CreateClusterRequest,
    CreateEventRequest,
    CreateSeriesRequest,
    CreateStreamRequest,
    DeleteClusterRequest,
    DeleteEventRequest,
    DeleteSeriesRequest,
    DeleteStreamRequest,
    GenerateStreamHlsTokenRequest,
    GenerateStreamHlsTokenResponse,
    GetClusterRequest,
    GetEventRequest,
    GetSeriesRequest,
    GetStreamRequest,
    GetStreamThumbnailRequest,
    GetStreamThumbnailResponse,
    ListClustersRequest,
    ListClustersResponse,
    ListEventsRequest,
    ListEventsResponse,
    ListSeriesRequest,
    ListSeriesResponse,
    ListStreamsRequest,
    ListStreamsResponse,
    MaterializeChannelRequest,
    UpdateClusterRequest,
    UpdateEventRequest,
    UpdateSeriesRequest,
    UpdateStreamRequest,
)
from google.cloud.visionai_v1.types.warehouse import (
    AddCollectionItemRequest,
    AddCollectionItemResponse,
    AnalyzeAssetMetadata,
    AnalyzeAssetRequest,
    AnalyzeAssetResponse,
    AnalyzeCorpusMetadata,
    AnalyzeCorpusRequest,
    AnalyzeCorpusResponse,
    Annotation,
    AnnotationCustomizedStruct,
    AnnotationList,
    AnnotationMatchingResult,
    AnnotationValue,
    Asset,
    AssetSource,
    BatchOperationStatus,
    BoolValue,
    CircleArea,
    ClipAssetRequest,
    ClipAssetResponse,
    Collection,
    CollectionItem,
    Corpus,
    CreateAnnotationRequest,
    CreateAssetRequest,
    CreateCollectionMetadata,
    CreateCollectionRequest,
    CreateCorpusMetadata,
    CreateCorpusRequest,
    CreateDataSchemaRequest,
    CreateIndexEndpointMetadata,
    CreateIndexEndpointRequest,
    CreateIndexMetadata,
    CreateIndexRequest,
    CreateSearchConfigRequest,
    CreateSearchHypernymRequest,
    Criteria,
    DataSchema,
    DataSchemaDetails,
    DateTimeRange,
    DateTimeRangeArray,
    DeleteAnnotationRequest,
    DeleteAssetMetadata,
    DeleteAssetRequest,
    DeleteCollectionMetadata,
    DeleteCollectionRequest,
    DeleteCorpusRequest,
    DeleteDataSchemaRequest,
    DeleteIndexEndpointMetadata,
    DeleteIndexEndpointRequest,
    DeleteIndexMetadata,
    DeleteIndexRequest,
    DeleteSearchConfigRequest,
    DeleteSearchHypernymRequest,
    DeployedIndex,
    DeployedIndexReference,
    DeployIndexMetadata,
    DeployIndexRequest,
    DeployIndexResponse,
    FacetBucket,
    FacetBucketType,
    FacetGroup,
    FacetProperty,
    FacetValue,
    FloatRange,
    FloatRangeArray,
    GenerateHlsUriRequest,
    GenerateHlsUriResponse,
    GenerateRetrievalUrlRequest,
    GenerateRetrievalUrlResponse,
    GeoCoordinate,
    GeoLocationArray,
    GetAnnotationRequest,
    GetAssetRequest,
    GetCollectionRequest,
    GetCorpusRequest,
    GetDataSchemaRequest,
    GetIndexEndpointRequest,
    GetIndexRequest,
    GetSearchConfigRequest,
    GetSearchHypernymRequest,
    ImageQuery,
    ImportAssetsMetadata,
    ImportAssetsRequest,
    ImportAssetsResponse,
    Index,
    IndexAssetMetadata,
    IndexAssetRequest,
    IndexAssetResponse,
    IndexedAsset,
    IndexEndpoint,
    IndexingStatus,
    IngestAssetRequest,
    IngestAssetResponse,
    IntRange,
    IntRangeArray,
    ListAnnotationsRequest,
    ListAnnotationsResponse,
    ListAssetsRequest,
    ListAssetsResponse,
    ListCollectionsRequest,
    ListCollectionsResponse,
    ListCorporaRequest,
    ListCorporaResponse,
    ListDataSchemasRequest,
    ListDataSchemasResponse,
    ListIndexEndpointsRequest,
    ListIndexEndpointsResponse,
    ListIndexesRequest,
    ListIndexesResponse,
    ListSearchConfigsRequest,
    ListSearchConfigsResponse,
    ListSearchHypernymsRequest,
    ListSearchHypernymsResponse,
    Partition,
    RemoveCollectionItemRequest,
    RemoveCollectionItemResponse,
    RemoveIndexAssetMetadata,
    RemoveIndexAssetRequest,
    RemoveIndexAssetResponse,
    SchemaKeySortingStrategy,
    SearchAssetsRequest,
    SearchAssetsResponse,
    SearchCapability,
    SearchCapabilitySetting,
    SearchConfig,
    SearchCriteriaProperty,
    SearchHypernym,
    SearchIndexEndpointRequest,
    SearchIndexEndpointResponse,
    SearchResultItem,
    StringArray,
    UndeployIndexMetadata,
    UndeployIndexRequest,
    UndeployIndexResponse,
    UpdateAnnotationRequest,
    UpdateAssetRequest,
    UpdateCollectionRequest,
    UpdateCorpusRequest,
    UpdateDataSchemaRequest,
    UpdateIndexEndpointMetadata,
    UpdateIndexEndpointRequest,
    UpdateIndexMetadata,
    UpdateIndexRequest,
    UpdateSearchConfigRequest,
    UpdateSearchHypernymRequest,
    UploadAssetMetadata,
    UploadAssetRequest,
    UploadAssetResponse,
    UserSpecifiedAnnotation,
    ViewCollectionItemsRequest,
    ViewCollectionItemsResponse,
    ViewIndexedAssetsRequest,
    ViewIndexedAssetsResponse,
)

__all__ = (
    "AppPlatformClient",
    "AppPlatformAsyncClient",
    "HealthCheckServiceClient",
    "HealthCheckServiceAsyncClient",
    "LiveVideoAnalyticsClient",
    "LiveVideoAnalyticsAsyncClient",
    "StreamingServiceClient",
    "StreamingServiceAsyncClient",
    "StreamsServiceClient",
    "StreamsServiceAsyncClient",
    "WarehouseClient",
    "WarehouseAsyncClient",
    "AppPlatformCloudFunctionRequest",
    "AppPlatformCloudFunctionResponse",
    "AppPlatformEventBody",
    "AppPlatformMetadata",
    "ClassificationPredictionResult",
    "ImageObjectDetectionPredictionResult",
    "ImageSegmentationPredictionResult",
    "NormalizedPolygon",
    "NormalizedPolyline",
    "NormalizedVertex",
    "ObjectDetectionPredictionResult",
    "OccupancyCountingPredictionResult",
    "PersonalProtectiveEquipmentDetectionOutput",
    "StreamAnnotation",
    "StreamAnnotations",
    "VideoActionRecognitionPredictionResult",
    "VideoClassificationPredictionResult",
    "VideoObjectTrackingPredictionResult",
    "StreamAnnotationType",
    "Cluster",
    "GcsSource",
    "OperationMetadata",
    "ClusterInfo",
    "HealthCheckRequest",
    "HealthCheckResponse",
    "AnalysisDefinition",
    "AnalyzerDefinition",
    "AttributeValue",
    "OperatorDefinition",
    "ResourceSpecification",
    "RunStatus",
    "RunMode",
    "Analysis",
    "Operator",
    "Process",
    "BatchRunProcessRequest",
    "BatchRunProcessResponse",
    "CreateAnalysisRequest",
    "CreateOperatorRequest",
    "CreateProcessRequest",
    "DeleteAnalysisRequest",
    "DeleteOperatorRequest",
    "DeleteProcessRequest",
    "GetAnalysisRequest",
    "GetOperatorRequest",
    "GetProcessRequest",
    "ListAnalysesRequest",
    "ListAnalysesResponse",
    "ListOperatorsRequest",
    "ListOperatorsResponse",
    "ListProcessesRequest",
    "ListProcessesResponse",
    "ListPublicOperatorsRequest",
    "ListPublicOperatorsResponse",
    "OperatorQuery",
    "ResolveOperatorInfoRequest",
    "ResolveOperatorInfoResponse",
    "UpdateAnalysisRequest",
    "UpdateOperatorRequest",
    "UpdateProcessRequest",
    "Registry",
    "AddApplicationStreamInputRequest",
    "AddApplicationStreamInputResponse",
    "AIEnabledDevicesInputConfig",
    "Application",
    "ApplicationConfigs",
    "ApplicationInstance",
    "ApplicationNodeAnnotation",
    "ApplicationStreamInput",
    "AutoscalingMetricSpec",
    "BigQueryConfig",
    "CreateApplicationInstancesRequest",
    "CreateApplicationInstancesResponse",
    "CreateApplicationRequest",
    "CreateDraftRequest",
    "CreateProcessorRequest",
    "CustomProcessorSourceInfo",
    "DedicatedResources",
    "DeleteApplicationInstancesRequest",
    "DeleteApplicationInstancesResponse",
    "DeleteApplicationRequest",
    "DeleteDraftRequest",
    "DeleteProcessorRequest",
    "DeployApplicationRequest",
    "DeployApplicationResponse",
    "Draft",
    "GcsOutputConfig",
    "GeneralObjectDetectionConfig",
    "GetApplicationRequest",
    "GetDraftRequest",
    "GetInstanceRequest",
    "GetProcessorRequest",
    "Instance",
    "ListApplicationsRequest",
    "ListApplicationsResponse",
    "ListDraftsRequest",
    "ListDraftsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListPrebuiltProcessorsRequest",
    "ListPrebuiltProcessorsResponse",
    "ListProcessorsRequest",
    "ListProcessorsResponse",
    "MachineSpec",
    "MediaWarehouseConfig",
    "Node",
    "OccupancyCountConfig",
    "PersonalProtectiveEquipmentDetectionConfig",
    "PersonBlurConfig",
    "PersonVehicleDetectionConfig",
    "Processor",
    "ProcessorConfig",
    "ProcessorIOSpec",
    "ProductRecognizerConfig",
    "RemoveApplicationStreamInputRequest",
    "RemoveApplicationStreamInputResponse",
    "ResourceAnnotations",
    "StreamWithAnnotation",
    "TagParsingConfig",
    "TagRecognizerConfig",
    "UndeployApplicationRequest",
    "UndeployApplicationResponse",
    "UniversalInputConfig",
    "UpdateApplicationInstancesRequest",
    "UpdateApplicationInstancesResponse",
    "UpdateApplicationRequest",
    "UpdateApplicationStreamInputRequest",
    "UpdateApplicationStreamInputResponse",
    "UpdateDraftRequest",
    "UpdateProcessorRequest",
    "VertexAutoMLVideoConfig",
    "VertexAutoMLVisionConfig",
    "VertexCustomConfig",
    "VideoStreamInputConfig",
    "AcceleratorType",
    "DataType",
    "ModelType",
    "GstreamerBufferDescriptor",
    "Packet",
    "PacketHeader",
    "PacketType",
    "RawImageDescriptor",
    "SeriesMetadata",
    "ServerMetadata",
    "AcquireLeaseRequest",
    "CommitRequest",
    "ControlledMode",
    "EagerMode",
    "EventUpdate",
    "Lease",
    "ReceiveEventsControlResponse",
    "ReceiveEventsRequest",
    "ReceiveEventsResponse",
    "ReceivePacketsControlResponse",
    "ReceivePacketsRequest",
    "ReceivePacketsResponse",
    "ReleaseLeaseRequest",
    "ReleaseLeaseResponse",
    "RenewLeaseRequest",
    "RequestMetadata",
    "SendPacketsRequest",
    "SendPacketsResponse",
    "LeaseType",
    "Channel",
    "Event",
    "Series",
    "Stream",
    "CreateClusterRequest",
    "CreateEventRequest",
    "CreateSeriesRequest",
    "CreateStreamRequest",
    "DeleteClusterRequest",
    "DeleteEventRequest",
    "DeleteSeriesRequest",
    "DeleteStreamRequest",
    "GenerateStreamHlsTokenRequest",
    "GenerateStreamHlsTokenResponse",
    "GetClusterRequest",
    "GetEventRequest",
    "GetSeriesRequest",
    "GetStreamRequest",
    "GetStreamThumbnailRequest",
    "GetStreamThumbnailResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListSeriesRequest",
    "ListSeriesResponse",
    "ListStreamsRequest",
    "ListStreamsResponse",
    "MaterializeChannelRequest",
    "UpdateClusterRequest",
    "UpdateEventRequest",
    "UpdateSeriesRequest",
    "UpdateStreamRequest",
    "AddCollectionItemRequest",
    "AddCollectionItemResponse",
    "AnalyzeAssetMetadata",
    "AnalyzeAssetRequest",
    "AnalyzeAssetResponse",
    "AnalyzeCorpusMetadata",
    "AnalyzeCorpusRequest",
    "AnalyzeCorpusResponse",
    "Annotation",
    "AnnotationCustomizedStruct",
    "AnnotationList",
    "AnnotationMatchingResult",
    "AnnotationValue",
    "Asset",
    "AssetSource",
    "BatchOperationStatus",
    "BoolValue",
    "CircleArea",
    "ClipAssetRequest",
    "ClipAssetResponse",
    "Collection",
    "CollectionItem",
    "Corpus",
    "CreateAnnotationRequest",
    "CreateAssetRequest",
    "CreateCollectionMetadata",
    "CreateCollectionRequest",
    "CreateCorpusMetadata",
    "CreateCorpusRequest",
    "CreateDataSchemaRequest",
    "CreateIndexEndpointMetadata",
    "CreateIndexEndpointRequest",
    "CreateIndexMetadata",
    "CreateIndexRequest",
    "CreateSearchConfigRequest",
    "CreateSearchHypernymRequest",
    "Criteria",
    "DataSchema",
    "DataSchemaDetails",
    "DateTimeRange",
    "DateTimeRangeArray",
    "DeleteAnnotationRequest",
    "DeleteAssetMetadata",
    "DeleteAssetRequest",
    "DeleteCollectionMetadata",
    "DeleteCollectionRequest",
    "DeleteCorpusRequest",
    "DeleteDataSchemaRequest",
    "DeleteIndexEndpointMetadata",
    "DeleteIndexEndpointRequest",
    "DeleteIndexMetadata",
    "DeleteIndexRequest",
    "DeleteSearchConfigRequest",
    "DeleteSearchHypernymRequest",
    "DeployedIndex",
    "DeployedIndexReference",
    "DeployIndexMetadata",
    "DeployIndexRequest",
    "DeployIndexResponse",
    "FacetBucket",
    "FacetGroup",
    "FacetProperty",
    "FacetValue",
    "FloatRange",
    "FloatRangeArray",
    "GenerateHlsUriRequest",
    "GenerateHlsUriResponse",
    "GenerateRetrievalUrlRequest",
    "GenerateRetrievalUrlResponse",
    "GeoCoordinate",
    "GeoLocationArray",
    "GetAnnotationRequest",
    "GetAssetRequest",
    "GetCollectionRequest",
    "GetCorpusRequest",
    "GetDataSchemaRequest",
    "GetIndexEndpointRequest",
    "GetIndexRequest",
    "GetSearchConfigRequest",
    "GetSearchHypernymRequest",
    "ImageQuery",
    "ImportAssetsMetadata",
    "ImportAssetsRequest",
    "ImportAssetsResponse",
    "Index",
    "IndexAssetMetadata",
    "IndexAssetRequest",
    "IndexAssetResponse",
    "IndexedAsset",
    "IndexEndpoint",
    "IndexingStatus",
    "IngestAssetRequest",
    "IngestAssetResponse",
    "IntRange",
    "IntRangeArray",
    "ListAnnotationsRequest",
    "ListAnnotationsResponse",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListCollectionsRequest",
    "ListCollectionsResponse",
    "ListCorporaRequest",
    "ListCorporaResponse",
    "ListDataSchemasRequest",
    "ListDataSchemasResponse",
    "ListIndexEndpointsRequest",
    "ListIndexEndpointsResponse",
    "ListIndexesRequest",
    "ListIndexesResponse",
    "ListSearchConfigsRequest",
    "ListSearchConfigsResponse",
    "ListSearchHypernymsRequest",
    "ListSearchHypernymsResponse",
    "Partition",
    "RemoveCollectionItemRequest",
    "RemoveCollectionItemResponse",
    "RemoveIndexAssetMetadata",
    "RemoveIndexAssetRequest",
    "RemoveIndexAssetResponse",
    "SchemaKeySortingStrategy",
    "SearchAssetsRequest",
    "SearchAssetsResponse",
    "SearchCapability",
    "SearchCapabilitySetting",
    "SearchConfig",
    "SearchCriteriaProperty",
    "SearchHypernym",
    "SearchIndexEndpointRequest",
    "SearchIndexEndpointResponse",
    "SearchResultItem",
    "StringArray",
    "UndeployIndexMetadata",
    "UndeployIndexRequest",
    "UndeployIndexResponse",
    "UpdateAnnotationRequest",
    "UpdateAssetRequest",
    "UpdateCollectionRequest",
    "UpdateCorpusRequest",
    "UpdateDataSchemaRequest",
    "UpdateIndexEndpointMetadata",
    "UpdateIndexEndpointRequest",
    "UpdateIndexMetadata",
    "UpdateIndexRequest",
    "UpdateSearchConfigRequest",
    "UpdateSearchHypernymRequest",
    "UploadAssetMetadata",
    "UploadAssetRequest",
    "UploadAssetResponse",
    "UserSpecifiedAnnotation",
    "ViewCollectionItemsRequest",
    "ViewCollectionItemsResponse",
    "ViewIndexedAssetsRequest",
    "ViewIndexedAssetsResponse",
    "FacetBucketType",
)
