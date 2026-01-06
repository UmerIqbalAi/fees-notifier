"""Payment data model."""
from pydantic import BaseModel, Field
from enum import Enum

class Month(str, Enum):
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"

class PaymentRequest(BaseModel):
    phone_number: str
    member_name: str | None = None
    month: Month
    amount: int = Field(gt=0)

class PaymentResponse(BaseModel):
    payment_id: int
    receipt: str
