from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Open_ai_api_key=os.getenv('OPENAI_API_KEY')

client=OpenAI()

response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":"Hey there!"}
    ]
)

print(response.choices)
