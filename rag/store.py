"""Vector store helpers backed by a local Chroma database."""

import chromadb
from openai import OpenAI

from rag.config import COLLECTION, DB_PATH, EMBEDDING_MODEL

_client = OpenAI()
_db = chromadb.PersistentClient(path=DB_PATH)
collection = _db.get_or_create_collection(COLLECTION)


def embed(texts: list[str]) -> list[list[float]]:
    response = _client.embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


def search(query: str, k: int = 4) -> list[dict]:
    results = collection.query(query_embeddings=embed([query]), n_results=k)
    return [
        {"text": doc, "source": meta.get("source")}
        for doc, meta in zip(results["documents"][0], results["metadatas"][0])
    ]
