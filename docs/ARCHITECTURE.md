# Enterprise Knowledge Assistant Architecture

## Overview

The Enterprise Knowledge Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions using natural language.

The system retrieves the most relevant document sections using semantic search before generating an answer with a Large Language Model (LLM).

---

## Architecture

```text
                 User

                   │
                   ▼

            Upload PDF (FastAPI)

                   │
                   ▼

           PDF Text Extraction

                   │
                   ▼

             Smart Chunking

                   │
                   ▼

      Sentence Transformer Embeddings

                   │
                   ▼

          ChromaDB Vector Database

                   │
                   ▼

           Semantic Similarity Search

                   │
                   ▼

          Retrieved Context Chunks

                   │
                   ▼

             Google Gemini LLM

                   │
                   ▼

             Final AI Response
```

---

## Components

### FastAPI

Provides REST API endpoints for uploading PDFs and querying the knowledge base.

### PDF Processor

Extracts text from uploaded PDF documents using PyMuPDF.

### Text Chunker

Splits long documents into overlapping chunks while preserving semantic meaning.

### Embedding Service

Uses Sentence Transformers to convert text into dense vector embeddings.

Model:

- all-MiniLM-L6-v2

### ChromaDB

Stores document embeddings for efficient semantic retrieval.

### RAG Pipeline

The Retrieval-Augmented Generation pipeline performs:

1. Query embedding
2. Vector search
3. Context retrieval
4. LLM response generation

### Google Gemini

Uses retrieved document context to generate accurate answers while minimizing hallucinations.

---

## Technology Stack

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- PyTorch
- Google Gemini
- PyMuPDF
- Uvicorn

---

## Future Improvements

- Multi-document support
- Metadata filtering
- Conversation memory
- Authentication
- Docker deployment
- CI/CD
- React frontend
- User management
- Streaming responses
- OCR for scanned PDFs