from pydantic import BaseModel
from typing import Optional, Any


class ResponseDTO(BaseModel):
    message: Optional[str] = None
    data: Optional[Any] = None
