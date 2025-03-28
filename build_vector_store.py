from sentence_transformers import SentenceTransformer
import faiss
import pickle
from function_metadata import function_data

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Prepare data
texts = [f"{item['name']} - {item['description']} - {item['category']}" for item in function_data]
embeddings = model.encode(texts)

# Create FAISS index
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and metadata
faiss.write_index(index, "functions.index")

with open("function_metadata.pkl", "wb") as f:
    pickle.dump(function_data, f)

print("Vector store built and saved.")
