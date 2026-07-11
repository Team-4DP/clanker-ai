"""
providers.py

Defines supported LLM providers.
"""

from enum import Enum


class LLMProvider(Enum):
    """
    Supported language model providers.
    """

    HUGGINGFACE = "huggingface"

    OLLAMA = "ollama"

    OPENAI = "openai"

    ANTHROPIC = "anthropic"

    GEMINI = "gemini"