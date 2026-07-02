from app.services.embeddings import create_embeddings
from app.services.vector_store import add_documents

chunks = [
    "FastAPI is a modern Python framework.",
    "Machine learning enables intelligent systems.",
    "Large Language Models can answer questions.",
]

embeddings = create_embeddings(chunks)

add_documents(chunks, embeddings)

print("Documents stored successfully!")