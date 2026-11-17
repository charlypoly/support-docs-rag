"""Chunk the Markdown files in docs/ and index them: python -m rag.ingest"""

from pathlib import Path

from rag.store import collection, embed

CHUNK_SIZE = 1200
OVERLAP = 200


def chunk(text: str) -> list[str]:
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start : start + CHUNK_SIZE])
        start += CHUNK_SIZE - OVERLAP
    return chunks


def main() -> None:
    for path in Path("docs").glob("**/*.md"):
        pieces = chunk(path.read_text())
        collection.upsert(
            ids=[f"{path}:{i}" for i in range(len(pieces))],
            documents=pieces,
            embeddings=embed(pieces),
            metadatas=[{"source": str(path)} for _ in pieces],
        )
        print(f"Indexed {path} ({len(pieces)} chunks)")


if __name__ == "__main__":
    main()
