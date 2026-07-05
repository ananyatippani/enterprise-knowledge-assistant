from typing import Dict, List

from app.services.embeddings import create_embeddings
from app.services.vector_store import search
from app.services.llm import generate_answer
from app.utils.logger import logger


def ask_question(question: str) -> Dict:
    """
    Complete Retrieval-Augmented Generation (RAG) pipeline.

    Steps:
    1. Convert the user question into an embedding.
    2. Perform semantic search in ChromaDB.
    3. Retrieve the most relevant document chunks.
    4. Build the context for the LLM.
    5. Generate a final answer using Gemini.
    """

    logger.info("=" * 60)
    logger.info("Starting RAG Pipeline")
    logger.info(f"Question: {question}")

    try:
        # Step 1: Create query embedding
        logger.info("Generating query embedding...")

        query_embedding = create_embeddings([question])[0]

        logger.info("Embedding generated successfully.")

        # Step 2: Semantic Search
        logger.info("Searching ChromaDB...")

        results = search(query_embedding)

        documents: List[str] = results.get("documents", [[]])[0]

        if not documents:
            logger.warning("No relevant documents found.")

            return {
                "question": question,
                "answer": "I couldn't find any relevant information in the uploaded documents.",
                "sources": []
            }

        logger.info(f"Retrieved {len(documents)} relevant chunks.")

        # Step 3: Build Context
        logger.info("Building context...")

        context = "\n\n".join(documents)

        # Step 4: Generate Answer
        logger.info("Generating Gemini response...")

        answer = generate_answer(
            question=question,
            context=context
        )

        logger.info("Gemini response generated successfully.")

        logger.info("RAG Pipeline completed successfully.")
        logger.info("=" * 60)

        return {
            "question": question,
            "answer": answer,
            "sources": documents
        }

    except Exception as e:

        logger.exception("RAG Pipeline failed.")

        return {
            "question": question,
            "answer": f"An error occurred while processing your request: {str(e)}",
            "sources": []
        }