# 📘 Section 25–26: Memory Layer in AI Agents

This section explores how to give AI agents **persistent, structured memory** so they can remember past conversations, user preferences, and facts across sessions using MongoDB.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `mem.py` | Memory system implementation with MongoDB |
| `memory in Ai agents.excalidraw` | Memory architecture diagrams |
| `docker-compose.yml` | MongoDB and supporting services via Docker |

---

## ✅ What I Learned

### 🔹 Why Agents Need Memory
- LLMs are stateless by default — each API call starts fresh
- Without memory, agents cannot:
  - Remember previous conversations
  - Learn user preferences over time
  - Build on earlier context in long tasks
- Memory turns a chatbot into a true personal assistant

### 🔹 Types of Memory in AI Agents

| Memory Type | Description | Example |
|-------------|-------------|---------|
| **In-context (short-term)** | Recent messages in the current prompt window | Last 10 chat turns |
| **External (long-term)** | Stored outside the LLM, retrieved when needed | Database of past conversations |
| **Semantic memory** | Meaning-based storage using embeddings | "User likes Python content" stored as vector |
| **Episodic memory** | Specific past events and interactions | "User asked about RAG on March 5th" |
| **Procedural memory** | How to do things — usually encoded in the system prompt | Persistent instructions and preferences |

### 🔹 MongoDB for Persistent Memory
- MongoDB is a document database — perfect for storing flexible JSON-like conversation data
- Run via Docker: `docker compose up -d`
- Python client: `pymongo.MongoClient`
- Each conversation thread is stored as a collection of message documents
- MongoDB's flexible schema accommodates changing message formats easily

### 🔹 Memory Patterns Implemented
- **Conversation history** — store every user/assistant message with timestamps and thread IDs
- **Summarisation** — periodically summarise older messages to stay within the context window
- **Entity extraction** — extract named entities (people, places, topics) and store them for future recall
- **Semantic search over memory** — embed stored memories and retrieve relevant ones by similarity

### 🔹 Memory Retrieval Strategy
1. User sends a new message
2. Retrieve relevant past memories (by recency, keyword, or semantic similarity)
3. Include retrieved memories in the system prompt or context
4. LLM generates a response informed by both the current message and recalled memories
5. Store the new interaction as a new memory entry

### 🔹 Managing Context Window Limits
- You cannot include all memories in every prompt — the context window is finite
- Strategies: retrieve only the top-k most relevant memories, summarise old conversations, keep a rolling window of recent messages

---

## 🛠️ Key Code Patterns

```python
import os
from datetime import datetime
from pymongo import MongoClient
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
mongo = MongoClient("mongodb://localhost:27017/")
db = mongo["agent_memory"]
conversations = db["conversations"]

def save_message(thread_id: str, role: str, content: str):
    conversations.insert_one({
        "thread_id": thread_id,
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow(),
    })

def get_history(thread_id: str, limit: int = 20) -> list[dict]:
    docs = conversations.find(
        {"thread_id": thread_id},
        sort=[("timestamp", 1)],
    ).limit(limit)
    return [{"role": d["role"], "content": d["content"]} for d in docs]

def chat(thread_id: str, user_message: str) -> str:
    # Load history from MongoDB
    history = get_history(thread_id)

    # Build messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant with memory of past conversations."},
        *history,
        {"role": "user", "content": user_message},
    ]

    # Call LLM
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    assistant_reply = response.choices[0].message.content

    # Persist new messages
    save_message(thread_id, "user", user_message)
    save_message(thread_id, "assistant", assistant_reply)

    return assistant_reply

# Example usage
reply = chat("user-42", "My favourite programming language is Python.")
reply2 = chat("user-42", "What's my favourite language?")  # Remembers!
print(reply2)
```

---

## 🐳 Docker Setup

```bash
cd "section 25-26 (Memory Latyer in AI Agents)"
docker compose up -d

# MongoDB is available at mongodb://localhost:27017
# MongoDB Compass (GUI) can connect at the same URI
```

---

## 📌 Prerequisites
- [Section 23–24: LangGraph & Multi-Modal AI](../section%2023-24%20%28Langgraph%20%26%20multi%20modal%20ai%29/README.md)
- Docker installed and running

## 📌 Next Section
➡️ [Section 27: Knowledge Graphs & Graph Memory](../section%2027%20%28Graph%20Memory%20and%20Knowledge%20graphs%29/README.md)
