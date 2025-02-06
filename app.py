from flask import Flask, render_template, request, jsonify
from src.helper import download_embeddings
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from src.prompt import system_prompt
import os
print(os.getcwd())

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY= os.getenv("PINECONE_API_KEY")
Llama_API_KEY = os.getenv("Llama_API_KEY")

os.environ["PINECONE_API_KEY"]= PINECONE_API_KEY
os.environ["Llama_API_KEY"]= Llama_API_KEY

embeddings = download_embeddings()

index_name = "medibot-index"

# Load existing index
from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":4})

# Define Llama model
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-70B-Instruct",
    huggingfacehub_api_token=Llama_API_KEY,
    task="text-generation"  # Explicitly define the task
)

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["context", "input"], 
    template="{{system_prompt}}\nUse the following context to answer the question:\n{context}\n\nQuestion: {input}\nAnswer:"
)

# Create the combine docs chain
combine_docs_chain = create_stuff_documents_chain(llm, prompt)
# Create the retrieval chain properly
rag_chain = create_retrieval_chain(retriever, combine_docs_chain) 


@app.route("/")
def index():
    return render_template('chatbot.html')

@app.route('/get', methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print("User input:", input)
    response = rag_chain.invoke({"input": msg})
    print("Response:", response.get("answer", "No answer found"))
    return str(response.get("answer", "No answer found"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
