from fastapi import UploadFile, APIRouter, File, Depends
from src.content_library import controller
from src.utils.helper import is_authenticated
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.users.model import UserModel
from src.content_library.dto import ContentLibraryResponseSchema


content_library_route = APIRouter(prefix="/upload")

@content_library_route.post("/upload-file", response_model=ContentLibraryResponseSchema)
async def upload_files(file: UploadFile = File(...), db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return await controller.upload_files(file, db, user)

@content_library_route.get("/my-files", response_model=list[ContentLibraryResponseSchema])
def my_uploads(db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.my_uploads(db, user)
