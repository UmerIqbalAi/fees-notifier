# Gym WhatsApp Receipt System

A minimal web application for gym receptionists to record monthly fee payments and generate receipts.

## Features

- ✅ Admin authentication with single password
- ✅ Record payments with phone number as unique identifier
- ✅ Automatic member record creation/reuse
- ✅ Formatted receipt generation
- ✅ SQLite persistence
- ✅ Simple web UI

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Setup

1. **Clone the repository**
```bash
git clone <repo-url>
cd fees_notifier
```

2. **Create environment file**
```bash
cp .env.example .env
```

Edit `.env` and set your admin password:
```
ADMIN_PASSWORD=your_secure_password_here
DATABASE_PATH=./gym_payments.db
```

3. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

4. **Run the backend**
```bash
cd backend
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

5. **Open the frontend**

Open `frontend/src/pages/login.html` in your web browser.

## Project Structure

```
├── backend/
│   ├── src/
│   │   ├── api/              # API endpoints
│   │   ├── models/           # Pydantic models
│   │   ├── services/         # Business logic
│   │   ├── config.py         # Environment configuration
│   │   ├── database.py       # SQLite setup
│   │   └── main.py           # FastAPI app
│   └── requirements.txt
├── frontend/
│   └── src/
│       └── pages/
│           ├── login.html    # Login page
│           └── payment.html  # Payment recording page
├── .env.example              # Environment template
└── README.md
```

## Usage

1. **Login**: Use the admin password from your `.env` file
2. **Record Payment**:
   - Enter phone number (e.g., 03001234567)
   - Enter member name (required for new members only)
   - Select month
   - Enter amount in PKR
3. **View Receipt**: Receipt is displayed after successful payment

## API Endpoints

### POST /login
Authenticate receptionist with admin password.

**Request:**
```json
{
  "password": "your_password"
}
```

**Response:** Sets session cookie for 8 hours

### POST /payments
Record payment and return receipt (requires authentication).

**Request:**
```json
{
  "phone_number": "03001234567",
  "member_name": "Ahmed Ali",
  "month": "January",
  "amount": 5000
}
```

**Response:**
```json
{
  "payment_id": 42,
  "receipt": "Payment Received ✅\n\nGym: MuscleLab Fitness\n..."
}
```

## Database Schema

### Members
- `phone_number` (TEXT, PRIMARY KEY)
- `name` (TEXT, NOT NULL)
- `created_at` (TEXT, NOT NULL)

### Payments
- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT)
- `phone_number` (TEXT, FOREIGN KEY)
- `month` (TEXT, NOT NULL)
- `amount` (INTEGER, NOT NULL, CHECK > 0)
- `created_at` (TEXT, NOT NULL)

## Configuration

Environment variables (`.env` file):

- `ADMIN_PASSWORD`: Admin password for receptionist login (required)
- `DATABASE_PATH`: Path to SQLite database file (default: `./gym_payments.db`)

## Development

### Run tests
```bash
cd backend
pytest
```

### API Documentation
Visit `http://localhost:8000/docs` for auto-generated Swagger UI documentation.

## License

MIT
