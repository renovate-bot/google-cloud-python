
transport inheritance structure
_______________________________

`IssueResolutionServiceTransport` is the ABC for all transports.
- public child `IssueResolutionServiceGrpcTransport` for sync gRPC transport (defined in `grpc.py`).
- public child `IssueResolutionServiceGrpcAsyncIOTransport` for async gRPC transport (defined in `grpc_asyncio.py`).
- private child `_BaseIssueResolutionServiceRestTransport` for base REST transport with inner classes `_BaseMETHOD` (defined in `rest_base.py`).
- public child `IssueResolutionServiceRestTransport` for sync REST transport with inner classes `METHOD` derived from the parent's corresponding `_BaseMETHOD` classes (defined in `rest.py`).
