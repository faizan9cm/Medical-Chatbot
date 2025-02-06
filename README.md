# Medical-Chatbot

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
    ## From the following link
https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-70B-Instruct


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