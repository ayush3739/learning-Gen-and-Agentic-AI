# 📘 Section 16–17: Prompting Techniques

This section focuses on **prompt engineering** — crafting, structuring, and serialising prompts to reliably elicit high-quality, predictable outputs from LLMs.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `Prompting.ipynb` | Comprehensive prompting strategies with live examples |
| `prompt_serialization_instruction.ipynb` | Structured prompt templates and serialisation |
| `via_github_models.py` | Prompting via the GitHub Models API |

---

## ✅ What I Learned

### 🔹 Zero-Shot Prompting
- Asking the model to perform a task with no examples provided
- Works well when the task is simple and well-defined
- The instruction must be clear and unambiguous

### 🔹 Few-Shot Prompting
- Providing 2–5 examples of input→output pairs inside the prompt
- Helps the model understand the desired format and style
- Particularly useful for structured extraction and classification tasks

```
Q: What is the capital of France? A: Paris
Q: What is the capital of Germany? A: Berlin
Q: What is the capital of Japan? A:
```

### 🔹 Chain-of-Thought (CoT) Prompting
- Instructing the model to "think step by step" before giving the final answer
- Dramatically improves accuracy on reasoning, maths, and multi-step tasks
- Can be zero-shot (`"Let's think step by step."`) or few-shot (showing reasoning examples)

### 🔹 Role-Based / System Prompts
- The `system` message shapes the model's persona and constraints
- "You are a senior Python engineer. Answer only in code." changes output style significantly
- Keeping system prompts concise and explicit produces better results

### 🔹 Instruction Templates
- Separating the template (structure) from the data (user input)
- Using `{placeholder}` style substitution for reusable prompt templates
- Benefits: version control, testing, and consistent model behaviour

### 🔹 Prompt Serialisation
- Storing prompt templates in Python dictionaries or YAML/JSON files
- Loading and rendering prompts programmatically at runtime
- Using Pydantic models to validate prompt data before formatting

### 🔹 Output Formatting Instructions
- Asking the model to respond in JSON, Markdown, or specific schemas
- Including schema examples in the prompt to guide format compliance
- Combining with Pydantic validation to parse and validate model output

### 🔹 GitHub Models API
- Using `GITHUB_TOKEN` with the OpenAI-compatible `https://models.inference.ai.azure.com` endpoint
- Testing prompt variations with models available through GitHub's marketplace
- Iterating on prompts quickly without incurring API costs

---

## 🛠️ Key Code Patterns

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),
)

# --- Zero-shot ---
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarise the following article in 3 bullet points:\n\n{article}"},
    ],
)

# --- Few-shot ---
few_shot_messages = [
    {"role": "system", "content": "Classify sentiment as POSITIVE, NEGATIVE, or NEUTRAL."},
    {"role": "user", "content": "I love this product!"},
    {"role": "assistant", "content": "POSITIVE"},
    {"role": "user", "content": "The delivery was late and the item was broken."},
    {"role": "assistant", "content": "NEGATIVE"},
    {"role": "user", "content": "The package arrived today."},
]

# --- Chain-of-thought ---
cot_prompt = """
Solve the following problem step by step, then give your final answer on a new line starting with 'Answer:'.

Problem: If a train travels 120 km in 2 hours, how long does it take to travel 300 km at the same speed?
"""

# --- Prompt template ---
TEMPLATE = """
You are a {role}.
Task: {task}
Input: {input}
Output format: {output_format}
"""

def build_prompt(role, task, input_data, output_format):
    return TEMPLATE.format(
        role=role,
        task=task,
        input=input_data,
        output_format=output_format,
    )
```

---

## 📌 Prerequisites
- [Section 14–15: LLM Basics](../section%2014-15%28llms%20intro%29/README.md)

## 📌 Next Section
➡️ [Section 18–19: Hugging Face & Ollama Docker](../section%2018-19%20%28Hugging%20Face%20%26%20ollama%20docker%29/README.md)
