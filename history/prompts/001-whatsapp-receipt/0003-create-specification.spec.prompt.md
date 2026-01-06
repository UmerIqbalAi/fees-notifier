---
id: 3
title: Create Gym WhatsApp Receipt System Specification
stage: spec
date: 2026-01-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-whatsapp-receipt
branch: 001-whatsapp-receipt
user: NLN
command: /sp.specify
labels: [specification, gym, whatsapp, payments, receipt]
links:
  spec: specs/001-whatsapp-receipt/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-whatsapp-receipt/spec.md
  - specs/001-whatsapp-receipt/checklists/requirements.md
tests:
  - none
---

## Prompt

# Gym WhatsApp Receipt System – Specification

## Goal
Provide a simple internal web application that allows a gym receptionist
to record monthly fee payments and automatically send a receipt to the
customer via WhatsApp.

## Primary Actor
- Receptionist (authorized via admin password)

## Authentication
- System must require a single admin password to access protected features.
- Password is checked against an environment variable.
- No usernames or accounts are required.

## Unique Customer Identifier
- phone_number (string) is the unique identifier for a customer.
- If a phone number already exists, the existing customer record is reused.

## Inputs
- phone_number: string (required, unique)
- member_name: string (required on first entry)
- month: enum (January–December)
- amount: integer (PKR)

## Core Behavior
1. Receptionist logs in using admin password.
2. Receptionist enters phone number and payment details.
3. System validates input.
4. System creates or reuses member record.
5. System stores payment in database.
6. System generates receipt text.
7. System returns receipt data in response.
8. System optionally triggers WhatsApp notification.

## Receipt Format
Receipt text must follow this template:

Payment Received ✅

Gym: MuscleLab Fitness
Name: {member_name}
Mobile: {phone_number}
Month: {month}
Amount: Rs. {amount}
Date: {current_date}

Thank you for your payment 💪

## API Requirements

### Authentication
- POST /login
- Accepts admin password
- Returns a session/token or simple auth flag

### Payments
- POST /payments
- Protected endpoint (requires login)
- Saves payment and returns receipt

## Persistence

### Members Table
- phone_number (primary key)
- name
- created_at

### Payments Table
- id
- phone_number (foreign key)
- month
- amount
- created_at

## WhatsApp Integration (Optional)
- Triggered only after successful payment save.
- Uses external service (Twilio or Meta).
- Failures must be logged but ignored.

## Error Handling
- Unauthorized access → HTTP 401
- Invalid input → HTTP 400

## Response snapshot

Created comprehensive specification with 3 prioritized user stories (P1: Record Payment, P1: Admin Auth, P2: WhatsApp Notification), 15 functional requirements, 6 measurable success criteria, and a complete quality checklist. All requirements are testable, technology-agnostic, and ready for planning phase.

## Outcome

- ✅ Impact: Complete feature specification ready for technical planning
- 🧪 Tests: Acceptance scenarios defined for all 3 user stories
- 📁 Files: specs/001-whatsapp-receipt/spec.md, specs/001-whatsapp-receipt/checklists/requirements.md
- 🔁 Next prompts: /sp.plan to create technical implementation plan
- 🧠 Reflection: Successfully translated user requirements into a testable, business-focused specification following SDD principles.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): Quality checklist - PASS (all items checked)
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
