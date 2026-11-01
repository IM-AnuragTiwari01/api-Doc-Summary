from src.extraction_agent.text_extract import page_content
from fastapi import APIRouter
from src.Schemas.dtos import AgentResponse
from src.utils.llm import agent

agent_route = APIRouter(prefix="/agent")

user_prompt = f"""Please summarize the document provided below:

<document>
{page_content}
</document>
"""


@agent_route.post("/summarize", response_model=AgentResponse)
def summarize():
    result = agent(user_prompt)    
    print(result)
    return AgentResponse(response=result)