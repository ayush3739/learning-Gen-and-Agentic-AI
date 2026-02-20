from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv("./.env")

openai_client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN"),
)

embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base="https://models.github.ai/inference",
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

#Take user Input 
user_query=input("Ask Something : ")

# Relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context= "\n\n\n".join([f"Page Content : {result.page_content} \n Page Number : {result.metadata['page_label']}\nfile Location : {result.metadata['source']}" for result in search_results])

System_prompt=f"""
    You are a helpful assistant who answers user query based on the available context.
    retreived from the PDF file along with page_contents and page_number.

    You should onle answer the user based on the following contect and navigate the 
    user to open the right page number to know more about the topic.

    CONTEXT:
    {context}
"""

response=openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":System_prompt},
        {"role":"user","content":user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")