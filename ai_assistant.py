import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import numpy as np
from sentence_transformers import SentenceTransformer, util
import json
from openai import OpenAI
from transformers import pipeline


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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"
)

def chat_gpt(question,context):
    prompt = f"{context}\n\nQuestion: {question}\nAnswer:"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def create_embeddings(temp_texts,sentence_encoder_model):
   #with torch.no_grad(): 
    embeddings_bert_model = sentence_encoder_model.encode(temp_texts, normalize_embeddings=True)
    return embeddings_bert_model



def read_json_to_list(filename):
    try:
        # Open and read the JSON data from the file
        with open(filename, 'r') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []        
        
        # Create a list to store the values
        values_list = []

prefix="Represent this sentence for searching hrelevant passages:"
sentence_encoder_model = SentenceTransformer('BAAI/bge-small-en',device='cpu')
content_embedding_list=read_json_to_list("embedding_file.txt")
chunks_content_list=read_json_to_list("chunks_file.txt")
embeddings=[]
for embedding in content_embedding_list:
    embeddings.append(embedding['embedding'])


# Chat loop
print("Chatbot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    query=prefix+user_input
    query_embeddings=create_embeddings(query,sentence_encoder_model)
    cosine_scores = util.cos_sim(query_embeddings, embeddings)[0].tolist()
    results = [{'snippet': inp['chunk'], 'score': score} for inp, score in zip(chunks_content_list, cosine_scores)]
    sorted_results = sorted(results, key=lambda x: x['score'],reverse=True)
    sorted_results_json=json.dumps(sorted_results)
    system_prompt = (
    "You are a helpful chatbot.We will provide you a list semantically releated chunks and along with their score and info_id in an object called CONTENT. Please answer the user queries based on the following information:\n"
    f"CONTENT: {sorted_results_json}\n"
    )
    
    response = chat_gpt(user_input,system_prompt)#chat_with_bot(prompt)
    
    print(f"Chatbot: {response}")
