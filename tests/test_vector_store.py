from app.services.embeddings import create_embeddings
from app.services.vector_store import add_documents, search


def test_vector_store():

    docs = [
        "Artificial Intelligence",
        "Machine Learning"
    ]

    embeddings = create_embeddings(docs)

    add_documents(
        docs,
        embeddings,
        source="test.pdf"
    )

    query = create_embeddings(
        ["Artificial Intelligence"]
    )[0]

    results = search(query)

    assert len(results["documents"][0]) > 0