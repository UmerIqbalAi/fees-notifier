"""Payment service."""
from datetime import datetime
from src.database import get_db

def create_or_get_member(phone_number: str, name: str | None = None) -> tuple[str, str]:
    """Create new member or get existing one. Returns (phone, name)."""
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if member exists
    cursor.execute("SELECT name FROM members WHERE phone_number = ?", (phone_number,))
    result = cursor.fetchone()
    
    if result:
        conn.close()
        return (phone_number, result[0])
    
    # New member - name is required
    if not name:
        conn.close()
        raise ValueError("Member name required for new customers")
    
    # Create new member
    created_at = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO members (phone_number, name, created_at) VALUES (?, ?, ?)",
        (phone_number, name, created_at)
    )
    conn.commit()
    conn.close()
    
    return (phone_number, name)

def save_payment(phone_number: str, month: str, amount: int) -> int:
    """Save payment and return payment ID. Raises ValueError if duplicate."""
    conn = get_db()
    cursor = conn.cursor()

    # Check for duplicate payment
    cursor.execute(
        "SELECT id FROM payments WHERE phone_number = ? AND month = ?",
        (phone_number, month)
    )
    existing = cursor.fetchone()

    if existing:
        conn.close()
        raise ValueError("Payment already recorded for this member for this month")

    created_at = datetime.now().isoformat()
    cursor.execute(
        "INSERT INTO payments (phone_number, month, amount, created_at) VALUES (?, ?, ?, ?)",
        (phone_number, month, amount, created_at)
    )

    payment_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return payment_id

def get_payments(month: str | None = None) -> dict:
    """Get all payments, optionally filtered by month. Returns summary + list."""
    conn = get_db()
    cursor = conn.cursor()

    if month:
        query = """
            SELECT p.id, m.name, p.phone_number, p.month, p.amount, p.created_at
            FROM payments p
            JOIN members m ON p.phone_number = m.phone_number
            WHERE p.month = ?
            ORDER BY p.created_at DESC
        """
        cursor.execute(query, (month,))
    else:
        query = """
            SELECT p.id, m.name, p.phone_number, p.month, p.amount, p.created_at
            FROM payments p
            JOIN members m ON p.phone_number = m.phone_number
            ORDER BY p.created_at DESC
        """
        cursor.execute(query)

    rows = cursor.fetchall()
    payments = [
        {
            "id": row[0],
            "name": row[1],
            "phone_number": row[2],
            "month": row[3],
            "amount": row[4],
            "created_at": row[5]
        }
        for row in rows
    ]

    total_count = len(payments)
    total_amount = sum(p["amount"] for p in payments)

    conn.close()

    return {
        "payments": payments,
        "total_count": total_count,
        "total_amount": total_amount
    }
