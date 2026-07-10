"""
chat.py

Handles conversations between the user and the LLM.
"""

from llm.hf_client import ask_ai


class ChatManager:
    """
    Handles user conversations.
    """

    def chat(self, message: str) -> str:
        """
        Send the user's message to the language model.

        Args:
            message: User input.

        Returns:
            Model response.
        """

        return ask_ai(message)