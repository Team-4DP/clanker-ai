"""
registry.py

Stores and retrieves Veridion tools.
"""

from __future__ import annotations

from tools.base import BaseTool


class ToolRegistry:
    """
    Registry of available tools.
    """

    def __init__(self) -> None:

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        """
        Register a tool.
        """

        self._tools[tool.name] = tool

    def get(
        self,
        name: str,
    ) -> BaseTool | None:
        """
        Return a registered tool.
        """

        return self._tools.get(name)

    def all_tools(
        self,
    ) -> list[BaseTool]:
        """
        Return every registered tool.
        """

        return list(self._tools.values())