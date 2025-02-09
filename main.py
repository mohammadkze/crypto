import json
from app.services.crypto_service import CryptoService
from app.models.request.crypto_request import CryptoListRequest
from app.config.crud_generator import EndpointCategory, APIVersion
# # Initialize the service
crypto_service = CryptoService()


request = CryptoListRequest(start=1, limit=10, convert="USD")
response = crypto_service.get_latest_listings(EndpointCategory.CRYPTOCURRENCY, "listings/latest", request, APIVersion.V1)
print(json.dumps(response, indent=4))

# # Fetch latest listings
request = CryptoListRequest(start=1, limit=10, convert="")
res2 = crypto_service.get_fear_and_greed(EndpointCategory.FEAR_AND_GREED, "historical", request, APIVersion.V3)
print(json.dumps(res2, indent=4))