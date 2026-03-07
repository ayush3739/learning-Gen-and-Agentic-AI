# 📘 Section 22: Distributed RAG with Message Queues

This section scales the RAG pipeline from a single process to a **distributed, queue-based architecture** using Redis and Python-RQ — so heavy embedding and retrieval work can be handled by background workers.

---

## 📂 Files & Structure

```
section_22_Rag_queue/
├── main.py                # Entry point — enqueues RAG jobs
├── server.py              # API server — accepts user queries
├── docker-compose.yml     # Redis service setup
├── client/
│   └── rq_client.py       # Redis Queue client — submits jobs
└── queues/
    └── worker.py          # RQ worker — processes RAG jobs in the background
```

| File | Topic |
|------|-------|
| `main.py` | Orchestrates the distributed RAG flow |
| `server.py` | HTTP server exposing a `/query` endpoint |
| `client/rq_client.py` | Submits RAG jobs to the Redis queue |
| `queues/worker.py` | Background worker that embeds, retrieves, and generates |
| `docker-compose.yml` | Runs Redis for queue management |

---

## ✅ What I Learned

### 🔹 Why Distributed RAG?
- Single-process RAG is fine for demos, but in production:
  - Embedding large documents is slow and CPU/GPU-intensive
  - Multiple users may query simultaneously
  - A web server should return immediately, not block waiting for LLM responses
- Solution: offload heavy work to background workers via a message queue

### 🔹 Redis as a Message Broker
- Redis is an in-memory data store used here as a job queue backend
- Fast, lightweight, and widely supported
- RQ (Redis Queue) is a Python library that wraps Redis for job scheduling

### 🔹 Python-RQ (RQ)
- `Queue("default", connection=Redis())` — create a named queue
- `queue.enqueue(func, *args)` — submit a job to the queue
- `rq worker` — CLI command to start a worker process that consumes jobs
- `job.result` — retrieve the result once the job is complete
- `job.get_status()` — check if a job is queued, started, finished, or failed
- Job TTL and timeout configuration

### 🔹 Architecture Pattern
```
User → API Server → enqueue job → Redis Queue
                                        ↓
                               RQ Worker processes:
                               1. Embed query
                               2. Search Qdrant
                               3. Call LLM
                               4. Store result → Redis
                                        ↓
User ← API Server ← poll result ← Redis
```

### 🔹 Scalability Benefits
- Workers can run on separate machines or in separate containers
- Multiple workers consume from the same queue in parallel
- The API server stays responsive regardless of how long RAG takes
- Easy to scale horizontally by adding more worker instances

---

## 🛠️ Key Code Patterns

```python
# client/rq_client.py — Submit a RAG job
from redis import Redis
from rq import Queue

redis_conn = Redis(host="localhost", port=6379)
q = Queue("rag_jobs", connection=redis_conn)

def submit_rag_job(query: str):
    from queues.worker import process_rag_query
    job = q.enqueue(process_rag_query, query)
    return job.id

# queues/worker.py — Process the RAG job
def process_rag_query(query: str) -> str:
    # 1. Embed the query
    # 2. Retrieve from Qdrant
    # 3. Call OpenAI LLM
    # 4. Return the answer
    ...

# server.py — Async result polling
from flask import Flask, request, jsonify
from rq.job import Job
from redis import Redis

app = Flask(__name__)
redis_conn = Redis()

@app.route("/query", methods=["POST"])
def query():
    q = request.json["question"]
    job = submit_rag_job(q)
    return jsonify({"job_id": job})

@app.route("/result/<job_id>")
def result(job_id):
    job = Job.fetch(job_id, connection=redis_conn)
    return jsonify({"status": job.get_status(), "result": job.result})
```

---

## 🐳 Docker Setup

```bash
cd section_22_Rag_queue
docker compose up -d        # starts Redis

# Start a worker (in a separate terminal)
rq worker rag_jobs

# Run the server
python server.py
```

---

## 📌 Prerequisites
- [Section 21: RAG Systems](../section%2021%20%28Rag%20systems%29/README.md)
- Docker installed and running

## 📌 Next Section
➡️ [Section 23–24: LangGraph & Multi-Modal AI](../section%2023-24%20%28Langgraph%20%26%20multi%20modal%20ai%29/README.md)
