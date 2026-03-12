> 📌 *Personal learning notes from the <a href="https://www.udemy.com/course/full-stack-ai-with-python/">Full Stack Generative and Agentic AI with Python</a> course.*

# 📘 Section 20: AI Agents

This section covers **AI Agents** — LLM-powered programs that can autonomously use tools, make decisions, and take actions in the world. We build a general-purpose agent and a practical weather agent, plus a web-based TODO app.

---

## 📂 Files in This Section

| File | Topic |
|------|-------|
| `Agent.py` | Core agent with tool/function calling loop |
| `weather_agent.py` | Real-world agent integrated with the OpenWeather API |
| `Ai_Agents.excalidraw` | Agent architecture and decision-loop diagrams |
| `todo_app/index.html` | Frontend for the agent-powered TODO application |
| `todo_app/script.js` | Agent interaction logic from the browser |
| `todo_app/styles.css` | Application styling |

---

## ✅ What I Learned

### 🔹 What is an AI Agent?
- An agent is an LLM that can autonomously **observe**, **reason**, and **act**
- The agent loop: receive input → reason (LLM) → choose action (tool) → execute → observe result → repeat
- Agents go beyond chatbots by interacting with external systems

### 🔹 Tool / Function Calling
- OpenAI's function calling feature lets the LLM request the execution of a specific function
- Tools are defined as JSON schemas describing the function name, description, and parameters
- The LLM decides **when** and **how** to call a tool based on the conversation context
- The application executes the tool and feeds the result back to the LLM

### 🔹 Defining Tools
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                },
                "required": ["city"],
            },
        },
    }
]
```

### 🔹 The Agent Loop
- Send messages + tool definitions to the LLM
- Check if the response contains a `tool_calls` field
- If yes: extract function name and arguments, execute the function, append the result as a `tool` message
- Send the updated messages back to the LLM
- Repeat until the LLM produces a final text response (no more tool calls)

### 🔹 Weather Agent
- Integrates with the [OpenWeather API](https://openweathermap.org/api)
- The agent receives a natural-language query (e.g., "What's the weather like in Tokyo?")
- Automatically decides to call `get_weather("Tokyo")`, gets the data, then generates a human-readable answer

### 🔹 Shell Command Execution
- Agents can be given a `run_shell_command` tool
- Allows the LLM to execute system commands and read their output
- Useful for coding assistants and automation agents

### 🔹 Web-Based Agent Interface (TODO App)
- HTML/CSS/JS frontend that communicates with the agent backend
- Users interact via a chat interface; the agent manages a TODO list
- Demonstrates how to expose agents as web services

---

## 🛠️ Key Code Patterns

```python
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_weather(city: str) -> dict:
    """Call OpenWeather API and return weather data."""
    import requests
    resp = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": city, "appid": os.getenv("OPENWEATHER_API_KEY"), "units": "metric"},
    )
    return resp.json()

TOOLS = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]

TOOL_REGISTRY = {"get_weather": get_weather}

def run_agent(user_message: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant with access to weather data."},
        {"role": "user", "content": user_message},
    ]
    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
        )
        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            return msg.content  # final answer

        for tc in msg.tool_calls:
            func = TOOL_REGISTRY[tc.function.name]
            args = json.loads(tc.function.arguments)
            result = func(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": json.dumps(result),
            })

print(run_agent("What's the weather in Paris?"))
```

---

## 📌 Prerequisites
- [Section 18–19: Hugging Face & Ollama](../section%2018-19%20%28Hugging%20Face%20%26%20ollama%20docker%29/README.md)
- OpenWeather API key (free tier available)

## 📌 Next Section
➡️ [Section 21: RAG Systems](../section%2021%20%28Rag%20systems%29/README.md)
