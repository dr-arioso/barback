from pydantic import BaseModel, Field
from typing import Optional

class BackendConfig(BaseModel):
    name: str = "bottle"
    google_service_account_json: Optional[str] = None
    openai_api_key: Optional[str] = None

class AppConfig(BaseModel):
    resolver: BackendConfig = Field(default_factory=BackendConfig)
