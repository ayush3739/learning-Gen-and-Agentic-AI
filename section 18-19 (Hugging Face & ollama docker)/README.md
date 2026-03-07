# 📘 Section 18–19: Hugging Face & Ollama (Docker)

This section introduces **open-source LLMs** — models you can run locally on your own hardware, without sending data to a third-party API. We use Hugging Face Transformers and Ollama (via Docker).

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `HF_basic.py` | Loading and running a Hugging Face model with the `pipeline` API |

---

## ✅ What I Learned

### 🔹 Hugging Face Transformers
- The `transformers` library gives a unified Python API over thousands of models
- `pipeline()` is the easiest entry point — one line to load and run a model
- Common tasks supported: `"text-generation"`, `"text-classification"`, `"summarization"`, `"translation"`, `"question-answering"`, `"fill-mask"`
- Models are downloaded automatically from the [Hugging Face Hub](https://huggingface.co/models) on first use and cached locally
- GPU acceleration by setting `device=0` (CUDA) or `device="mps"` (Apple Silicon)

### 🔹 Hugging Face Pipeline API
- `pipe = pipeline("text-generation", model="gpt2")` — load a model
- `pipe("Once upon a time", max_new_tokens=50)` — run inference
- The `tokenizer` and `model` can be loaded separately for more control
- `AutoTokenizer` and `AutoModelForCausalLM` for flexible model loading

### 🔹 Running Models Offline
- After the first download, models work entirely offline
- Useful for privacy-sensitive applications
- Models are cached in `~/.cache/huggingface/hub/`
- `TRANSFORMERS_OFFLINE=1` environment variable forces offline mode

### 🔹 Ollama (Docker-based local LLMs)
- Ollama is a tool for downloading and serving open-source LLMs locally
- Run via Docker: `docker run -d -p 11434:11434 ollama/ollama`
- Pull a model: `docker exec <container> ollama pull llama3`
- Exposes an OpenAI-compatible REST API at `http://localhost:11434`
- Supported models: Llama 3, Mistral, Gemma, Phi-3, CodeLlama, and many more
- Use the OpenAI Python SDK with `base_url="http://localhost:11434/v1"` and `api_key="ollama"`

### 🔹 Comparing Approaches

| Approach | Cost | Privacy | Latency | Control |
|----------|------|---------|---------|---------|
| OpenAI API | Pay per token | Data sent to OpenAI | Low (network) | Low |
| Gemini API | Pay per token | Data sent to Google | Low (network) | Low |
| Hugging Face (local) | Free | Fully local | Depends on hardware | High |
| Ollama (Docker) | Free | Fully local | Depends on hardware | High |

---

## 🛠️ Key Code Patterns

```python
from transformers import pipeline

# Text generation with GPT-2
generator = pipeline("text-generation", model="gpt2")
result = generator("The future of AI is", max_new_tokens=100, num_return_sequences=1)
print(result[0]["generated_text"])

# Sentiment analysis
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
print(classifier("I absolutely love this!"))
# [{'label': 'POSITIVE', 'score': 0.9998}]

# Summarisation
summariser = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summariser(long_text, max_length=130, min_length=30, do_sample=False)

# Ollama via OpenAI SDK
from openai import OpenAI

ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required by SDK, value doesn't matter for Ollama
)

response = ollama_client.chat.completions.create(
    model="llama3",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
)
print(response.choices[0].message.content)
```

---

## 🐳 Docker Setup for Ollama

```bash
# Pull and start Ollama container
docker run -d --name ollama -p 11434:11434 ollama/ollama

# Download a model (e.g., Llama 3 8B)
docker exec ollama ollama pull llama3

# Test via curl
curl http://localhost:11434/api/generate \
  -d '{"model": "llama3", "prompt": "Hello!", "stream": false}'
```

---

## 📌 Prerequisites
- [Section 16–17: Prompting Techniques](../section%2016-17%20%28Prompting%20Techniques%29/README.md)
- Docker installed and running (for Ollama)

## 📌 Next Section
➡️ [Section 20: AI Agents](../section%2020%20%28AI%20Agents%29/README.md)
