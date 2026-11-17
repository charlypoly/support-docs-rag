# Support Docs RAG

A small retrieval-augmented agent that answers questions from the Markdown files
in `docs/`. It uses OpenAI for chat and embeddings and a local Chroma database.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your OpenAI key
python -m rag.ingest   # index docs/
python -m rag.agent    # start chatting
```

## Layout

- `rag/ingest.py`: chunk and index documents
- `rag/store.py`: embeddings and vector search
- `rag/tools.py`: tools exposed to the agent (currently `search_docs`)
- `rag/agent.py`: tool-calling chat loop
