"""
sqlite_memory.py

Provides persistent conversation storage for Veridion using SQLite.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from memory.conversation import ChatMessage


class SQLiteMemory:
    """
    Handles persistent conversation storage using SQLite.

    This class is responsible for:
        - Creating the database
        - Saving messages
        - Loading recent messages
        - Clearing conversation history

    No other part of Veridion should interact with SQLite directly.
    """

    def __init__(self, database: Path) -> None:
        """
        Initialise the SQLite memory service.

        Args:
            database:
                Path to the SQLite database file.
        """
        self.database = database
        self._initialise_database()

    def _initialise_database(self) -> None:
        """
        Create the database and conversation table if they do not exist.
        """

        self.database.parent.mkdir(parents=True, exist_ok=True)

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS conversation (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

            connection.commit()

    def save_message(
        self,
        role: str,
        content: str,
    ) -> None:
        """
        Save a message to the conversation history.

        Args:
            role:
                Message sender ("user", "assistant", etc.).

            content:
                Message text.
        """

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO conversation (
                    role,
                    content
                )
                VALUES (?, ?)
                """,
                (role, content),
            )

            connection.commit()

    def get_recent_messages(
        self,
        limit: int,
    ) -> list[ChatMessage]:
        """
        Retrieve the most recent conversation messages.

        Args:
            limit:
                Maximum number of messages to return.

        Returns:
            Messages ordered from oldest to newest.
        """

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    role,
                    content
                FROM conversation
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            )

            rows = cursor.fetchall()

        messages = [
            ChatMessage(
                role=row[0],
                content=row[1],
            )
            for row in rows
        ]

        return list(reversed(messages))

    def clear(self) -> None:
        """
        Remove all conversation history.
        """

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM conversation")

            connection.commit()

    def count_messages(self) -> int:
        """
        Return the number of stored messages.

        Returns:
            Total message count.
        """

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM conversation
                """
            )

            result = cursor.fetchone()

        return int(result[0]) if result else 0