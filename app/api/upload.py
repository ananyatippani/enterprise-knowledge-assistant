from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(tags=["Upload"])

UPLOAD_FOLDER = Path("data/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    destination = UPLOAD_FOLDER / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF uploaded successfully!",
        "filename": file.filename,
        "saved_to": str(destination)
    }