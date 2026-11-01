from fastapi import UploadFile, File, APIRouter
import aiofiles
from pathlib import Path
from src.extraction_agent.text_extract import get_pdf_text

file_upload_route = APIRouter(prefix="/upload")

UPLOAD_DIR = Path(__file__).parent.parent / "documents" / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

@file_upload_route.post("/upload-file")
async def upload_files(file: UploadFile = File(...)):
    file_name = file.filename
    file_path = UPLOAD_DIR / file.filename
    
    # we are opening the file in "write-binary" mode
    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)
    
    extracted_text = get_pdf_text(file_name)
    
    return {
        "filename": file.filename
    }