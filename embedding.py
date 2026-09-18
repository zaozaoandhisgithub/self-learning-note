from foundry_local_sdk import Configuration, FoundryLocalManager
import numpy as np
    
FoundryLocalManager.initialize(Configuration(app_name="assignment"))
model = FoundryLocalManager.instance.catalog.get_model("qwen3-embedding-0.6b")
model.download(); model.load()
client = model.get_embedding_client()

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

text = 'the quick brown fox jumped over the lazy dog'
response = client.generate_embedding("The quick brown fox jumps over the lazy dog")
embedding = response.data[0].embedding
automobile_embedding  = client.generate_embedding("automobile").data[0].embedding
vehicle_embedding     = client.generate_embedding("vehicle").data[0].embedding
dinosaur_embedding    = client.generate_embedding("dinosaur").data[0].embedding
stick_embedding       = client.generate_embedding("stick").data[0].embedding

print(cosine_similarity(automobile_embedding, vehicle_embedding))
print(cosine_similarity(automobile_embedding, dinosaur_embedding))
print(cosine_similarity(automobile_embedding, stick_embedding))
