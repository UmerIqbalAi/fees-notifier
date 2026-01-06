# Feature Specification: Gym WhatsApp Receipt System

**Feature Branch**: `001-whatsapp-receipt`
**Created**: 2026-01-04
**Status**: Draft
**Input**: User description: "Provide a simple internal web application that allows a gym receptionist to record monthly fee payments and automatically send a receipt to the customer via WhatsApp."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Record Payment and Generate Receipt (Priority: P1)

The receptionist logs into the system, enters a customer's phone number and payment details, and the system saves the payment and returns a formatted receipt. This is the core MVP functionality.

**Why this priority**: This is the fundamental value proposition - recording payments and generating receipts. Without this, the system has no purpose. This can operate completely independently without WhatsApp integration.

**Independent Test**: Can be fully tested by logging in, entering payment details for a new or existing customer, and verifying that the payment is saved and a formatted receipt is returned. Delivers immediate value by digitizing payment records.

**Acceptance Scenarios**:

1. **Given** the receptionist is logged in and a new customer visits, **When** the receptionist enters the phone number, member name, month, and amount, **Then** the system creates a new member record, saves the payment, and returns a formatted receipt with all details.

2. **Given** the receptionist is logged in and an existing customer returns, **When** the receptionist enters the phone number and payment details, **Then** the system reuses the existing member record, saves the payment, and returns a formatted receipt.

3. **Given** the receptionist enters invalid data (missing required fields, invalid phone format), **When** the receptionist submits the payment form, **Then** the system displays clear validation errors and does not save the payment.

4. **Given** a payment has been successfully saved, **When** the system generates the receipt, **Then** the receipt includes: gym name (MuscleLab Fitness), member name, phone number, month, amount in PKR, current date, and thank you message.

---

### User Story 2 - Admin Authentication (Priority: P1)

The receptionist must authenticate using a single admin password before accessing payment recording features. This protects sensitive financial data from unauthorized access.

**Why this priority**: Security is non-negotiable for a payment system. This must be implemented before any payment features are accessible. This is a foundational requirement that enables the core payment functionality.

**Independent Test**: Can be fully tested by attempting to access payment features without login (should be blocked), logging in with correct password (should succeed), and logging in with incorrect password (should fail). Delivers immediate security value.

**Acceptance Scenarios**:

1. **Given** the receptionist is not logged in, **When** they attempt to access the payment recording page, **Then** they are redirected to the login page.

2. **Given** the receptionist is on the login page, **When** they enter the correct admin password and submit, **Then** they are authenticated and redirected to the payment recording page.

3. **Given** the receptionist is on the login page, **When** they enter an incorrect password and submit, **Then** they see an error message and remain on the login page.

4. **Given** the receptionist is logged in, **When** their session expires or they log out, **Then** they must re-authenticate to access payment features.

---

### User Story 3 - WhatsApp Receipt Notification (Priority: P2)

After successfully recording a payment, the system automatically sends the receipt to the customer via WhatsApp. This is a convenience feature that enhances the customer experience.

**Why this priority**: This is valuable but not essential to the core payment recording functionality. The system must work even if WhatsApp fails (per constitution principle IV). This can be added after the core payment system is proven to work.

**Independent Test**: Can be fully tested by recording a payment and verifying that a WhatsApp message is sent to the customer's phone number with the receipt text. If WhatsApp fails, the payment should still be saved successfully. Delivers customer convenience value.

**Acceptance Scenarios**:

1. **Given** a payment has been successfully saved, **When** the WhatsApp service is available, **Then** the system sends the formatted receipt to the customer's phone number via WhatsApp.

2. **Given** a payment has been successfully saved, **When** the WhatsApp service is unavailable or fails, **Then** the system logs the failure but does not rollback the payment, and the receptionist is notified of the notification failure.

3. **Given** a WhatsApp notification is sent, **When** the customer receives it, **Then** the message contains the complete formatted receipt with all payment details.

---

### Edge Cases

- What happens when a receptionist enters a duplicate payment for the same customer and month?
- How does the system handle phone numbers in different formats (with/without country code, spaces, dashes)?
- What happens when the database is locked or unavailable during payment submission?
- How does the system handle concurrent payment submissions from multiple receptionists?
- What happens when the WhatsApp service is temporarily down but recovers later?
- How does the system handle very long member names or special characters?
- What happens when a receptionist stays logged in for an extended period (session timeout)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST require authentication via a single admin password before allowing access to payment recording features.
- **FR-002**: System MUST validate the admin password against an environment variable (no hardcoded passwords).
- **FR-003**: System MUST use phone number as the unique identifier for all customer records.
- **FR-004**: System MUST create a new member record when a phone number is encountered for the first time, requiring member name input.
- **FR-005**: System MUST reuse existing member records when a phone number already exists in the system.
- **FR-006**: System MUST validate all payment inputs: phone number (required, valid format), member name (required for new members), month (required, one of January-December), amount (required, positive integer).
- **FR-007**: System MUST persist member data including: phone number (primary key), name, and creation timestamp.
- **FR-008**: System MUST persist payment data including: unique ID, phone number (foreign key), month, amount, and creation timestamp.
- **FR-009**: System MUST generate a formatted receipt following the template: "Payment Received ✅\n\nGym: MuscleLab Fitness\nName: {member_name}\nMobile: {phone_number}\nMonth: {month}\nAmount: Rs. {amount}\nDate: {current_date}\n\nThank you for your payment 💪"
- **FR-010**: System MUST return the formatted receipt in the payment submission response.
- **FR-011**: System MUST trigger WhatsApp notification after successful payment save (best-effort, failures must not affect payment persistence).
- **FR-012**: System MUST log all WhatsApp notification failures without rolling back the payment transaction.
- **FR-013**: System MUST return HTTP 401 for unauthorized access attempts to protected endpoints.
- **FR-014**: System MUST return appropriate error messages for validation failures (HTTP 400) and server errors (HTTP 500).
- **FR-015**: System MUST support session-based authentication with logout capability.

### Key Entities

- **Member**: Represents a gym customer. Identified uniquely by phone number. Contains: phone number (string, primary key), name (string), creation timestamp (datetime).

- **Payment**: Represents a monthly fee payment made by a member. Contains: unique ID (auto-generated), phone number (foreign key to Member), month (enum: January-December), amount (integer in PKR), creation timestamp (datetime).

- **Receipt**: Represents the formatted text output generated after a successful payment. Not persisted; generated dynamically from payment and member data.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Receptionist can record a payment and receive a formatted receipt in under 30 seconds from login.
- **SC-002**: System successfully saves 100% of payment submissions when validation passes, regardless of WhatsApp service status.
- **SC-003**: System prevents unauthorized access to payment features in 100% of cases when admin password is not provided.
- **SC-004**: Customers receive WhatsApp notifications for at least 95% of payments when WhatsApp service is operational.
- **SC-005**: System handles at least 50 concurrent payment submissions without data loss or significant performance degradation.
- **SC-006**: Payment data remains intact and queryable even after multiple WhatsApp service failures.

## Assumptions

- Phone numbers will be provided in a consistent format (implementation will define normalization rules).
- The gym operates in Pakistan (PKR currency, phone number formats).
- A single receptionist will typically be using the system, though concurrent access should be supported.
- WhatsApp integration will use a third-party service (Twilio or Meta API) configured via environment variables.
- Session timeout will be set to a reasonable duration (e.g., 8 hours) to avoid frequent re-authentication during business hours.
- The system will be deployed on a free-tier platform (Vercel or similar).
- Payment amounts are recorded as integers (no decimal currency units for this MVP).
- Members pay monthly fees; duplicate payments for the same month should be allowed (business rule to be confirmed during planning).
