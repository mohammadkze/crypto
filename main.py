import json
from app.services.crypto_service import CryptoService
from app.models.request.crypto_request import CryptoListRequest

# # Initialize the service
crypto_service = CryptoService()

# # Fetch latest listings
request = CryptoListRequest(start=1, limit=10, convert="USD")
response = crypto_service.get_latest_listings(request)
print(json.dumps(response, indent=4))

