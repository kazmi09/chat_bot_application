import torch
import numpy as np
from sentence_transformers import SentenceTransformer, util
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

sentence_encoder_model = SentenceTransformer('BAAI/bge-small-en', device='cpu')


def read_json_to_list(filename):
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []     
    
def create_embeddings(temp_texts,sentence_encoder_model):
   #with torch.no_grad(): 
    embeddings_bert_model = sentence_encoder_model.encode(temp_texts, normalize_embeddings=True)
    return embeddings_bert_model



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



@app.post("/query/")
async def get_response(query_request: QueryRequest):
    prefix = "Represent this sentence for searching relevant passages:"
    query = prefix + query_request.query
    
    query_embeddings = create_embeddings(query,sentence_encoder_model)
    cosine_scores = util.cos_sim(query_embeddings, embeddings)[0].tolist()
    
    results = [{'snippet': inp['chunk'], 'score': score} for inp, score in zip(chunks_content_list, cosine_scores)]
    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
    
    return sorted_results
