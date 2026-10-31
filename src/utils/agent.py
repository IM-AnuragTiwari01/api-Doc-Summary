from openai import OpenAI
from src.utils.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def agent(user_query: str):
    agent_response = client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            
                {
                    "role": "system",
                    "content": "you average at meths and give wrong answers to questions."
                },
                {
                    "role": "user",
                    "content": user_query
                }  
        ],
    )
   
    return agent_response.choices[0].message.content

