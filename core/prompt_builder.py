"""
prompt_builder.py

Builds prompts for Veridion's language model.
"""

from __future__ import annotations

from core.intent import Intent
from core.prompts import (
    CHAT_PROMPT,
    CODING_PROMPT,
    DESIGN_PROMPT,
    FILE_PROMPT,
    RESEARCH_PROMPT,
    WEB_SEARCH_PROMPT,
)

from memory.conversation import ChatMessage


class PromptBuilder:
    """
    Builds conversations for the language model.
    """

    def build(
        self,
        history: list[ChatMessage],
        intent: Intent,
    ) -> list[dict[str, str]]:
        """
        Build the conversation sent to the LLM.
        """

        system_prompt = self._get_system_prompt(intent)

        messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        for message in history:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content,
                }
            )

        return messages

    def _get_system_prompt(
        self,
        intent: Intent,
    ) -> str:
        """
        Return the appropriate system prompt.
        """

        match intent:

            case Intent.CODING:
                return CODING_PROMPT

            case Intent.DESIGN:
                return DESIGN_PROMPT

            case Intent.FILE:
                return FILE_PROMPT

            case Intent.RESEARCH:
                return RESEARCH_PROMPT

            case Intent.WEB_SEARCH:
                return WEB_SEARCH_PROMPT

            case _:
                return CHAT_PROMPT