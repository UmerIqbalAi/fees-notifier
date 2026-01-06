"""Member data model."""
from pydantic import BaseModel

class Member(BaseModel):
    phone_number: str
    name: str
    created_at: str
