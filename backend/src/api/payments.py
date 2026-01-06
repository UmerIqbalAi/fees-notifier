"""Payment endpoints."""
from fastapi import APIRouter, HTTPException, Cookie, Query
from src.models.payment import PaymentRequest, PaymentResponse
from src.services import payment_service, receipt_service

router = APIRouter()

@router.post("/payments", response_model=PaymentResponse)
def create_payment(request: PaymentRequest, session: str | None = Cookie(default=None)):
    """Create payment and return receipt."""
    # Check authentication
    if session != "authenticated":
        raise HTTPException(status_code=401, detail="Admin authentication required")

    try:
        # Create or get member
        phone, name = payment_service.create_or_get_member(
            request.phone_number,
            request.member_name
        )

        # Save payment (will raise ValueError if duplicate)
        payment_id = payment_service.save_payment(
            phone,
            request.month.value,
            request.amount
        )

        # Generate receipt
        receipt = receipt_service.generate_receipt(
            name,
            phone,
            request.month.value,
            request.amount
        )

        return PaymentResponse(payment_id=payment_id, receipt=receipt)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save payment")

@router.get("/payments")
def list_payments(month: str | None = Query(default=None), session: str | None = Cookie(default=None)):
    """Get all payments with optional month filter."""
    # Check authentication
    if session != "authenticated":
        raise HTTPException(status_code=401, detail="Admin authentication required")

    try:
        return payment_service.get_payments(month)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch payments")
