"""
intent.py

Defines the supported intents for Veridion.
"""

from __future__ import annotations

from enum import Enum


class Intent(Enum):
    """
    High-level user intents.
    """

    CHAT = "chat"
    CODING = "coding"
    RESEARCH = "research"
    WEB_SEARCH = "web_search"
    FILE = "file"
    PLANNING = "planning"