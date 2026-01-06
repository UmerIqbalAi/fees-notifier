"""Configuration from environment variables."""
import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
DATABASE_PATH = os.getenv("DATABASE_PATH", "./gym_payments.db")
