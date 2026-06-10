import pypdf
import anthropic
import os
from dotenv import load_dotenv
import chromadb
from rag.ingest import create_collection, embed_chunks
from rag.retrieve import retrieve_chunks
import json
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
chroma_client = chromadb.PersistentClient(path="C:\\Users\\mikeo\\Projects\\Project1-CLI\\rag\\chromadb")
def ask(question: str) -> str:
    chunks = retrieve_chunks(question, 2) #If you need more chunks, you change here, set for 2 just for speed of testing
    content = chunks + [f"Question: {question}"] # The question should be the last element in the list of messages.
    result = [{"role": "user", "content": content}]
    system_prompt = """You are trying to answer relevant questions based on the context provided in the message.
    Only answer based on the context, if the answer is not in the context, say "You could not find the answer."
    Do not answer based on your own or external knowledge.
    The context will be fed to you in the form of chunks in the input message together with the question.
    I will pass the context and questions as a string.
    The question will be start from the string "Question:"
    The rest of the string are the context pulled from the vector database.
    """ #Set up system prompt to place guard rails for the RAG system.
    try:
        response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=system_prompt,
        messages=result
     )
    except anthropic.APIStatusError as e:
       print(f"HTTP error occurred: {e.status_code} - {e.message}")
       return
    except anthropic.APIConnectionError as e:
        print(f"Connection error occurred: {e}")
        return
    except anthropic.APITimeoutError as e:
        print(f"Request timed out: {e}")
        return
    except  anthropic.APIError as e:
        print(f"An error occurred: {e}")
        return
    return response.content[0].text
print(ask("How was OCBC financial performance?"))