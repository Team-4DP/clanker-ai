from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """
    Represents one conversation message.
    """

    role: str
    content: str