from app.config.request_generator import RequestGenerator, APIVersion
from app.models.request.crypto_request import CryptoListRequest
from app.models.response.crypto_response import CryptoResponse
from typing import Optional

class CryptoService(RequestGenerator):
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        """Inherit from RequestGenerator to handle cryptocurrency-related API requests."""
        super().__init__(base_url, api_key)

    def get_latest_listings(self, request: CryptoListRequest, version: APIVersion = APIVersion.V1) -> CryptoResponse:
        """Fetch the latest cryptocurrency listings with request model."""
        endpoint = "cryptocurrency/listings/latest"
        response = self.get(endpoint, version, params=request)

        # Convert to Pydantic model
        crypto_response = CryptoResponse(**response)

        # Return a dictionary (which is JSON serializable)
        return crypto_response.model_dump()
