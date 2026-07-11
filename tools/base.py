"""
base.py

Defines the base interface for all Veridion tools.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Abstract base class for all Veridion tools.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Name of the tool.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Short description of the tool.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        query: str,
        **kwargs,
    ) -> str:
        """
        Execute the tool.

        Args:
            query:
                User query.

            **kwargs:
                Additional tool-specific arguments.

        Returns:
            Tool output.
        """
        raise NotImplementedError