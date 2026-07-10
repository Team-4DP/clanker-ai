"""
assistant.py

Main application controller for Veridion.
"""

from core.chat import ChatManager


class Veridion:
    """
    Main controller for the Veridion assistant.

    Coordinates the chat manager, memory,
    tools and language model.
    """

    def __init__(self) -> None:
        self.chat_manager = ChatManager()

    def chat(self, message: str) -> str:
        """
        Process a user message.

        Args:
            message: User input.

        Returns:
            Assistant response.
        """
        return self.chat_manager.chat(message)