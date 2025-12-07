import fitz  # PyMuPDF
from langchain_ollama import ChatOllama
from apify_client import ApifyClient
from dotenv import load_dotenv
import os
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file."""
    docs = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in docs:
        text += page.get_text("text")
    return text

def ask_ollama(prompt, max_tokens=500):
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        max_tokens=max_tokens
    )

    try:
        result = llm.invoke(prompt)
        return result.content.strip()   # clean output
    except Exception as e:
        return f"LLM Error: {str(e)}"



