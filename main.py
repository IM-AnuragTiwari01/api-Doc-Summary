from fastapi import FastAPI
from src.utils.settings import settings
from src.Schemas.dtos import InputSchema, AgentResponse
from src.utils.llm import agent
from src.extraction_agent.extraction_agent import agent_route
from src.file_upload.file_upload import file_upload_route
from src.utils.db import Base, engine

Base.metadata.create_all(engine) # as soon as our server starts it connects to db

app = FastAPI(title= "Document Summarizer Agent")

app.include_router(agent_route)
app.include_router(file_upload_route)
