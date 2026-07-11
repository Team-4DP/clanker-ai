"""
provider_manager.py

Manages language model providers.
"""

from __future__ import annotations

from llm.base import BaseLLM
from llm.factory import create_llm


class ProviderManager:
    """
    Creates and manages the active language model provider.
    """

    def __init__(self) -> None:
        self._provider: BaseLLM = create_llm()

    @property
    def provider(self) -> BaseLLM:
        """
        Return the active provider.
        """
        return self._provider

    def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        """
        Send a chat request using the active provider.
        """

        return self._provider.chat(messages)