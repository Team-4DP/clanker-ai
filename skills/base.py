"""
base.py

Defines the base interface for Veridion skills.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.intent import Intent


class BaseSkill(ABC):
    """
    Base class for every Veridion skill.
    """

    @property
    @abstractmethod
    def intent(self) -> Intent:
        """
        Intent handled by this skill.
        """
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        message: str,
        **kwargs,
    ):
        """
        Execute the skill.

        Returns any data needed to answer the user.
        """
        raise NotImplementedError