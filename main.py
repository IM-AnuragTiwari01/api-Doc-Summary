from fastapi import FastAPI
from src.utils.settings import settings
from src.utils.llm import agent
from src.extract_summarize.router import extract_summarize_route
from src.content_library.router import content_library_route
from src.utils.db import Base, engine
from src.users.router import user_route

Base.metadata.create_all(engine) # as soon as our server starts it connects to db

app = FastAPI(title= "Document Summarizer Agent")

app.include_router(extract_summarize_route)
app.include_router(content_library_route)
app.include_router(user_route)
