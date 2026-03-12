> **📌 Disclaimer:** This repository contains my personal notes and practice code written while following the **[Full Stack Generative and Agentic AI with Python](https://www.udemy.com/course/full-stack-ai-with-python/)** course by **Hitesh Choudhary** and **Piyush Garg** on Udemy. All code is independently written for learning purposes only. No course material, videos, or slides are reproduced here.
> 
# 🤖 Learning Generative & Agentic AI

A structured, hands-on course repository that progresses from **Python fundamentals** all the way to **production-ready AI systems** — covering LLMs, RAG pipelines, AI Agents, voice agents, knowledge graphs, and more.

---

## 📚 What You Will Learn

| Section | Topic | Key Concepts |
|---------|-------|-------------|
| [1 – 6](section%201-6/README.md) | **Python Fundamentals** | Lambda functions, `enumerate`, `zip`, `*args/**kwargs`, dictionaries, walrus operator, collections, dunder/magic methods |
| [7 – 10](section%207-10/README.md) | **Advanced Python & OOP** | Generators, decorators, object-oriented programming, list/dict/set comprehensions, exception handling |
| [11](section%2011%20%28Mutltiprocessing%2CMultiThreading%2CGil%29/README.md) | **Concurrency & Parallelism** | Multiprocessing, multithreading, Global Interpreter Lock (GIL), inter-process communication, shared values |
| [12](section%2012%20%28Asyncio%29/README.md) | **Asyncio & Async Programming** | `async`/`await`, event loops, `aiohttp`, race conditions, deadlocks, background workers, daemon threads |
| [13](section%2013%20%28Pydantic%29/README.md) | **Pydantic** | Data validation, type-safe models, JSON serialization/deserialization |
| [14 – 15](section%2014-15%28llms%20intro%29/README.md) | **LLM Basics** | OpenAI API, Google Gemini API, GitHub Models API, LLM fundamentals |
| [16 – 17](section%2016-17%20%28Prompting%20Techniques%29/README.md) | **Prompt Engineering** | Few-shot prompting, chain-of-thought, role-based prompts, prompt serialization |
| [18 – 19](section%2018-19%20%28Hugging%20Face%20%26%20ollama%20docker%29/README.md) | **Local LLMs** | Hugging Face Transformers, Ollama (Docker), running models offline |
| [20](section%2020%20%28AI%20Agents%29/README.md) | **AI Agents** | Tool calling, function calling, autonomous decision-making, shell command execution |
| [21](section%2021%20%28Rag%20systems%29/README.md) | **RAG Systems** | Document loading & chunking, vector embeddings, Qdrant vector DB, semantic search, retrieval-augmented generation |
| [22](section_22_Rag_queue/README.md) | **Distributed RAG with Queues** | Redis message queues, RQ workers, scalable RAG architecture |
| [23 – 24](section%2023-24%20%28Langgraph%20%26%20multi%20modal%20ai%29/README.md) | **LangGraph & Multi-Modal AI** | Graph-based agent orchestration, memory checkpointing, image/vision model processing |
| [25 – 26](section%2025-26%20%28Memory%20Latyer%20in%20AI%20Agents%29/README.md) | **Memory Layers in AI Agents** | Persistent conversation history, MongoDB for document storage, semantic memory |
| [27](section%2027%20%28Graph%20Memory%20and%20Knowledge%20graphs%29/README.md) | **Knowledge Graphs** | Neo4j graph database, entity-relationship modelling, graph-based reasoning |
| [28](section%2028%20%28Voice%20agents%20%26%20MCP%20%29/README.md) | **Voice Agents & MCP** | Speech-to-text, text-to-speech (ElevenLabs, Azure, gTTS), Model Context Protocol (MCP) |

---

## 🛠️ Technologies & Tools Used

### Languages & Frameworks
- **Python 3.10+** — primary language throughout
- **Jupyter Notebooks** — interactive tutorials and experiments
- **HTML / CSS / JavaScript** — frontend for TODO and voice apps

### LLM Providers & APIs
- [OpenAI](https://platform.openai.com/) (GPT-4o, gpt-4o-mini)
- [Google Gemini](https://ai.google.dev/) (Gemini 1.5 / 2.0)
- [GitHub Models](https://github.com/marketplace/models) (OpenAI-compatible endpoint)
- [Hugging Face](https://huggingface.co/) (open-source transformers)

### AI / Agent Frameworks
- [LangGraph](https://langchain-ai.github.io/langgraph/) — stateful agent workflows
- [Pydantic](https://docs.pydantic.dev/) — data validation and structured outputs
- [aiohttp](https://docs.aiohttp.org/) — async HTTP client

### Databases & Infrastructure
| Tool | Purpose |
|------|---------|
| [Qdrant](https://qdrant.tech/) | Vector database for semantic search |
| [MongoDB](https://www.mongodb.com/) | Document storage for conversation memory |
| [Neo4j](https://neo4j.com/) | Graph database for knowledge graphs |
| [Redis + RQ](https://python-rq.org/) | Message queue for distributed workers |
| [Docker Compose](https://docs.docker.com/compose/) | Orchestrating all database services |

### Voice & Speech
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — speech-to-text
- [gTTS](https://pypi.org/project/gTTS/) / [pyttsx3](https://pypi.org/project/pyttsx3/) — text-to-speech
- [ElevenLabs](https://elevenlabs.io/) / Azure TTS — premium TTS options

---

## 🗂️ Repository Structure

```
learning-Gen-and-Agentic-AI/
├── section 1-6/              # Python fundamentals
├── section 7-10/             # Advanced Python & OOP
├── section 11/               # Multiprocessing, Multithreading, GIL
├── section 12 (Asyncio)/     # Async programming
├── section 13 (Pydantic)/    # Data validation
├── section 14-15(llms intro)/# LLM APIs & basics
├── section 16-17 (Prompting)/# Prompt engineering
├── section 18-19 (HF & Ollama)/# Local open-source LLMs
├── section 20 (AI Agents)/   # Agent implementation
├── section 21 (Rag systems)/ # RAG pipeline
├── section_22_Rag_queue/     # Distributed RAG + queues
├── section 23-24 (Langgraph)/# LangGraph & multi-modal AI
├── section 25-26 (Memory)/   # Memory layers in agents
├── section 27 (Knowledge graphs)/# Graph memory & Neo4j
├── section 28 (Voice & MCP)/ # Voice agents & MCP
└── requirements.txt          # All Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ayush3739/learning-Gen-and-Agentic-AI.git
cd learning-Gen-and-Agentic-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root (or in the relevant section folder):

```env
OPENAI_API_KEY=your_openai_key
GITHUB_TOKEN=your_github_models_token
Gemini_api_key=your_gemini_key
OPENWEATHER_API_KEY=your_weather_key
NEO_PASSWORD=your_neo4j_password
```

> **Note:** `.env` files are listed in `.gitignore` and are **never** committed to the repository.

### 4. Start infrastructure services (where required)

Several sections use Docker Compose for databases:

```bash
# RAG systems (section 21) — starts Qdrant
cd "section 21 (Rag systems)" && docker compose up -d

# Distributed RAG (section 22) — starts Redis
cd section_22_Rag_queue && docker compose up -d

# LangGraph (section 23-24) — starts supporting services
cd "section 23-24 (Langgraph & multi modal ai)" && docker compose up -d

# Memory agents (section 25-26) — starts MongoDB + Neo4j
cd "section 25-26 (Memory Latyer in AI Agents)" && docker compose up -d
```

---

## 🔐 Security Review

A security scan was conducted on all files in this repository:

- ✅ **No hardcoded API keys or passwords found.**
- ✅ All credentials are loaded from environment variables via `os.getenv(...)`.
- ✅ `.env` files (where real keys are stored) are included in `.gitignore` and are never committed.
- ✅ Only one clearly labelled placeholder found: `"YOUR_ELEVENLABS_API_KEY"` in `section 28/tts_alternatives.py` — this is intentional and not a real credential.

**Best practice followed throughout:** use `.env` files locally, load with `os.getenv()`, and always add `.env` to `.gitignore`.

---

## 📈 Learning Path

```
Python Core  ──►  Advanced Python  ──►  Concurrency / Async
     │
     ▼
Pydantic / Data Validation
     │
     ▼
LLM APIs  ──►  Prompt Engineering  ──►  Local LLMs
     │
     ▼
AI Agents  ──►  RAG Systems  ──►  Distributed RAG
     │
     ▼
LangGraph  ──►  Multi-Modal  ──►  Memory Layers
     │
     ▼
Knowledge Graphs  ──►  Voice Agents & MCP
```

Each section builds on the previous one, making this repository suitable for developers progressing from **basic Python to full-stack agentic AI systems**.

---

## 📝 Notes

- Each section folder contains `.excalidraw` architecture diagrams that can be opened in [Excalidraw](https://excalidraw.com/) for visual reference.
- Jupyter Notebooks (`.ipynb`) can be run with `jupyter notebook` or in VS Code with the Jupyter extension.
- Some sections require a running Docker daemon for database services.
