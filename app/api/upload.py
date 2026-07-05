from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_processor import extract_text
from app.services.text_chunker import chunk_text
from app.services.embeddings import create_embeddings
from app.services.vector_store import add_documents

router = APIRouter(tags=["Upload"])

UPLOAD_FOLDER = Path("data/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:

        if Path(file.filename).suffix.lower() != ".pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported."
            )

        destination = UPLOAD_FOLDER / file.filename

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # -----------------------------
        # AI Pipeline
        # -----------------------------

        text = extract_text(destination)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No text could be extracted from the PDF."
            )

        chunks = chunk_text(text)

        embeddings = create_embeddings(chunks)

        add_documents(
            chunks,
            embeddings
        )

        return {
            "status": "success",
            "filename": file.filename,
            "chunks": len(chunks),
            "message": "Document processed successfully."
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )