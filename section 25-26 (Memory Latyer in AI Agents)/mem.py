from ast import While

from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI
import os 
load_dotenv()

OpenAI_key = os.getenv("GITHUB_TOKEN")
os.environ["OPENAI_API_KEY"] = OpenAI_key

client=OpenAI(
    api_key=OpenAI_key,
    base_url="https://models.github.ai/inference"
)

config={
    "version":"v1.1",
    "embedder": {
        "provider": "openai",
        "config" : {"api_key": OpenAI_key, "model": "text-embedding-3-small" }
    },
    "llm":{
        "provider": "openai",
        "config":{"api_key": OpenAI_key, "model": "gpt-4.1-mini"}
    },
    "vector_store":{
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    }
}

mem_client = Memory.from_config(config)

while True :
    user_query = input("👉 ")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"user","content": user_query}
        ]
    )

    ai_response=response.choices[0].message.content
    print("AI:",ai_response)


    mem_client.add(
        user_id="ayush",
        messages=[
            {"role":"user","content": user_query},
            {"role":"assistant","content": ai_response}
        ]
    )

    print("Memory has been saved ")