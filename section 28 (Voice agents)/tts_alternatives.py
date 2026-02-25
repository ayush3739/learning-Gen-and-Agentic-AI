# FREE TTS ALTERNATIVES

# Option 1: gTTS (Google Text-to-Speech) - Free, requires internet
"""
Install: pip install gTTS
"""
from gtts import gTTS
import os

def tts_gtts(text: str):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Windows
    # os.system("afplay output.mp3")  # Mac
    # os.system("mpg123 output.mp3")  # Linux


# Option 2: edge-tts (Microsoft Edge TTS) - Free, high quality
"""
Install: pip install edge-tts
"""
import edge_tts
import asyncio

async def tts_edge(text: str):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")  # Female voice
    # Other voices: en-US-GuyNeural (male), en-GB-SoniaNeural (British female)
    await communicate.save("output.mp3")
    os.system("start output.mp3")  # Windows

# Usage:
# asyncio.run(tts_edge("Hello, this is a test"))


# Option 3: ElevenLabs (Free tier: 10k chars/month) - Very high quality
"""
Install: pip install elevenlabs
Get API key from: https://elevenlabs.io (free tier available)
"""
from elevenlabs import play
from elevenlabs.client import ElevenLabs

def tts_elevenlabs(text: str):
    client = ElevenLabs(api_key="YOUR_ELEVENLABS_API_KEY")
    audio = client.generate(
        text=text,
        voice="Rachel",  # or "Josh", "Bella", etc.
        model="eleven_monolingual_v1"
    )
    play(audio)


# Option 4: Coqui TTS (Local AI model) - Free, offline, AI-powered
"""
Install: pip install TTS
"""
from TTS.api import TTS

def tts_coqui(text: str):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path="output.wav")
    os.system("start output.wav")


# Comparison:
"""
pyttsx3:     ⭐⭐⭐ - Offline, instant, basic quality
gTTS:        ⭐⭐⭐⭐ - Online, good quality, simple
edge-tts:    ⭐⭐⭐⭐⭐ - Online, excellent quality, free
ElevenLabs:  ⭐⭐⭐⭐⭐ - Online, best quality, limited free tier
Coqui TTS:   ⭐⭐⭐⭐ - Offline, AI-powered, slower
"""
