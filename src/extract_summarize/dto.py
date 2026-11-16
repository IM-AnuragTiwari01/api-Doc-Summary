from pydantic import BaseModel

class SummarizeRequestSchema(BaseModel):
    stored_path: str

class JobDescRequestSchema(BaseModel):
    job_description:str
    stored_path: str