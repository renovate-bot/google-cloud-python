
transport inheritance structure
_______________________________

`OperatingSystemServiceTransport` is the ABC for all transports.
- public child `OperatingSystemServiceGrpcTransport` for sync gRPC transport (defined in `grpc.py`).
- public child `OperatingSystemServiceGrpcAsyncIOTransport` for async gRPC transport (defined in `grpc_asyncio.py`).
- private child `_BaseOperatingSystemServiceRestTransport` for base REST transport with inner classes `_BaseMETHOD` (defined in `rest_base.py`).
- public child `OperatingSystemServiceRestTransport` for sync REST transport with inner classes `METHOD` derived from the parent's corresponding `_BaseMETHOD` classes (defined in `rest.py`).
