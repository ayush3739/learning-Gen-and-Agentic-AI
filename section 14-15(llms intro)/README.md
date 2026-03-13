> 📌 *Personal learning notes from the <a href="https://www.udemy.com/course/full-stack-ai-with-python/">Full Stack Generative and Agentic AI with Python</a> course.*

# 📘 Section 14–15: LLM Basics

This section introduces **Large Language Models (LLMs)** and how to call them programmatically via APIs. We use OpenAI, Google Gemini, and GitHub Models as providers.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `basic.ipynb` | Foundational LLM concepts and first API calls |
| `open_ai.py` | OpenAI GPT-4o and gpt-4o-mini integration |
| `gemini.py` | Google Gemini API client |
| `gemini_using_openai.py` | Accessing Gemini through an OpenAI-compatible endpoint |
| `llm_basics.excalidraw` | LLM architecture and data-flow diagrams |

---

## ✅ What I Learned

### 🔹 What is an LLM?
- Large language models are transformer-based neural networks trained on massive text corpora
- They predict the next token given a context (prompt)
- Capabilities: text generation, summarisation, translation, code generation, reasoning
- Key parameters: **temperature** (creativity), **max tokens** (output length), **top-p** (nucleus sampling)

### 🔹 OpenAI API
- Authenticating with `OPENAI_API_KEY` via environment variables
- Using the `openai` Python SDK: `from openai import OpenAI`
- Creating chat completions with `client.chat.completions.create()`
- Understanding the **messages array**: `system`, `user`, `assistant` roles
- Selecting models: `gpt-4o`, `gpt-4o-mini`
- Extracting the response text: `response.choices[0].message.content`
- Tracking token usage: `response.usage.prompt_tokens`, `completion_tokens`, `total_tokens`
- Cost estimation based on token counts

### 🔹 Google Gemini API
- Authenticating with `Gemini_api_key` via environment variables
- Using the `google-generativeai` Python SDK
- `genai.GenerativeModel("gemini-1.5-flash")` and `model.generate_content()`
- Differences between Gemini's API style and OpenAI's

### 🔹 Gemini via OpenAI-Compatible Endpoint
- Google exposes a Gemini endpoint compatible with the OpenAI client
- Reusing existing OpenAI SDK code by changing `base_url` and `model` name
- Simplifies multi-provider code by keeping a single client interface

### 🔹 GitHub Models API
- Free access to GPT-4o and other models via GitHub Models marketplace
- Uses a `GITHUB_TOKEN` for authentication
- OpenAI-compatible endpoint: `https://models.inference.ai.azure.com`
- Useful for testing without a paid OpenAI subscription

### 🔹 Streaming Responses
- Using `stream=True` to receive tokens as they are generated
- Processing `chunk.choices[0].delta.content` in a for-loop
- Better user experience for long outputs

### 🔹 Key LLM Concepts
| Concept | Description |
|---------|-------------|
| **Token** | The smallest unit of text the model processes (~¾ of a word) |
| **Context window** | Maximum tokens the model can see at once |
| **Temperature** | 0 = deterministic, 1+ = more creative/random |
| **Top-p** | Cumulative probability threshold for token selection |
| **System prompt** | Instructions that shape the model's behaviour |
| **Few-shot** | Providing examples inside the prompt |

---

## 🛠️ Key Code Patterns

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Basic chat completion
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    temperature=0.7,
    max_tokens=256,
)
print(response.choices[0].message.content)
print(f"Tokens used: {response.usage.total_tokens}")

# Streaming
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a story."}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

# Google Gemini
import google.generativeai as genai
genai.configure(api_key=os.getenv("Gemini_api_key"))
model = genai.GenerativeModel("gemini-1.5-flash")
resp = model.generate_content("Explain photosynthesis in one paragraph.")
print(resp.text)
```

---

## 📌 Prerequisites
- [Section 13: Pydantic](../section%2013%20%28Pydantic%29/README.md)

## 📌 Next Section
➡️ [Section 16–17: Prompting Techniques](../section%2016-17%20%28Prompting%20Techniques%29/README.md)
