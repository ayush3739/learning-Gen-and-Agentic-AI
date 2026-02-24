from ast import While
from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI
import os ,json
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
    "graph_store":{
        "provider":"neo4j",
        "config":{
            "url":os.getenv("NEO_CONNECTION_URI"),
            "username":os.getenv("NEO_USERNAME"),
            "password":os.getenv("NEO_PASSWORD"),
        }
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

    search_memory= mem_client.search(query=user_query,user_id="ayush",)

    memories=[
        f"ID: {mem.get('id')}\nMemory: {mem.get("memory")}" for mem in search_memory.get("results")
    ]

    system_prompt=f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system","content": system_prompt},
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