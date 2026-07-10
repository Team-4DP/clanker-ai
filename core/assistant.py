"""
assistant.py

Main application controller for Veridion.
"""

from core.chat import ChatManager

from config import DATABASE_PATH

from memory.sqlite_memory import SQLiteMemory


class Veridion:
    """
    Main controller for the Veridion assistant.

    Coordinates the chat manager, memory,
    tools and language model.
    """

    def __init__(self) -> None:
        self.memory = SQLiteMemory(DATABASE_PATH)
        self.chat_manager = ChatManager(
    memory=self.memory,
)

    def chat(self, message: str) -> str:
        """
        Process a user message.

        Args:
            message: User input.

        Returns:
            Assistant response.
        """
        return self.chat_manager.chat(message)