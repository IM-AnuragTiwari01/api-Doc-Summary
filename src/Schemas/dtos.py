from pydantic import BaseModel, Field

class InputSchema(BaseModel):
    user_query: str = Field(..., min_length=1, description="User input text")
    
class AgentResponse(BaseModel):
    response: str