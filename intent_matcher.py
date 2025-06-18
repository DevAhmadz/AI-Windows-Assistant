import json
from sentence_transformers import SentenceTransformer, util

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load training phrases from intents.json
with open("intents.json", "r") as f:
    intent_examples = json.load(f)

# Build intent embeddings
intent_embeddings = {}
for intent, examples in intent_examples.items():
    intent_embeddings[intent] = model.encode(examples, convert_to_tensor=True)

def get_intent(user_input, threshold=0.6):
    """Return the best matching intent for user input."""
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    best_intent = None
    best_score = 0.0

    for intent, embeddings in intent_embeddings.items():
        scores = util.pytorch_cos_sim(user_embedding, embeddings)
        max_score = scores.max().item()
        if max_score > best_score:
            best_score = max_score
            best_intent = intent

    return best_intent if best_score >= threshold else None
