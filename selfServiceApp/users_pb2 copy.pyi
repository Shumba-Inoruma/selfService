from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
ERROR: Status
FAILED: Status
INFORMATION: Status
SUCCESS: Status

class Error(_message.Message):
    __slots__ = ["debugDescription", "localizedDescription"]
    DEBUGDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    debugDescription: str
    localizedDescription: str
    def __init__(self, localizedDescription: _Optional[str] = ..., debugDescription: _Optional[str] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ["information"]
    INFORMATION_FIELD_NUMBER: _ClassVar[int]
    information: str
    def __init__(self, information: _Optional[str] = ...) -> None: ...

class Success(_message.Message):
    __slots__ = ["debugDescription", "localizedDescription"]
    DEBUGDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALIZEDDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    debugDescription: str
    localizedDescription: str
    def __init__(self, localizedDescription: _Optional[str] = ..., debugDescription: _Optional[str] = ...) -> None: ...

class request(_message.Message):
    __slots__ = ["balance", "cdma", "debugInfo", "domain", "email", "package_id", "password", "token", "username", "verificationCode"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CDMA_FIELD_NUMBER: _ClassVar[int]
    DEBUGINFO_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    VERIFICATIONCODE_FIELD_NUMBER: _ClassVar[int]
    balance: float
    cdma: str
    debugInfo: str
    domain: str
    email: str
    package_id: str
    password: str
    token: str
    username: str
    verificationCode: str
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., password: _Optional[str] = ..., balance: _Optional[float] = ..., email: _Optional[str] = ..., package_id: _Optional[str] = ..., token: _Optional[str] = ..., verificationCode: _Optional[str] = ..., debugInfo: _Optional[str] = ..., cdma: _Optional[str] = ...) -> None: ...

class response(_message.Message):
    __slots__ = ["alias", "balance", "domain", "email", "error", "info", "password", "status", "success", "token", "username"]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
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
    alias: str
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
    def __init__(self, username: _Optional[str] = ..., domain: _Optional[str] = ..., password: _Optional[str] = ..., balance: _Optional[float] = ..., email: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., token: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., info: _Optional[_Union[Info, _Mapping]] = ..., success: _Optional[_Union[Success, _Mapping]] = ..., alias: _Optional[str] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
