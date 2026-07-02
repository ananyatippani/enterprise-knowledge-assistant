# 🚀 Enterprise Knowledge Assistant

An AI-powered Enterprise Knowledge Assistant built using **FastAPI**, **LangChain**, **ChromaDB**, and **Large Language Models (LLMs)**. The application enables intelligent document understanding through Retrieval-Augmented Generation (RAG), semantic search, and conversational AI.

---

## ✨ Features

- 📄 PDF document upload
- 📑 Automatic text extraction
- ✂️ Intelligent text chunking
- 🔍 Semantic document search *(Coming Soon)*
- 🧠 Retrieval-Augmented Generation (RAG) *(Coming Soon)*
- 💬 AI-powered question answering *(Coming Soon)*
- ⚡ FastAPI REST API
- 📚 Interactive Swagger API Documentation
- 🐳 Docker support *(Coming Soon)*
- 🔐 Authentication *(Coming Soon)*

---

## 🏗️ Project Architecture

```
                    PDF Documents
                          │
                          ▼
                    Upload API (FastAPI)
                          │
                          ▼
                 Document Processing
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
 Text Extraction                     Text Chunking
        │                                   │
        └─────────────────┬─────────────────┘
                          ▼
                  Embedding Generation
                          │
                          ▼
                      ChromaDB
                          │
                          ▼
                  Semantic Retrieval
                          │
                          ▼
              Large Language Model (LLM)
                          │
                          ▼
                   AI Generated Answer
```

---

## 🛠️ Technology Stack

### Backend

- FastAPI
- Python 3.12

### AI & Machine Learning

- LangChain
- Hugging Face Transformers
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

### Vector Database

- ChromaDB

### API

- REST APIs
- Swagger UI

### Tools

- Git
- GitHub
- Docker *(Coming Soon)*

---

## 📂 Project Structure

```
enterprise-knowledge-assistant/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── utils/
│   ├── prompts/
│   ├── config.py
│   ├── models.py
│   └── main.py
│
├── data/
│   ├── uploads/
│   └── processed/
│
├── vector_db/
├── tests/
├── docs/
├── screenshots/
├── notebooks/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/ananyatippani/enterprise-knowledge-assistant.git
cd enterprise-knowledge-assistant
```

### Create a virtual environment

```bash
python3 -m venv venv
```

### Activate the environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📸 Current Progress

✅ FastAPI backend

✅ Project architecture

✅ PDF upload API

✅ PDF text extraction

✅ Text chunking

🚧 Embedding generation

🚧 ChromaDB integration

🚧 Semantic search

🚧 RAG pipeline

🚧 Conversational AI

🚧 Docker deployment

---

## 🗺️ Roadmap

### Phase 1

- [x] FastAPI Backend
- [x] PDF Upload
- [x] Document Processing

### Phase 2

- [ ] Sentence Transformer Embeddings
- [ ] ChromaDB Integration
- [ ] Semantic Search

### Phase 3

- [ ] Retrieval-Augmented Generation (RAG)
- [ ] OpenAI / Gemini Integration
- [ ] Conversational AI

### Phase 4

- [ ] Authentication
- [ ] User Management
- [ ] Multi-document Support

### Phase 5

- [ ] Docker
- [ ] GitHub Actions
- [ ] Cloud Deployment

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome. Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Ananya Sai Tippani**

- LinkedIn: https://www.linkedin.com/in/ananya-tippani-5025b2269/
- Portfolio: https://ananyasaitippani.my.canva.site/
