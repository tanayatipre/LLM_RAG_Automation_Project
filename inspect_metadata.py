import pickle

# Load and inspect the function metadata
with open("function_metadata.pkl", "rb") as f:
    function_data = pickle.load(f)

# Print all registered functions and their details
print("\nRegistered Functions:")
for i, func in enumerate(function_data):
    print(f"{i + 1}. Name: {func['name']}, Description: {func['description']}, Category: {func['category']}")
