from langchain.document_loaders import DirectoryLoader, PyPDFLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Extract data from the PDF file
def load_pdf_file(path):
    loader= DirectoryLoader(path, 
                            glob="*.pdf",
                            loader_cls=PyPDFLoader)
    documents= loader.load()
    return documents

# Split the data into chunks
def split_text(extracted_data):
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks= text_splitter.split_documents(extracted_data)
    return text_chunks

# Download embeddings from HuggingFace
def download_embeddings():
    embeddings= HuggingFaceEmbeddings(model_name= 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings