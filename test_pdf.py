from pathlib import Path

from app.services.pdf_processor import extract_text
from app.services.text_chunker import chunk_text

pdf_path = Path("data/uploads/sample.pdf")

text = extract_text(pdf_path)

if not text.strip():
    print("❌ No text could be extracted.")
    exit()

print("=" * 50)
print("TEXT PREVIEW")
print("=" * 50)
print(text[:500])

chunks = chunk_text(text)

print("\n" + "=" * 50)
print("CHUNK INFORMATION")
print("=" * 50)

print(f"Total Chunks: {len(chunks)}")

if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0])
else:
    print("No chunks created.")