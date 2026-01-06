<!--
Sync Impact Report:
- Version change: [CONSTITUTION_VERSION] -> 1.0.0
- List of modified principles (old title -> new title if renamed):
    - [PRINCIPLE_1_NAME] -> I. Spec-Driven Development (SDD)
    - [PRINCIPLE_2_NAME] -> II. Simplicity & Minimal MVP
    - [PRINCIPLE_3_NAME] -> III. Mobile Identifier (Single Source of Truth)
    - [PRINCIPLE_4_NAME] -> IV. Resilience & Independence
    - [PRINCIPLE_5_NAME] -> V. Security-First Administration
    - [PRINCIPLE_6_NAME] -> VI. Side-Effect Integrity
- Added sections: Core Principles, Technology Constraints, Development Workflow
- Removed sections: none
- Templates requiring updates (✅ updated / ⚠ pending) with file paths:
    - .specify/templates/plan-template.md (⚠ pending - instruction context updated)
    - .specify/templates/spec-template.md (⚠ pending - configuration alignment)
    - .specify/templates/tasks-template.md (⚠ pending - task categorization)
- Follow-up TODOs if any placeholders intentionally deferred:
    - none
-->

# Fees Notifier Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
The project MUST strictly follow Spec-Driven Development. Every feature begins with a specification, followed by a plan and tasks. Code implementation MUST ONLY occur after design approval and implementation of tests that verify the requirements.

### II. Simplicity & Minimal MVP
The system is built as a minimal, production-ready MVP for small gym business. Prioritize simplicity, clarity, and reliability over extensive features. Avoid over-engineering; if a feature is not explicitly defined in the spec, it MUST NOT be implemented.

### III. Mobile Identifier (Single Source of Truth)
The mobile number is the unique, primary identifier for all customers. Any data lookup, payment association, or notification target MUST revolve around the mobile number.

### IV. Resilience & Independence
The system MUST work even if external services (like WhatsApp) fail. Core operations, particularly saving payments and maintaining the local database, must remain functional regardless of the status of notification channels.

### V. Security-First Administration
The system uses a single admin password (gym PIN) stored securely in environment variables. Access control is binary: authorized admin or public. Unauthorized users MUST NOT access payment actions or sensitive configuration.

### VI. Side-Effect Integrity
Core actions (e.g., saving payments) must succeed independently of their side effects (e.g., sending a notification). Notifications are best-effort; a notification failure MUST NOT rollback a successful payment entry.

## Technology Constraints

### Stack Requirements
- **Backend**: Python + FastAPI
- **Validation**: Pydantic for all data validation and schema enforcement.
- **Database**: SQLite (local file-based) for MVP persistence.
- **Frontend**: Simple web UI (Next.js or basic HTML).
- **Deployment**: Free-tier friendly (Vercel-compatible).

## Development Workflow

### Planning & Execution
- Use `/sp.specify` to define features.
- Use `/sp.plan` to derive technical architecture.
- Use `/sp.tasks` to generate actionable items.
- All code changes must be small, testable, and reference specific code line numbers (file:line).

## Governance

### Amendment & Versioning
- This constitution is the authoritative source for all architectural and procedural decisions.
- Versioning follows semantic versioning (MAJOR.MINOR.PATCH).
- MAJOR: Fundamental principle changes or removals.
- MINOR: New principles or significant guidance expansions.
- PATCH: Formatting, typos, or minor clarifications.
- All amendments require a Sync Impact Report and verification across all project templates.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04
