# 📚 RAG (Retrieval-Augmented Generation) Learning Journey

This repository contains my hands-on learning journey for building **Retrieval-Augmented Generation (RAG)** applications using **LangChain**, **OpenAI**, and **ChromaDB**.

The goal of this repository is not only to build RAG applications but also to understand **how RAG works internally**, following an incremental learning approach similar to how enterprise systems are designed.

---

# 🎯 Learning Objectives

- Understand the complete RAG architecture
- Learn how embeddings work
- Learn vector databases
- Build RAG from scratch
- Understand document chunking
- Implement semantic search
- Learn prompt augmentation
- Build enterprise-style RAG pipelines
- Prepare for Data Engineer / GenAI Engineer interviews

---

# 🛠️ Technology Stack

- Python
- LangChain
- OpenAI API
- ChromaDB
- PyPDFLoader
- RecursiveCharacterTextSplitter
- OpenAI Embeddings
- GPT-5 Nano
- dotenv

---

# 📂 Repository Structure

```text
RAG/

│
├── 01_Text_RAG.ipynb
├── 02_PDF_RAG.ipynb
├── 03_Persistent_VectorDB.ipynb
├── 04_Add_New_Documents.ipynb
├── 05_Enterprise_RAG.ipynb
│
├── Doc_pdf/
│      fabric-onelake.pdf
│      fabric-admin.pdf
│
├── vectorDB/
│
├── .env
├── requirements.txt
└── README.md
```

---

# 🧠 Learning Roadmap

## Project 1 — Basic RAG using Text

### Goal

Understand the simplest RAG pipeline.

Architecture

```text
Text

↓

Chunk

↓

Embedding

↓

Vector Database

↓

Question

↓

Similarity Search

↓

LLM

↓

Answer
```

Topics Learned

- LangChain Documents
- RecursiveCharacterTextSplitter
- OpenAI Embeddings
- ChromaDB
- Similarity Search

---

## Project 2 — PDF RAG

### Goal

Load PDF documents and build a searchable knowledge base.

Architecture

```text
PDF

↓

PyPDFLoader

↓

Documents

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Question

↓

Answer
```

Topics Learned

- PyPDFLoader
- Document Objects
- Metadata
- PDF Chunking
- Semantic Search

---

## Project 3 — Persistent Vector Database

### Goal

Persist embeddings locally and reuse them.

Architecture

```text
PDF

↓

Chunks

↓

Embeddings

↓

Persist ChromaDB

↓

Reload ChromaDB

↓

Search
```

Topics Learned

- persist_directory
- Loading existing vector databases
- Avoid regenerating embeddings
- Production workflow

---

## Project 4 — Incremental Knowledge Base

### Goal

Add new PDF documents into an existing vector database.

Architecture

```text
Existing ChromaDB

↓

Load Database

↓

New PDF

↓

Chunking

↓

Embeddings

↓

add_documents()

↓

Updated Database

↓

Question

↓

Answer
```

Topics Learned

- add_documents()
- Incremental indexing
- Enterprise document ingestion
- Growing knowledge bases

---

## Project 5 — Enterprise Document Assistant

### Goal

Build an enterprise-style RAG application.

Architecture

```text
                    PDF

                     │

                     ▼

              Document Loader

                     │

                     ▼

             Metadata Enrichment

                     │

                     ▼

          Recursive Chunking

                     │

                     ▼

          OpenAI Embeddings

                     │

                     ▼

              ChromaDB

                     │

                     ▼

           Semantic Retrieval

                     │

                     ▼

           Context Creation

                     │

                     ▼

              GPT Prompt

                     │

                     ▼

              Final Answer
```

Topics Learned

- Enterprise pipeline
- Prompt Engineering
- Source Attribution
- Similarity Search
- Context Building

---

# 📖 RAG Workflow

```text
                 User Question

                       │

                       ▼

             Convert Question

               Into Embedding

                       │

                       ▼

        Search Similar Vectors

           Inside ChromaDB

                       │

                       ▼

         Retrieve Top K Chunks

                       │

                       ▼

      Build Context + Question

                       │

                       ▼

             GPT-5 Nano

                       │

                       ▼

              Final Answer
```

---

# 📌 Key Concepts Learned

## Document Loader

Loads external data sources.

Example:

- PDF
- Word
- HTML
- CSV
- Text

---

## Documents

LangChain stores every page as

```python
Document(
    page_content="...",
    metadata={}
)
```

---

## Chunking

Large documents are split into small pieces.

Example

```text
100 Page PDF

↓

650 Chunks
```

---

## Embeddings

Convert text into numerical vectors.

Example

```text
"What is OneLake?"

↓

[0.34, -0.18, 0.77, ...]
```

---

## Vector Database

Stores

- embeddings
- original text
- metadata

---

## Semantic Search

Instead of keyword matching

```text
OneLake

≠

Storage

```

the embedding captures meaning, enabling semantic retrieval.

---

## Retrieval

Top K similar chunks are retrieved.

Example

```python
vectordb.similarity_search(
    question,
    k=3
)
```

---

## Prompt Augmentation

The retrieved chunks are inserted into the prompt.

```text
Context

+

Question

↓

GPT
```

---

## Generation

GPT generates the final grounded answer.

---

# 💻 Libraries Used

```python
PyPDFLoader

RecursiveCharacterTextSplitter

OpenAIEmbeddings

ChatOpenAI

Chroma

dotenv
```

---

# 📚 Skills Practiced

- LangChain
- RAG
- Vector Databases
- ChromaDB
- Embeddings
- Semantic Search
- Prompt Engineering
- Metadata
- Enterprise RAG
- OpenAI API
- GPT Models

---

# 🚀 Future Improvements

Planned enhancements:

- Multi-PDF RAG
- Metadata Filtering
- Parent Document Retriever
- Context Compression
- Multi-Query Retrieval
- BM25 + Vector Hybrid Search
- Reranking
- FAISS
- Pinecone
- Weaviate
- Milvus
- Azure AI Search
- PostgreSQL pgvector
- LangGraph Agentic RAG
- Conversation Memory
- Streaming Responses
- Source Highlighting
- Citation-based Responses

---

# 🎯 Interview Topics Covered

This repository covers common interview topics including:

- What is RAG?
- Why do we need RAG?
- LLM limitations
- Embeddings
- Chunking strategies
- Chunk overlap
- Metadata
- Vector databases
- ChromaDB
- Similarity search
- Cosine similarity
- Prompt augmentation
- Retrieval pipeline
- Persistent vector databases
- Incremental indexing
- Enterprise RAG architecture

---

# 📌 Author

**Junaid Bilal**

Senior Data Platform & Analytics Engineer

Learning Focus:

- Data Engineering
- Generative AI
- LangChain
- Agentic AI
- RAG Systems
- Azure
- Databricks
- Snowflake