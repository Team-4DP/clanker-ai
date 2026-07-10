"""
config.py

Central configuration for Veridion.

This module contains configurable settings used throughout the
application. It should not contain application logic.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# ---------------------------------------------------------------------
# Load environment variables
# ---------------------------------------------------------------------

load_dotenv()

# ---------------------------------------------------------------------
# Project Paths
# ---------------------------------------------------------------------

PROJECT_ROOT: Path = Path(__file__).resolve().parent

DATA_DIR: Path = PROJECT_ROOT / "data"

DATABASE_PATH: Path = DATA_DIR / "veridion.db"

# ---------------------------------------------------------------------
# Hugging Face
# ---------------------------------------------------------------------

HF_TOKEN: str | None = os.getenv("HF_TOKEN")

MODEL_NAME: str = "Qwen/Qwen2.5-7B-Instruct"

# ---------------------------------------------------------------------
# Conversation
# ---------------------------------------------------------------------

MAX_HISTORY: int = 20

# ---------------------------------------------------------------------
# Generation Settings
# ---------------------------------------------------------------------

TEMPERATURE: float = 0.7

MAX_NEW_TOKENS: int = 1024

# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------

LOG_LEVEL: str = "INFO"

LOG_FORMAT: str = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)