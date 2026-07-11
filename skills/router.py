"""
router.py

Routes intents to skills.
"""

from __future__ import annotations

from core.intent import Intent
from skills.base import BaseSkill


class SkillRouter:
    """
    Routes intents to registered skills.
    """

    def __init__(self) -> None:

        self._skills: dict[Intent, BaseSkill] = {}

    def register(
        self,
        skill: BaseSkill,
    ) -> None:

        self._skills[skill.intent] = skill

    def get(
        self,
        intent: Intent,
    ) -> BaseSkill | None:

        return self._skills.get(intent)

    def has(
        self,
        intent: Intent,
    ) -> bool:

        return intent in self._skills