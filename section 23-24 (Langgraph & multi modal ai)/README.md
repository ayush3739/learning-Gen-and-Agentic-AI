# 📘 Section 23–24: LangGraph & Multi-Modal AI

This section introduces **LangGraph** — a framework for building stateful, graph-based agent workflows — and **multi-modal AI**, where agents process both text and images.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `chat.py` | Basic LangGraph chat agent with state management |
| `chat_2.py` | Extended LangGraph patterns and routing |
| `chat_checkpoint.py` | Persistent conversation memory via checkpointing |
| `multi_modal_agent.ipynb` | Vision/image processing with multi-modal LLMs |
| `langgraph.excalidraw` | LangGraph node/edge workflow diagrams |
| `docker-compose.yml` | Supporting services for persistence |

---

## ✅ What I Learned

### 🔹 What is LangGraph?
- LangGraph is an extension of LangChain for building **stateful, cyclic agent graphs**
- Unlike linear chains, graphs can loop — essential for multi-step reasoning agents
- The graph has **nodes** (processing steps) and **edges** (transitions between steps)
- A **state** object is passed through the graph and updated at each node

### 🔹 LangGraph Core Concepts
- **StateGraph** — the main graph builder
- **State** — a typed dict (often a Pydantic model or `TypedDict`) shared across all nodes
- **Node** — a Python function that takes the state and returns updated state fields
- **Edge** — a directed connection from one node to another
- **Conditional edge** — routes to different nodes based on the current state (enables branching and looping)
- **`END`** — special node that terminates the graph

### 🔹 Building a Chat Agent with LangGraph
- Define state: `{"messages": list[BaseMessage]}`
- Create a node that calls the LLM: takes messages, returns updated messages
- Add a tool-calling node that executes tools when the LLM requests them
- Use a conditional edge: if the LLM made tool calls → go to tool node → loop back; otherwise → END

### 🔹 Memory & Checkpointing
- LangGraph's **checkpointer** saves the graph state after every step
- Allows conversations to be paused, resumed, and inspected
- `MemorySaver` — in-memory checkpointing for development
- `SqliteSaver` — SQLite-backed persistence for simple production use
- `thread_id` — a unique key that identifies a conversation session
- Enables multi-turn conversations that remember previous exchanges

### 🔹 Multi-Modal AI
- Modern LLMs (GPT-4o, Gemini 1.5) can process both text and images
- Images are passed in the messages array as base64-encoded data or URLs
- Use cases: image captioning, visual QA, document understanding, chart analysis
- The model returns a text description or answer grounded in the image

### 🔹 Multi-Modal Message Format
```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is in this image?"},
            {
                "type": "image_url",
                "image_url": {"url": "https://example.com/image.jpg"},
                # or: "url": f"data:image/jpeg;base64,{base64_image}"
            },
        ],
    }
]
```

---

## 🛠️ Key Code Patterns

```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI

# --- Define state ---
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# --- LLM node ---
llm = ChatOpenAI(model="gpt-4o-mini")

def call_llm(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# --- Build graph ---
graph_builder = StateGraph(AgentState)
graph_builder.add_node("llm", call_llm)
graph_builder.set_entry_point("llm")
graph_builder.add_edge("llm", END)
graph = graph_builder.compile()

# --- Run ---
result = graph.invoke({"messages": [("user", "Hello!")]})
print(result["messages"][-1].content)

# --- With checkpointing ---
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
graph_with_memory = graph_builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "user-123"}}
result = graph_with_memory.invoke({"messages": [("user", "My name is Alice")]}, config=config)
# Later, in a new call, it remembers "Alice"
result2 = graph_with_memory.invoke({"messages": [("user", "What's my name?")]}, config=config)
```

---

## 🐳 Docker Setup

```bash
cd "section 23-24 (Langgraph & multi modal ai)"
docker compose up -d
```

---

## 📌 Prerequisites
- [Section 22: Distributed RAG](../section_22_Rag_queue/README.md)

## 📌 Next Section
➡️ [Section 25–26: Memory Layers in AI Agents](../section%2025-26%20%28Memory%20Latyer%20in%20AI%20Agents%29/README.md)
