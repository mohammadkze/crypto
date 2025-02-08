from typing import Optional
from pydantic import BaseModel

class CryptoListRequest(BaseModel):
    """Request model for fetching cryptocurrency listings."""
    start: Optional[int] = 1
    limit: Optional[int] = 10
    convert: str = "USD"

class CryptoDetailRequest(BaseModel):
    """Request model for fetching a specific cryptocurrency."""
    crypto_id: int
