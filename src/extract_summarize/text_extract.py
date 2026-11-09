from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from fastapi import APIRouter




def get_pdf_text(file_path: str):
    # Base uploads path: src/documents/uploads
    UPLOAD_DIR = file_path
    doc_path = UPLOAD_DIR 
    
    loader = PyPDFLoader(file_path=doc_path)
    docs = loader.load()
    
    # for logging
    print()
    print("-------------------------------*** LOGGING ***---------------------------------------------------")
    print(docs[0].page_content)
    print("-------------------------------*** LOGGING ***---------------------------------------------------")
    print()
    return docs[0].page_content






