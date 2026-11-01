from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# Base uploads path: src/documents/uploads
UPLOAD_DIR = Path(__file__).resolve().parent.parent / "documents" / "uploads"

def get_pdf_text(file_name: str):
    doc_path = UPLOAD_DIR / file_name
    
    loader = PyPDFLoader(file_path=str(doc_path))
    docs = loader.load()
    
    # docs[0].page_content gets the first page
    return docs[0].page_content






