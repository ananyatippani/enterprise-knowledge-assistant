from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_processor import extract_text
from app.services.text_chunker import chunk_text
from app.services.embeddings import create_embeddings
from app.services.vector_store import add_documents
from app.utils.logger import logger

router = APIRouter(tags=["Upload"])

UPLOAD_FOLDER = Path("data/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, process it, generate embeddings,
    and store everything in ChromaDB.
    """

    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    # Save uploaded PDF
    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"Uploaded PDF: {file.filename}")

    try:
        # Extract text
        text = extract_text(destination)
        logger.info("Text extracted successfully.")

        # Chunk text
        chunks = chunk_text(text)
        logger.info(f"Created {len(chunks)} chunks.")

        # Generate embeddings
        embeddings = create_embeddings(chunks)
        logger.info("Embeddings generated successfully.")

        # Store in ChromaDB
        add_documents(
            chunks=chunks,
            embeddings=embeddings,
            source=file.filename
        )

        logger.info("Document stored in ChromaDB.")

        return {
            "status": "success",
            "filename": file.filename,
            "chunks": len(chunks),
            "message": "Document processed successfully."
        }

    except Exception as e:
        logger.exception("Error processing uploaded PDF.")

        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )