import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("functions.index")

with open("function_metadata.pkl", "rb") as f:
    function_data = pickle.load(f)

def retrieve_function(user_query, top_k=1):
    # Load model, index, and metadata at the time of each request
    index = faiss.read_index("functions.index")

    with open("function_metadata.pkl", "rb") as f:
        function_data = pickle.load(f)

    query_embedding = model.encode([user_query])
    distances, indices = index.search(query_embedding, top_k)

    print(f"User query: {user_query}")
    print(f"Indices returned: {indices}")
    print(f"Distances: {distances}")
    
    results = []
    for idx in indices[0]:
        if idx < len(function_data):
            print(f"Function matched: {function_data[idx]}")  
            results.append(function_data[idx])
    return results[0] if results else None
