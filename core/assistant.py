"""
assistant.py

Main Veridion assistant.
"""

from config import DATABASE_PATH, MAX_HISTORY

from core.chat import ChatManager
from core.prompt_builder import PromptBuilder

from llm.factory import create_llm

from memory.sqlite_memory import SQLiteMemory


class Veridion:
    """
    Main Veridion assistant.
    """

    def __init__(self) -> None:

        self.memory = SQLiteMemory(DATABASE_PATH)

        self.prompt_builder = PromptBuilder()

        self.llm = create_llm()

        self.chat_manager = ChatManager(
            llm=self.llm,
            memory=self.memory,
        )

    def chat(
        self,
        user_message: str,
    ) -> str:

        self.memory.save_message(
            role="user",
            content=user_message,
        )

        history = self.memory.get_recent_messages(MAX_HISTORY)

        messages = self.prompt_builder.build(history)

        response = self.chat_manager.chat(messages)

        self.memory.save_message(
            role="assistant",
            content=response,
        )

        return response