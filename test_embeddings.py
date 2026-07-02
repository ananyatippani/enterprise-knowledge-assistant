from app.services.embeddings import create_embeddings

chunks = [
    "FastAPI is a modern Python framework.",
    "Machine learning enables intelligent systems."
]

embeddings = create_embeddings(chunks)

print(embeddings.shape)