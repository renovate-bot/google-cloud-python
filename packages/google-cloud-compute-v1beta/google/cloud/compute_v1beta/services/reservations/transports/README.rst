
transport inheritance structure
_______________________________

`ReservationsTransport` is the ABC for all transports.
- public child `ReservationsGrpcTransport` for sync gRPC transport (defined in `grpc.py`).
- public child `ReservationsGrpcAsyncIOTransport` for async gRPC transport (defined in `grpc_asyncio.py`).
- private child `_BaseReservationsRestTransport` for base REST transport with inner classes `_BaseMETHOD` (defined in `rest_base.py`).
- public child `ReservationsRestTransport` for sync REST transport with inner classes `METHOD` derived from the parent's corresponding `_BaseMETHOD` classes (defined in `rest.py`).
