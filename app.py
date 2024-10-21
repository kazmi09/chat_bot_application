import torch
import numpy as np
from sentence_transformers import SentenceTransformer, util
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
sentence_encoder_model = SentenceTransformer('BAAI/bge-small-en', device='cpu')

origins = [
    "https://bounce-insights-chatbot.onrender.com", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_json_to_list(filename):
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []     
    
def create_embeddings(temp_texts,sentence_encoder_model):
    try:
        embeddings_bert_model = sentence_encoder_model.encode(temp_texts, normalize_embeddings=True)
        return embeddings_bert_model
    except Exception as ex:
        return ex



#model prefix
prefix="Represent this sentence for searching hrelevant passages:"
#read the generated embedded files of dataset1
content_embedding_list=read_json_to_list("embedding_file.txt")
#read the generated chunk files of dataset1
chunks_content_list=read_json_to_list("chunks_file.txt")
embeddings=[]
for embedding in content_embedding_list:
    embeddings.append(embedding['embedding'])



class QueryRequest(BaseModel):
    query: str


client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)
def chat_gpt(question,context):
    try:
        prompt = f"{context}\n\nQuestion: {question}\nAnswer:"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as ex:
        return ex

@app.post("/query/")
async def get_response(query_request: QueryRequest):
   
   try:
        prefix = "Represent this sentence for searching relevant passages:"
        query = prefix + query_request.query
        
        query_embeddings = create_embeddings(query,sentence_encoder_model)
        cosine_scores = util.cos_sim(query_embeddings, embeddings)[0].tolist()
        
        results = [{'snippet': inp['chunk'], 'score': score} for inp, score in zip(chunks_content_list, cosine_scores)]
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
        sorted_results_json=json.dumps(sorted_results)
        system_prompt = (
        "You are a helpful chatbot.We will provide you a list semantically releated chunks and along with their score and info_id in an object called CONTENT. Please answer the user queries based on the following information:\n"
        f"CONTENT: {sorted_results_json}\n"
        )

        response = chat_gpt(query_request.query,system_prompt)
        return {"response": response}

   except Exception as ex:
        return ex

