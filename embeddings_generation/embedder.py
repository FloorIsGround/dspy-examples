import dspy
import os
from ollama import Client
import pprint

from dotenv import load_dotenv
load_dotenv()

ollama = Client(
    host=os.getenv("OLLAMA_HOST") # If using ollama and locally hosting a small embedding model
)

def call_embedder(texts):
    # model used is bge-m3 a 567m paramater embedding model
    # has an 8k context max
    # https://ollama.com/library/bge-m3
    response = ollama.embed(model="bge-m3", input=texts) 
    if "embeddings" in response:
        vecs = response["embeddings"]
    elif "embedding" in response:
        vecs = [response["embedding"]]
    else:
        raise RuntimeError(f"Unexpected embed response keys {list(response.keys())}")
    return vecs[0] if isinstance(texts, str) else vecs

embedder = dspy.Embedder(call_embedder)
embeddings = embedder(["hello", "world"])


pprint.pprint(embeddings)
