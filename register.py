import os
import pickle
from sentence_transformers import SentenceTransformer
import faiss
from function_metadata import function_data
from build_vector_store import model  

CUSTOM_PATH = "custom_functions.py"
METADATA_PATH = "function_metadata.pkl"
INDEX_PATH = "functions.index"

def register_new_function(name, description, category, logic):
    # Save function logic to file
    with open(CUSTOM_PATH, "a") as f:
        f.write(f"\n\ndef {name}(n):\n")  # Added parameter for factorial
        for line in logic.split('\n'):
            f.write("    " + line + "\n")

    # Append to metadata
    new_entry = {"name": name, "description": description, "category": category}
    function_data.append(new_entry)

    # Rebuild vector store
    texts = [f"{item['name']} - {item['description']} - {item['category']}" for item in function_data]
    embeddings = model.encode(texts)
    dimension = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(function_data, f)

    return new_entry
