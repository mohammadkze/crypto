import os
import requests
import json
from typing import Optional, Dict, Any, Union
from enum import Enum
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class APIVersion(Enum):
    V1 = "v1"
    V2 = "v2"

class RequestGenerator:
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None, 
                 header: Optional[Dict[str, str]] = None) -> None:
        """Initialize with base URL and API Key from environment variables."""
        self.base_url: str = base_url or os.getenv("API_URL", "")
        self.api_key: str = api_key or os.getenv("API_KEY", "")
        
        self.session: requests.Session = requests.Session()
        self.session.headers.update({
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key
        })

        if header:
            self.session.headers.update(header)

    def get(self, endpoint: str, version: APIVersion = APIVersion.V1,
            params: Optional[Dict[str, Union[str, int, float]]] = None) -> Dict[str, Any]:
        """Send a GET request to the API with versioning."""
        url: str = f"{self.base_url}/{version.value}/{endpoint}"
        print(f"url = {url}")
        try:
            response: requests.Response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def post(self, endpoint: str, version: APIVersion = APIVersion.V1,
             data: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send a POST request to the API with versioning."""
        url: str = f"{self.base_url}/{version.value}/{endpoint}"
        try:
            response: requests.Response = self.session.post(url, data=data, json=json_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
