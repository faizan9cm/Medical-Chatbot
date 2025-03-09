# Medical-Chatbot
This project is an end-to-end medical chatbot utilizing the **Retrieval-Augmented Generation (RAG)** technique to enhance information retrieval from medical documents. The chatbot processes medical PDFs, extracts relevant content, generates embeddings, and stores them in **Pinecone**, a vector database, enabling efficient similarity search.  

The system is powered by **Llama 3.3 LLM** and is integrated into a **Streamlit** app, providing users with an interactive and context-aware conversational experience. This ensures accurate and relevant responses based on medical document queries.  

### Key Features:  
- **RAG-based chatbot** for enhanced medical document retrieval  
- **PDF processing pipeline** to extract and index content  
- **Pinecone vector database** for efficient similarity search  
- **Llama 3.3 LLM** for intelligent and context-aware responses  
- **Streamlit UI** for an interactive and user-friendly experience  

# How to run
### Steps:

Clone the repository 

```bash
Project repo: https://github.com/
```

### Step 01- Create a conda environment after opening the repository
```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

### Step 02- Install the requirements
```bash
pip install -r requirements.txt
```

### Step 03- Create a `.env` file in the root directory and add your Pinecone credentials as follows

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Llama_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Step 04- Use Llama 3.3
    # From the following link
    https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct


```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```

### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama3
- Pinecone
