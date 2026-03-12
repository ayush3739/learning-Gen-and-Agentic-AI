> 📌 *Personal learning notes from the <a href="https://www.udemy.com/course/full-stack-ai-with-python/">Full Stack Generative and Agentic AI with Python</a> course.*

# 📘 Section 21: RAG Systems (Retrieval-Augmented Generation)

This section covers **RAG** — a technique that gives LLMs access to your own documents by retrieving relevant context at query time, solving the "LLMs don't know your data" problem.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `index.py` | Document loading, chunking, embedding, and indexing into Qdrant |
| `retrieval_code(chat).py` | Chat interface with semantic retrieval and LLM answer generation |
| `node-js.pdf` | Sample document used for RAG demonstration |
| `docker-compose.yml` | Qdrant vector database setup via Docker |
| `RAG.excalidraw` | End-to-end RAG pipeline architecture diagram |

---

## ✅ What I Learned

### 🔹 The Problem RAG Solves
- LLMs have a knowledge cut-off date and don't know about your private documents
- Fine-tuning is expensive; RAG is a cheaper, more flexible alternative
- RAG retrieves relevant document chunks at query time and includes them in the prompt

### 🔹 RAG Pipeline — Indexing Phase
1. **Load documents** — PDF, text, web pages, etc.
2. **Chunk documents** — split into smaller overlapping segments (e.g., 512 tokens, 50 overlap)
3. **Embed chunks** — convert each chunk to a dense vector using an embedding model
4. **Store vectors** — save chunk text + vector in a vector database (Qdrant)

### 🔹 RAG Pipeline — Retrieval & Generation Phase
1. **Embed the user query** — same embedding model as indexing
2. **Similarity search** — find the top-k most similar chunks in Qdrant
3. **Build the prompt** — inject retrieved chunks as context
4. **Generate answer** — LLM uses the context to answer accurately

### 🔹 Qdrant Vector Database
- Qdrant is an open-source vector similarity search engine
- Run locally via Docker: `docker compose up -d`
- Python client: `qdrant_client.QdrantClient`
- Creating a collection: `client.create_collection(name, vectors_config=VectorParams(size, distance))`
- Upserting vectors: `client.upsert(collection_name, points=[PointStruct(id, vector, payload)])`
- Searching: `client.search(collection_name, query_vector, limit=k)`

### 🔹 Text Chunking Strategies
- **Fixed size** — split every N characters or tokens
- **Sentence-based** — split on sentence boundaries for coherence
- **Recursive character splitting** — LangChain's `RecursiveCharacterTextSplitter`
- **Overlap** — sliding window overlap retains context across chunk boundaries

### 🔹 Embeddings
- Embedding models convert text into high-dimensional vectors (e.g., 1536-dim for `text-embedding-3-small`)
- OpenAI `client.embeddings.create(model="text-embedding-3-small", input=text)`
- Cosine similarity measures how semantically close two vectors are

### 🔹 Chat with Memory over Documents
- Maintaining a conversation history while grounding answers in retrieved context
- Including previous messages + retrieved context in each LLM call
- Preventing hallucinations by explicitly saying "Answer only using the provided context"

---

## 🛠️ Key Code Patterns

```python
import os
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
qdrant = QdrantClient(host="localhost", port=6333)

COLLECTION = "my_docs"
EMBED_MODEL = "text-embedding-3-small"
EMBED_DIM = 1536

# --- Indexing ---
def embed(text: str) -> list[float]:
    resp = client.embeddings.create(model=EMBED_MODEL, input=text)
    return resp.data[0].embedding

def index_chunks(chunks: list[str]):
    qdrant.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE),
    )
    points = [
        PointStruct(id=str(uuid.uuid4()), vector=embed(chunk), payload={"text": chunk})
        for chunk in chunks
    ]
    qdrant.upsert(collection_name=COLLECTION, points=points)

# --- Retrieval ---
def retrieve(query: str, top_k: int = 5) -> list[str]:
    results = qdrant.search(
        collection_name=COLLECTION,
        query_vector=embed(query),
        limit=top_k,
    )
    return [r.payload["text"] for r in results]

# --- Generation ---
def answer(query: str) -> str:
    context = "\n\n".join(retrieve(query))
    messages = [
        {"role": "system", "content": "Answer the question using ONLY the provided context. If the answer isn't in the context, say so."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
    ]
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return resp.choices[0].message.content
```

---

## 🐳 Docker Setup

```bash
# Start Qdrant
cd "section 21 (Rag systems)"
docker compose up -d

# Qdrant dashboard available at http://localhost:6333/dashboard
```

---

## 📌 Prerequisites
- [Section 20: AI Agents](../section%2020%20%28AI%20Agents%29/README.md)
- Docker installed and running

## 📌 Next Section
➡️ [Section 22: Distributed RAG with Queues](../section_22_Rag_queue/README.md)
