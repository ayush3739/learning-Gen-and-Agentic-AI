from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
load_dotenv('./.env')

pdf_path=Path(__file__).parent / "node-js.pdf" 

#load this file in python program

loader=PyPDFLoader(file_path=pdf_path)
docs=loader.load()

print(docs[12]) #125
# print(len(docs))


#Split the docs into Smaller chunks

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400,
)

chunks=text_splitter.split_documents(documents=docs)


#Vector Embeddings for this chunk
embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=os.getenv("GITHUB_TOKEN"),
    openai_api_base="https://models.github.ai/inference",
)

vector_store=QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",

)

print("Indexing of documents done..")