from fastapi import APIRouter, Depends
from src.extract_summarize import controller
from src.extract_summarize.dto import SummarizeRequestSchema
from sqlalchemy.orm import Session
from src.users.model import UserModel
from src.utils.db import get_db
from src.utils.helper import is_authenticated

extract_summarize_route = APIRouter(prefix="/extract")

@extract_summarize_route.post("/summarize")
async def summarize_agent(body: SummarizeRequestSchema, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return await controller.summarize_agent(body, db, user)