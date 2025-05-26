from typing import TypeVar, Generic, Optional

from pydantic import BaseModel


T = TypeVar('T')


class ResponseSchema(BaseModel, Generic[T]):
    message: str
    data: Optional[T] = None
    success: bool
    status_code: int