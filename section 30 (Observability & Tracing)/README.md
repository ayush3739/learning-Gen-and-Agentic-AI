# Section 30: Observability and Tracing

Personal learning notes and practice notebooks for observability, tracing, prompt management, evaluation, and monitoring of AI applications.

## Modules

- **Module 0:** RAG application foundation
- **Module 1:** Tracing basics, run types, threads, and tracing methods
- **Module 2:** Datasets, evaluators, and experiments
- **Module 3:** Prompt management and prompt development
- **Module 4:** Human feedback
- **Module 5:** Filtering and online evaluation

## Basic Setup

Run these commands from this folder. The project uses the shared virtual environment in the repository root:

```powershell
cd "C:\Users\Ayush Maurya\Desktop\hexon\learn_ai"
.\venv\Scripts\Activate.ps1
cd ".\section 30 (Observability & Tracing)"
uv sync --active
```

Create a `.env` file in this folder with your own keys:

```env
GROQ_API_KEY=your_groq_key
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=langsmith-academy
```

The notebooks use Groq through its OpenAI-compatible API with the `openai/gpt-oss-20b` model. RAG embeddings use the local Ollama model `nomic-embed-text`.

Make sure Ollama is running and the model is available:

```powershell
ollama list
```

Open the notebooks in VS Code and select the Python interpreter from the shared `venv` environment.

## License

The original MIT license and copyright notice are preserved in [LICENSE](LICENSE). Changes in this folder are personal learning modifications.
