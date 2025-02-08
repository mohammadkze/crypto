from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")  # Generic type for data

class Status(BaseModel):
    timestamp: str
    error_code: int
    error_message: str | None
    elapsed: int
    credit_count: int
    notice: str | None

class BaseResponse(BaseModel, Generic[T]):
    status: Status
    data: T
