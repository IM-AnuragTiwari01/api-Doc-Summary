from fastapi.concurrency import run_in_threadpool
from src.extract_summarize.dto import SummarizeRequestSchema, JobDescRequestSchema
from sqlalchemy.orm import Session
from src.users.model import UserModel
from src.extract_summarize.text_extract import get_pdf_text
from src.utils.llm import agent

async def summarize_agent(body: SummarizeRequestSchema, db: Session, user: UserModel):
    
    stored_path = body.stored_path
    
    # extracted text will be returned to this place
    extracted_text = await run_in_threadpool(get_pdf_text, stored_path)
    
    user_prompt = f""""
    you need to summarize this below document.
    Here is the document context:
    <document>
    {extracted_text}
    </document>
    """
    
    response = await run_in_threadpool(agent, user_prompt)
    print()
    print("-------------------------------*** LOGGING ***---------------------------------------------------")
    print(response.usage)
    print("-------------------------------*** LOGGING ***---------------------------------------------------")
    print()
    return {
        "summary": response.choices[0].message.content
    }
    
async def assisstance_from_job_description(body: JobDescRequestSchema, db: Session, user: UserModel):
    
    stored_path = body.stored_path
    job_description = body.job_description
    extracted_text = await run_in_threadpool(get_pdf_text, stored_path)
    user_prompt = f""""
        you need to summarize this below document.
        Here is the document context:
        
        <document>
        {extracted_text}
        </document>
        
        below is the job description provided by the user list down the matched and unmatched 
        skills as pointers also what all skill can be further mentioned in the skills or other
        sections of the resume with respected job description.
        <document>
        {job_description}
        </document>
        """
    response = await run_in_threadpool(agent, user_prompt)
    print()
    print("-------------------------------*** LOGGING ***---------------------------------------------------")
    print(response.usage)
    print("-------------------------------*** LOGGING ***---------------------------------------------------")
    print()
    return {
            "summary": response.choices[0].message.content
    }