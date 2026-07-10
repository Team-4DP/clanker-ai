import sqlite3
from pathlib import Path

from memory.conversation import ChatMessage


class SQLiteMemory:
    """
    Stores conversations inside a SQLite database.
    """

    def __init__(self, database: Path) -> None:
        self.database = database
        self._initialise_database()

    # Step 3
    def _initialise_database(self) -> None:
        """
        Creates the database and conversation table if they do not exist.
        """

        self.database.parent.mkdir(exist_ok=True)

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

    # Step 4
    def save_message(
        self,
        role: str,
        content: str,
    ) -> None:
        """
        Save a message to the database.
        """

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO conversation
                (
                    role,
                    content
                )
                VALUES (?, ?)
                """,
                (role, content),
            )

            connection.commit()

    # Step 5
    def get_recent_messages(
        self,
        limit: int,
    ) -> list[ChatMessage]:
        """
        Return the most recent messages.
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
            ChatMessage(role=row[0], content=row[1])
            for row in rows
        ]

        return list(reversed(messages))

    # Step 6
    def clear(self) -> None:
        """
        Delete all conversation history.
        """

        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM conversation")

            connection.commit()