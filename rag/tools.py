"""Tools the agent can call. Each entry has an OpenAI tool schema and a handler."""

import json

from rag.store import search

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": "Search the internal knowledge base for relevant passages.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    }
]


def search_docs(query: str) -> str:
    return json.dumps(search(query))


HANDLERS = {"search_docs": search_docs}
