from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
import os
import asyncio
import edge_tts
import pygame
import time  

load_dotenv('./.env')

client=OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.github.ai/inference"
)

async def tts(speech: str):
    print("Speaking...")
    
    communicate = edge_tts.Communicate(speech, "en-US-AriaNeural")
    await communicate.save("temp_audio.mp3")
    
    # Play audio in background without opening media player GUI
    pygame.mixer.init()
    pygame.mixer.music.load("temp_audio.mp3")
    pygame.mixer.music.play()
    
    # Wait for audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    pygame.mixer.quit()


def main():
    r= sr.Recognizer() # speech to text 

    with sr.Microphone() as source: # mic input
        r.adjust_for_ambient_noise(source) # adjust for ambient noise
        r.pause_threshold=2 # pause threshold

        SYSTEM_PROMPT="""
                You are a expert voice agent . You are given the transcipt of what user has said using voice
                You need to output as if you are an voice agent and whatever you speak 
                will be converted back to audio using AI and played back to user.
            """
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
        ] 
        
        while True:

            print("Speak Something...") # print listening
            audio= r.listen(source) # listen to the source

            print("Processing Audio... (STT)") # print processing
            stt=r.recognize_google(audio) # speech to text using google api

            print("You said: ", stt) # print what user said

            messages.append({"role":"user","content":stt}) 

            response=client.chat.completions.create(
                model="gpt-4o-mini",  
                messages=messages
            )

            print("AI Response: ",response.choices[0].message.content)
            asyncio.run(tts(speech=response.choices[0].message.content))
main()