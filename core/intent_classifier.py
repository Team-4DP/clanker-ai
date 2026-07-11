"""
intent_classifier.py

Determines the user's intent from their message.
"""

from __future__ import annotations

from core.intent import Intent


class IntentClassifier:
    """
    Classifies user messages into high-level intents.
    """

    def __init__(self) -> None:
        """
        Initialise the classifier.
        """
        self._coding_keywords = {
            "python",
            "java",
            "javascript",
            "c++",
            "c#",
            "rust",
            "go",
            "bug",
            "error",
            "debug",
            "code",
            "coding",
            "program",
            "function",
            "class",
            "algorithm",
            "api",
        }

        self._web_keywords = {
            "search",
            "latest",
            "news",
            "today",
            "current",
            "recent",
            "internet",
            "online",
            "web",
            "look up",
            "lookup",
        }

        self._file_keywords = {
            "file",
            "folder",
            "directory",
            "read",
            "analyse",
            "analyze",
            "document",
            "pdf",
            "image",
            "zip",
            "csv",
            "json",
        }

        self._planning_keywords = {
            "plan",
            "roadmap",
            "design",
            "architecture",
            "strategy",
            "project",
            "organise",
            "organize",
        }

    def classify(self, message: str) -> Intent:
        """
        Determine the user's intent.

        Args:
            message:
                The user's message.

        Returns:
            The detected Intent.
        """

        text = message.lower()

        if any(keyword in text for keyword in self._coding_keywords):
            return Intent.CODING

        if any(keyword in text for keyword in self._web_keywords):
            return Intent.WEB_SEARCH

        if any(keyword in text for keyword in self._file_keywords):
            return Intent.FILE

        if any(keyword in text for keyword in self._planning_keywords):
            return Intent.PLANNING

        return Intent.CHAT