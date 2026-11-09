from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
    
class ContentLibraryResponseSchema(BaseModel):
        
    id: Optional[UUID] = None
    original_name: Optional[str] = None
    created_at: Optional[datetime] = None
    stored_path: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)