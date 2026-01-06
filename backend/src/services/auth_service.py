"""Authentication service."""
import secrets
from src import config

def validate_password(password: str) -> bool:
    """Validate admin password using constant-time comparison."""
    if not config.ADMIN_PASSWORD:
        return False
    return secrets.compare_digest(password, config.ADMIN_PASSWORD)
