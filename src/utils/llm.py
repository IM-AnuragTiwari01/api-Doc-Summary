from openai import OpenAI
from src.utils.settings import settings
from src.utils.system_prompt import SYSTEM_PROMPT

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def agent(user_prompt: str):
    agent_response = client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }  
        ],
    )
   
    return agent_response

