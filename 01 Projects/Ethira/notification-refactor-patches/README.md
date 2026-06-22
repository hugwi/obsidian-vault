# Notification System Refactor Patches

Incremental refactor plan for the unified notification system. See `docs/adr-unified-notification-system.md` for the full ADR.

## Phases

| Phase | Scope | Risk | Files changed |
|-------|-------|------|---------------|
| [Phase 0](phase-0-fix-null-check-bug.patch) | Fix `sendDirectMessage` null-check bug | Minimal | 1 file, ~10 lines |
| [Phase 1](phase-1-domain-types-and-notification-service.md) | Domain types + NotificationService | Zero (all new files) | ~12 new files |
| [Phase 2](phase-2-extract-templates-migrate-answer-ready.md) | Templates + migrate answer-ready | Low | 5 new + 1 modified |
| [Phase 3](phase-3-migrate-roi-daily-summary.md) | Migrate ROI daily summary | Low | 3 new + 1 modified |
| [Phase 4](phase-4-slack-channel-communicator-trust-exchange.md) | SlackChannelCommunicator + trust exchange | Low | 1 new + 3 modified |

## How to apply

- **Phase 0**: Apply the `.patch` file directly with `git apply`
- **Phases 1-4**: Follow the markdown guides, creating files and modifying existing ones as described

## Key design decisions

- **Dual API**: `notifyUser()` (high-level, channel-agnostic) and `sendWithFallback()` (low-level, explicit targets)
- **Channel-agnostic**: `UserChannelResolver` per channel type -- adding Teams = new resolver, zero changes to NotificationService
- **Communicators wrap existing services**: `SlackChatService` and `MailjetService` stay as-is
- **`NotificationSendResult` discriminated union**: replaces ambiguous `T | null` returns
