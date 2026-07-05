from uuid import uuid4
from typing import List

import chromadb


def get_collection():
    client = chromadb.PersistentClient(path="vector_db")

    return client.get_or_create_collection(
        name="documents"
    )


def add_documents(
    chunks: List[str],
    embeddings,
    source: str = "Unknown Document"
):

    collection = get_collection()

    ids = [
        str(uuid4())
        for _ in chunks
    ]

    metadatas = [
        {
            "source": source,
            "chunk": i + 1
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


def search(
    query_embedding,
    k: int = 5
):

    collection = get_collection()

    return collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )