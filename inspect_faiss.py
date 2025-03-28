import faiss

# Load the FAISS index
index = faiss.read_index("functions.index")

# Get the number of stored functions (embeddings)
num_functions = index.ntotal
print(f"Number of functions in FAISS index: {num_functions}")

# Optionally inspect first 5 embeddings and distances
import numpy as np
dummy_query = np.random.random((1, 384)).astype("float32")  # Random embedding
distances, indices = index.search(dummy_query, 5)  # Retrieve top 5 matches

print("Sample indices and distances (for testing):")
print("Indices:", indices)
print("Distances:", distances)
