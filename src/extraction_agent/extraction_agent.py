from fastapi import APIRouter
from src.Schemas.dtos import AgentResponse
from src.utils.llm import agent
from pydantic import BaseModel
from src.extraction_agent.text_extract import get_pdf_text

agent_route = APIRouter(prefix="/agent")

class SummarizeRequestSchema(BaseModel):
    filename: str


@agent_route.post("/summarize", response_model=AgentResponse)
def summarize(body: SummarizeRequestSchema):
    
    page_content = get_pdf_text(body.filename)

    user_prompt = f"""Please summarize the document provided below:
    <document>
    {page_content}
    </document>"""
    
    result = agent(user_prompt)
    print(result)
    return AgentResponse(response=result)
    
    