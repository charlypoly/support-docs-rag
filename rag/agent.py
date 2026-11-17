"""Chat with the docs agent: python -m rag.agent"""

import json

from openai import OpenAI

from rag.config import CHAT_MODEL
from rag.tools import HANDLERS, TOOLS

client = OpenAI()

SYSTEM_PROMPT = (
    "You answer questions using the tools available to you. "
    "Cite the source of each fact you use."
)


def answer(question: str, history: list[dict] | None = None) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, *(history or [])]
    messages.append({"role": "user", "content": question})
    for _ in range(8):
        response = client.chat.completions.create(
            model=CHAT_MODEL, messages=messages, tools=TOOLS
        )
        message = response.choices[0].message
        messages.append(message.model_dump(exclude_none=True))
        if not message.tool_calls:
            return message.content or ""
        for call in message.tool_calls:
            args = json.loads(call.function.arguments or "{}")
            result = HANDLERS[call.function.name](**args)
            messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
    return "Stopped after too many tool calls."


def main() -> None:
    while True:
        question = input("> ").strip()
        if question in {"", "exit", "quit"}:
            break
        print(answer(question))


if __name__ == "__main__":
    main()
