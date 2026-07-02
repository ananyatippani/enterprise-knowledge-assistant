from sentence_transformers import SentenceTransformer

# Load the model only once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(chunks)
    return embeddings