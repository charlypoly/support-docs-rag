import os

from dotenv import load_dotenv

load_dotenv()

CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-6-astra")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
DB_PATH = os.getenv("CHROMA_PATH", ".chroma")
COLLECTION = "docs"
