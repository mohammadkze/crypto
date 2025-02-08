from typing import List, Dict, Optional
from pydantic import BaseModel
from app.models.response.base_response import BaseResponse


class Quote(BaseModel):
    price: float
    volume_24h: float
    volume_change_24h: float
    percent_change_1h: float
    percent_change_24h: float
    percent_change_7d: float
    market_cap: float
    market_cap_dominance: float
    fully_diluted_market_cap: float
    last_updated: str


class CryptoModel(BaseModel):
    id: int
    name: str
    symbol: str
    slug: str
    cmc_rank: int
    num_market_pairs: int
    circulating_supply: int
    total_supply: int
    max_supply: Optional[int]
    infinite_supply: Optional[bool]
    last_updated: str
    date_added: str
    tags: List[str]
    platform: Optional[Dict]
    self_reported_circulating_supply: Optional[float]
    self_reported_market_cap: Optional[float]
    quote: Dict[str, Quote]  # Example: {"USD": Quote(...)}


class CryptoResponse(BaseResponse[List[CryptoModel]]):
    pass
