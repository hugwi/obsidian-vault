# Phase 3: Migrate ROI Daily Summary

**Scope:** Same pattern as Phase 2, applied to `roi-issue-daily-summary.service.ts`.

## Files to create

#### `api/src/infrastructure/services/notification/templates/roi-daily-summary/roi-daily-summary.types.ts`
```typescript
export type RoiDailySummaryData = {
  recipientName: string;
  issues: Array<{
    description: string;
    severity: string;
    createdAt: Date;
  }>;
  dashboardUrl: string;
};
```

#### `api/src/infrastructure/services/notification/templates/roi-daily-summary/roi-daily-summary.slack.ts`
Extract Slack message building from existing `roi-issue-daily-summary.service.ts`.

#### `api/src/infrastructure/services/notification/templates/roi-daily-summary/roi-daily-summary.email.ts`
Extract email building from existing `roi-issue-daily-summary.service.ts`.

## Files to modify

#### `api/src/application/services/roi-validation-issue/roi-issue-daily-summary.service.ts`
- Remove `SlackApplicationRepository`, `SlackChatService`, `MailjetService` dependencies
- Add `NotificationService` dependency
- Use `notifyUser()` with Slack DM first, email fallback
- Use templates for message rendering
