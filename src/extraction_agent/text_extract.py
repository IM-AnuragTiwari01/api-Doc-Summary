from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

curr_dir = Path(__file__).parent.parent
doc_path = curr_dir/ "documents"/ "resume.pdf"

loader = PyPDFLoader(
    file_path = doc_path
)

docs = loader.load()
page_content = docs[0].page_content






