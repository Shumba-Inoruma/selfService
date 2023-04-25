from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DISPUTED: PaymentStatus
ERROR: Status
FAILED: PaymentStatus
FAILURE: Status
INFORMATION: Status
PAYNOW: PaymentMethod
PAYPAL: PaymentMethod
PENDING: PaymentStatus
STRIPE: PaymentMethod
SUCCESS: PaymentStatus
SUCCESSFUL: Status
VOUCHER: PaymentMethod

class Details(_message.Message):
    __slots__ = ["domain", "purchaseId", "username"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PURCHASEID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    domain: str
    purchaseId: str
    username: str
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., purchaseId: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ["debugDescription", "localizedDescription"]
    DEBUGDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    debugDescription: str
    localizedDescription: str
    def __init__(self, localizedDescription: _Optional[str] = ..., debugDescription: _Optional[str] = ...) -> None: ...

class Gift(_message.Message):
    __slots__ = ["amount", "destination", "domain", "source"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    amount: float
    destination: str
    domain: str
    source: str
    def __init__(self, source: _Optional[str] = ..., destination: _Optional[str] = ..., domain: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ["information"]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    information: str
    def __init__(self, information: _Optional[str] = ...) -> None: ...

class Payment(_message.Message):
    __slots__ = ["amount", "created", "domain", "method", "paymentType", "status", "transaction", "username"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PAYMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    amount: float
    created: str
    domain: str
    method: PaymentMethod
    paymentType: str
    status: PaymentStatus
    transaction: str
    username: str
    def __init__(self, username: _Optional[str] = ..., amount: _Optional[float] = ..., domain: _Optional[str] = ..., status: _Optional[_Union[PaymentStatus, str]] = ..., method: _Optional[_Union[PaymentMethod, str]] = ..., transaction: _Optional[str] = ..., created: _Optional[str] = ..., paymentType: _Optional[str] = ...) -> None: ...

class Success(_message.Message):
    __slots__ = ["debugDescription", "localizedDescription"]
    DEBUGDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    debugDescription: str
    localizedDescription: str
    def __init__(self, localizedDescription: _Optional[str] = ..., debugDescription: _Optional[str] = ...) -> None: ...

class information(_message.Message):
    __slots__ = ["amount", "count", "destination", "domain", "email", "source", "username"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    amount: float
    count: int
    destination: str
    domain: str
    email: str
    source: str
    username: str
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., source: _Optional[str] = ..., destination: _Optional[str] = ..., amount: _Optional[float] = ..., email: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class product(_message.Message):
    __slots__ = ["domain", "packageName", "productId", "token", "username"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    domain: str
    packageName: str
    productId: str
    token: str
    username: str
    def __init__(self, packageName: _Optional[str] = ..., productId: _Optional[str] = ..., token: _Optional[str] = ..., username: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class reply(_message.Message):
    __slots__ = ["balance", "domain", "email", "error", "info", "password", "status", "success", "token", "username"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    balance: float
    domain: str
    email: str
    error: Error
    info: Info
    password: str
    status: Status
    success: Success
    token: str
    username: str
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., password: _Optional[str] = ..., balance: _Optional[float] = ..., email: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., token: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., info: _Optional[_Union[Info, _Mapping]] = ..., success: _Optional[_Union[Success, _Mapping]] = ...) -> None: ...

class request(_message.Message):
    __slots__ = ["object", "payment"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    object: str
    payment: Payment
    def __init__(self, payment: _Optional[_Union[Payment, _Mapping]] = ..., object: _Optional[str] = ...) -> None: ...

class requests(_message.Message):
    __slots__ = ["amount", "balance", "debugInfo", "domain", "email", "package_id", "password", "receiver", "token", "transactionId", "username", "voucherPin"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    DEBUGINFO_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    VOUCHERPIN_FIELD_NUMBER: _ClassVar[int]
    amount: float
    balance: float
    debugInfo: str
    domain: str
    email: str
    package_id: str
    password: str
    receiver: str
    token: str
    transactionId: str
    username: str
    voucherPin: str
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., password: _Optional[str] = ..., balance: _Optional[float] = ..., email: _Optional[str] = ..., package_id: _Optional[str] = ..., token: _Optional[str] = ..., receiver: _Optional[str] = ..., amount: _Optional[float] = ..., voucherPin: _Optional[str] = ..., debugInfo: _Optional[str] = ..., transactionId: _Optional[str] = ...) -> None: ...

class response(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class transfer(_message.Message):
    __slots__ = ["destination", "source"]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    destination: Payment
    source: Payment
    def __init__(self, source: _Optional[_Union[Payment, _Mapping]] = ..., destination: _Optional[_Union[Payment, _Mapping]] = ...) -> None: ...

class verified(_message.Message):
    __slots__ = ["isVerified"]
    ISVERIFIED_FIELD_NUMBER: _ClassVar[int]
    isVerified: bool
    def __init__(self, isVerified: bool = ...) -> None: ...

class PaymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PaymentMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
