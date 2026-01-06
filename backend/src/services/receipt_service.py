"""Receipt generation service."""
from datetime import datetime

def generate_receipt(member_name: str, phone_number: str, month: str, amount: int) -> str:
    """Generate formatted receipt text."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    receipt = f"""Payment Received ✅

Gym: MuscleLab Fitness
Name: {member_name}
Mobile: {phone_number}
Month: {month}
Amount: Rs. {amount}
Date: {current_date}

Thank you for your payment 💪"""
    
    return receipt
