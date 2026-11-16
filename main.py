from fastapi import FastAPI
from src.utils.settings import settings
from src.utils.llm import agent
from src.extract_summarize.router import extract_summarize_route
from src.content_library.router import content_library_route
from src.utils.db import Base, engine
from src.users.router import user_route
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine) # as soon as our server starts it connects to db

app = FastAPI(title= "Document Summarizer Agent")
# --- CORS Configuration ---
origins = [
    "http://localhost:5173",    # Vite default port
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------
app.include_router(extract_summarize_route)
app.include_router(content_library_route)
app.include_router(user_route)
