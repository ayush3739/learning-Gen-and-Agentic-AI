# 📘 Section 28: Voice Agents & Model Context Protocol (MCP)

This section adds **voice** (speech-to-text and text-to-speech) to AI agents and introduces the **Model Context Protocol (MCP)** — a standardised way to expose tools and data to AI models.

---

## 📂 Files in This Section

```
section 28 (Voice agents & MCP)/
├── voice_agent.py          # Main voice agent — listen, think, speak
├── cursor.py               # MCP integration with Cursor IDE
├── tts_alternatives.py     # Comparison of TTS engines
├── MCP.excalidraw          # Model Context Protocol diagrams
├── voice_agents.excalidraw # Voice agent architecture diagrams
└── todo_app/               # Voice-enabled TODO application
    ├── index.html
    ├── script.js
    └── style.css
```

| File | Topic |
|------|-------|
| `voice_agent.py` | End-to-end voice agent: STT → LLM → TTS |
| `cursor.py` | Exposing tools to AI via MCP for Cursor IDE |
| `tts_alternatives.py` | gTTS, pyttsx3, ElevenLabs, Azure TTS comparison |
| `todo_app/` | Voice-controlled TODO web application |

---

## ✅ What I Learned

### 🔹 Speech-to-Text (STT)
- `SpeechRecognition` library — wraps multiple STT backends
- `speech_recognition.Recognizer` — the main class
- `recognizer.listen(source)` — capture audio from the microphone
- `recognizer.recognize_google(audio)` — transcribe using Google's free API
- `recognizer.recognize_whisper(audio)` — local transcription with OpenAI Whisper
- OpenAI Whisper API: `client.audio.transcriptions.create(model="whisper-1", file=audio_file)`
- Handling noise with `recognizer.adjust_for_ambient_noise(source)`

### 🔹 Text-to-Speech (TTS) — Multiple Approaches

| Library | Type | Quality | Offline | Cost |
|---------|------|---------|---------|------|
| `pyttsx3` | Local TTS engine | Basic | ✅ Yes | Free |
| `gTTS` | Google TTS | Good | ❌ No | Free |
| ElevenLabs | Neural TTS | Excellent | ❌ No | Paid |
| Azure TTS | Neural TTS | Excellent | ❌ No | Paid |
| OpenAI TTS | Neural TTS | Very good | ❌ No | Paid |

```python
# pyttsx3 (offline)
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, world!")
engine.runAndWait()

# gTTS (Google)
from gtts import gTTS
import os
tts = gTTS("Hello, world!", lang="en")
tts.save("output.mp3")
os.system("mpg321 output.mp3")

# ElevenLabs (premium)
from elevenlabs import generate, play
audio = generate(text="Hello, world!", voice="Rachel", api_key="YOUR_ELEVENLABS_API_KEY")
play(audio)

# OpenAI TTS
response = client.audio.speech.create(model="tts-1", voice="alloy", input="Hello, world!")
response.stream_to_file("output.mp3")
```

### 🔹 Building a Voice Agent
- The voice agent loop:
  1. **Listen** — capture microphone input and transcribe with STT
  2. **Think** — send transcript to LLM (with optional tool calling)
  3. **Speak** — convert LLM response to audio with TTS
- Wake-word detection for hands-free activation
- Streaming TTS for lower perceived latency

### 🔹 Model Context Protocol (MCP)
- MCP is an open protocol (by Anthropic) that standardises how AI models access tools and data sources
- Think of it as "USB for AI tools" — one standard interface, many compatible providers
- **MCP Server** — exposes tools, resources, and prompts over a standard protocol
- **MCP Client** — an AI application (Claude, Cursor, etc.) that consumes MCP servers
- Transport options: `stdio` (subprocess), `SSE` (HTTP server-sent events)
- MCP servers can expose: **Tools** (callable functions), **Resources** (readable data), **Prompts** (reusable prompt templates)

### 🔹 MCP with Cursor IDE
- Cursor IDE supports MCP servers for custom tool integration
- Register an MCP server in Cursor's settings: `{"mcpServers": {"my-server": {"command": "python", "args": ["cursor.py"]}}}`
- The AI in Cursor can then call your custom tools directly during coding sessions
- Use-cases: custom code search, internal API access, company knowledge base

### 🔹 Voice-Enabled TODO App
- HTML/CSS/JS frontend with Web Speech API for browser-based STT
- User speaks commands: "Add task: buy groceries", "Mark task 1 as done", "List all tasks"
- Agent parses the command with the LLM and calls the appropriate TODO tool
- Agent confirms the action via TTS

---

## 🛠️ Voice Agent Pattern

```python
import os
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen() -> str:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
    return recognizer.recognize_google(audio)

def think(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant. Keep responses short and conversational."},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content

def speak(text: str):
    tts_engine.say(text)
    tts_engine.runAndWait()

def voice_agent_loop():
    speak("Voice agent ready. How can I help?")
    while True:
        try:
            user_input = listen()
            print(f"You: {user_input}")
            if "exit" in user_input.lower():
                speak("Goodbye!")
                break
            reply = think(user_input)
            print(f"Agent: {reply}")
            speak(reply)
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")

voice_agent_loop()
```

---

## 🔗 MCP Resources
- [MCP Official Docs](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Cursor MCP Guide](https://docs.cursor.com/context/model-context-protocol)

---

## 📌 Prerequisites
- [Section 27: Knowledge Graphs](../section%2027%20%28Graph%20Memory%20and%20Knowledge%20graphs%29/README.md)
- Microphone and speakers/headphones for voice features
- API keys for chosen TTS provider (ElevenLabs / Azure / OpenAI TTS)

## 📌 This is the final section 🎉
You have progressed from Python fundamentals all the way to voice-enabled, tool-using AI agents with persistent memory and graph-based knowledge. Congratulations!
