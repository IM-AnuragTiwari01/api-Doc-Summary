from fastapi import FastAPI
from src.utils.settings import settings
from src.Schemas.dtos import InputSchema, AgentResponse
from src.utils.agent import agent

app = FastAPI(title= "Document Summarizer Agent")


@app.post("/agent-test", response_model=AgentResponse)
def agent_test(body: InputSchema):
    query: str = body.user_query
    result = agent(query)
    
    print(result)
    return AgentResponse(response=result)