> 📌 *Personal learning notes from the <a href="https://www.udemy.com/course/full-stack-ai-with-python/">Full Stack Generative and Agentic AI with Python</a> course.*

# 📘 Section 13: Pydantic

This section covers **Pydantic** — the most popular Python library for data validation and settings management. It underpins many AI frameworks (LangChain, FastAPI, OpenAI SDK) so understanding it is essential before moving into LLMs.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `pydantic_basics_and_Serialization.ipynb` | Core Pydantic models, validation, serialisation/deserialisation |
| `pydantic.excalidraw` | Data validation architecture diagram |

---

## ✅ What I Learned

### 🔹 Pydantic `BaseModel`
- Defining data models by subclassing `pydantic.BaseModel`
- Type annotations drive automatic validation
- Creating instances and accessing fields like regular Python attributes
- Immutable models with `model_config = ConfigDict(frozen=True)`

### 🔹 Field Types & Constraints
- Standard Python types: `str`, `int`, `float`, `bool`, `list`, `dict`
- Optional fields with `Optional[T]` or `T | None`
- Default values with `Field(default=...)` and `Field(default_factory=...)`
- Constrained types: `Field(gt=0)`, `Field(max_length=100)`, `Field(pattern=r"^\d+$")`
- `EmailStr`, `HttpUrl`, `AnyUrl` and other specialised validators

### 🔹 Validators
- `@field_validator` for custom per-field validation logic
- `@model_validator` for cross-field validation
- `mode="before"` vs. `mode="after"` validation phases
- Raising `ValueError` to trigger validation errors

### 🔹 Serialisation & Deserialisation
- `.model_dump()` — convert model to a Python dict
- `.model_dump_json()` — convert model to a JSON string
- `Model.model_validate(dict)` — build a model from a dict
- `Model.model_validate_json(json_string)` — parse JSON directly
- Aliasing fields with `Field(alias="field_name")` for external APIs
- `model_config = ConfigDict(populate_by_name=True)`

### 🔹 Nested Models
- Composing models inside other models
- Automatic recursive validation of nested structures
- Lists and dicts of models

### 🔹 Pydantic Settings
- `pydantic_settings.BaseSettings` for environment-variable-driven configuration
- Reading `.env` files automatically
- Type coercion from string environment variables

---

## 🛠️ Key Code Patterns

```python
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str = Field(pattern=r"^\d{5}$")

class User(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(default=None, ge=0, le=120)
    address: Address

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be blank")
        return v.title()

# Create from dict
user = User.model_validate({
    "id": 1,
    "name": "alice",
    "email": "alice@example.com",
    "address": {"street": "123 Main St", "city": "Springfield", "postal_code": "12345"},
})

# Serialise
print(user.model_dump())
print(user.model_dump_json(indent=2))

# Parse JSON
user2 = User.model_validate_json('{"id":2,"name":"Bob",...}')
```

---

## 📌 Why Pydantic Matters for AI
- OpenAI SDK uses Pydantic for structured output parsing
- LangChain / LangGraph use Pydantic for agent state and tool schemas
- FastAPI (common API layer for AI apps) is built on Pydantic
- Pydantic ensures your LLM's JSON responses are correctly typed

---

## 📌 Prerequisites
- [Section 12: Asyncio](../section%2012%20%28Asyncio%29/README.md)

## 📌 Next Section
➡️ [Section 14–15: LLM Basics](../section%2014-15%28llms%20intro%29/README.md)
