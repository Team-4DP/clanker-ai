"""
base.py

Defines the abstract interface for all language model providers.

Every provider (Hugging Face, Ollama, OpenAI, etc.) must implement
this interface so the rest of Veridion can remain provider-agnostic.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for language model providers.
    """

    @abstractmethod
    def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """
        Generate a response from the language model.

        Args:
            messages:
                A list of chat messages in OpenAI-compatible format.
                Example:

                [
                    {"role": "system", "content": "..."},
                    {"role": "user", "content": "..."}
                ]

        Returns:
            The assistant's response.
        """

        raise NotImplementedError