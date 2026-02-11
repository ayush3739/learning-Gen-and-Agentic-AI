from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Open_ai_api_key=os.getenv('OPENAI_API_KEY')
gemini_api_key=os.getenv('Gemini_api_key')

client=OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response=client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role":"user","content":"Hey there! I am Ayush Maurya! Nice to meet you. Who are you?"}
    ]
)

print(response.choices[0].message.content)
