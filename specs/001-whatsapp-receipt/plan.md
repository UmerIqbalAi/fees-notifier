# Implementation Plan: Gym WhatsApp Receipt System

**Branch**: `001-whatsapp-receipt` | **Date**: 2026-01-04 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-whatsapp-receipt/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a minimal web application for gym receptionists to record monthly fee payments and send receipts via WhatsApp. The system uses phone numbers as unique customer identifiers, persists payment data in SQLite, and ensures core payment operations succeed independently of WhatsApp service availability. Authentication uses a single admin password from environment variables.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI, Pydantic, SQLite (stdlib), python-dotenv
**Storage**: SQLite (local file-based database)
**Testing**: pytest with pytest-asyncio
**Target Platform**: Serverless/cloud platform (Vercel, Railway, or similar free-tier)
**Project Type**: Web application (backend API + frontend UI)
**Performance Goals**: Sub-second response time for payment submission, support 50 concurrent requests
**Constraints**: Free-tier deployment (limited memory/CPU), must work offline if WhatsApp unavailable
**Scale/Scope**: Single gym with 1-2 receptionists, approximately 100-500 members, 1000-5000 payments/year

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Spec-Driven Development (SDD)
✅ **PASS**: Specification completed in spec.md. This plan follows after spec approval. Tasks will be generated only after plan completion.

### Principle II: Simplicity & Minimal MVP
✅ **PASS**: Implementing only features explicitly defined in spec. No additional abstractions, patterns, or frameworks beyond MVP requirements.

### Principle III: Mobile Identifier (Single Source of Truth)
✅ **PASS**: Phone number is primary key in database design. All operations (lookup, payment association, notifications) use phone number as identifier.

### Principle IV: Resilience & Independence
✅ **PASS**: Payment persistence is independent of WhatsApp service. Design uses fire-and-forget pattern for notifications with logging only.

### Principle V: Security-First Administration
✅ **PASS**: Single admin password stored in environment variable. Binary access control: authenticated or rejected. No user accounts or role complexity.

### Principle VI: Side-Effect Integrity
✅ **PASS**: Payment save operation commits before WhatsApp notification attempt. Notification failures are logged but do not affect payment transaction.

### Technology Constraints Compliance
✅ **PASS**: Using Python + FastAPI + Pydantic + SQLite as mandated. Frontend will be simple Next.js or HTML. Deployment targets Vercel-compatible free-tier platforms.

**Gate Status**: ✅ **ALL CHECKS PASSED** - Proceed to Phase 0 Research

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── member.py          # Member entity (phone, name, timestamps)
│   │   └── payment.py         # Payment entity (id, phone, month, amount, timestamps)
│   ├── services/
│   │   ├── auth_service.py    # Admin password validation
│   │   ├── payment_service.py # Payment creation, member lookup/creation
│   │   ├── receipt_service.py # Receipt text generation
│   │   └── whatsapp_service.py # WhatsApp notification (optional)
│   ├── api/
│   │   ├── auth.py            # POST /login endpoint
│   │   └── payments.py        # POST /payments endpoint
│   ├── database.py            # SQLite connection and initialization
│   ├── config.py              # Environment variable loading
│   └── main.py                # FastAPI application entry point
└── tests/
    ├── test_auth.py           # Auth service tests
    ├── test_payment.py        # Payment service tests
    └── test_receipt.py        # Receipt generation tests

frontend/
├── src/
│   ├── pages/
│   │   ├── login.tsx          # Login page
│   │   └── payment.tsx        # Payment recording page
│   ├── components/
│   │   ├── PaymentForm.tsx    # Payment input form
│   │   └── ReceiptDisplay.tsx # Receipt preview component
│   └── services/
│       └── api.ts             # API client for backend calls
└── tests/
    └── components.test.tsx    # Component tests

.env.example                   # Template for environment variables
README.md                      # Setup and deployment instructions
requirements.txt               # Python dependencies
```

**Structure Decision**: Selected **Option 2: Web application** structure. Rationale: The feature requires both a backend API (FastAPI) for payment processing and a frontend UI (Next.js) for receptionist interaction. Separating backend and frontend allows independent deployment (backend on serverless, frontend on Vercel static hosting) and clear responsibility boundaries.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations. All constitution checks passed.
