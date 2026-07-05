from app.services.embeddings import create_embeddings


def test_embeddings():

    embeddings = create_embeddings(
        ["Artificial Intelligence"]
    )

    assert embeddings.shape[0] == 1
    assert embeddings.shape[1] == 384