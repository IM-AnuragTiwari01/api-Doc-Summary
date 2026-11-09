from pydantic import BaseModel

class SummarizeRequestSchema(BaseModel):
    stored_path: str