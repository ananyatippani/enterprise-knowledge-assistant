from app.services.text_chunker import chunk_text


def test_chunker():

    text = """

Artificial Intelligence

Machine Learning

Deep Learning

Large Language Models

"""

    chunks = chunk_text(text)

    assert len(chunks) > 0
    assert isinstance(chunks[0], str)