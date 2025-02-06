from src.helper import load_pdf_file, split_text, download_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY= os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"]= PINECONE_API_KEY

extracted_data= load_pdf_file(data="data/")
text_chunks= split_text(extracted_data)
embeddings = download_embeddings()

pc = Pinecone(api_key= PINECONE_API_KEY)

index_name = "medibot-index"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

# Embed each chunk and add to the Pinecone index
from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)