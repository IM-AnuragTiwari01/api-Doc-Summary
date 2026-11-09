from fastapi import UploadFile, HTTPException, status
import aiofiles
from pathlib import Path
from src.extract_summarize.text_extract import get_pdf_text
from src.users.model import UserModel
import uuid
from sqlalchemy.orm import Session
from src.content_library.model import ContentLibrary


async def upload_files(file: UploadFile , db: Session,  user: UserModel):
    current_user_id = str(user.id)
    UPLOAD_DIR = Path(__file__).parent.parent / "documents" / "uploads" / current_user_id
    UPLOAD_DIR.mkdir(parents = True, exist_ok=True)
    
    new_file_id = uuid.uuid4()
    file_extension = file.filename.split(".")[-1]
    physical_file_name = f"{new_file_id}.{file_extension}"
    
    file_path = UPLOAD_DIR / physical_file_name
    
    # we are opening the file in "write-binary" mode
    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)
    
    new_content: ContentLibrary = ContentLibrary(
        id = new_file_id,
        user_id = user.id,
        original_name = file.filename,
        stored_path = str(file_path)
    )
    
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    
    return new_content


def my_uploads(db: Session, user: UserModel):
    current_user_id = user.id
    
    if not current_user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no user with user_id : {current_user_id}")
    
    if current_user_id:
        query = db.query(ContentLibrary).filter(ContentLibrary.user_id == current_user_id)
    
    return query.all()