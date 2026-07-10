import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is missing. Check your .env file.")
from pathlib import Path

# -------------------------
# Project Paths
# -------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"

DATABASE_PATH = DATA_DIR / "veridion.db"

# -------------------------
# AI Settings
# -------------------------

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

MAX_HISTORY = 20