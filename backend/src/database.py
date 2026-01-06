"""SQLite database initialization and connection management."""
import sqlite3
from src import config

def get_db():
    """Get database connection."""
    conn = sqlite3.connect(config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database schema."""
    conn = get_db()
    cursor = conn.cursor()

    # Members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            phone_number TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    # Payments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT NOT NULL,
            month TEXT NOT NULL,
            amount INTEGER NOT NULL CHECK(amount > 0),
            created_at TEXT NOT NULL,
            FOREIGN KEY (phone_number) REFERENCES members(phone_number) ON DELETE CASCADE
        )
    """)

    # Indexes
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_payments_phone ON payments(phone_number)
    """)

    conn.commit()
    conn.close()
