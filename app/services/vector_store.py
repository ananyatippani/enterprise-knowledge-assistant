import chromadb

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="documents"
)


def add_documents(chunks, embeddings):
    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )


def search(query_embedding, k=3):
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )

    return results