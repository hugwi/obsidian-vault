# ADR: Unified Notification System

## Context

Notification logic is scattered across the codebase with inconsistent patterns:

- `TrustPortalAnswerReadyNotificationService` -- Slack DM with email fallback, but **doesn't check `sendDirectMessage` return value** (the bug in Vilma's PR #844)
- `RoiIssueDailySummaryService` -- Slack DM with email fallback, **correctly checks return value**
- `TrustExchangeAccessRequestSlackNotificationService` -- Slack channel only, no email fallback, silently swallows failures
- `SlackNotificationService` (infrastructure) -- internal webhook-based alerts (DLQ, cost reports), completely separate pattern

Each service independently: looks up Slack apps, resolves Slack users, builds messages, handles fallback (or doesn't), and logs. This leads to duplicated logic, inconsistent error handling, and bugs like the one in PR #844 where a null return silently drops a notification.

### Root cause: `SlackChatService` return type ambiguity

`sendDirectMessage` (and most other methods) return `T | null` for two distinct failure modes:
1. **Not configured** -- no Slack app exists for the workspace
2. **Operational failure** -- the API call (`openConversation`/`postMessage`) failed

Callers can't distinguish between them. See `api/src/application/services/slack/slack-chat.service.ts:184-204`.

## Decision

Introduce a unified notification system using the **Strategy + Resolver** pattern, refactored incrementally across multiple PRs.

### Design principles
- **Two API levels**: high-level `notifyUser()` for the common DM case, low-level `sendWithFallback()` for explicit target control
- **Callers describe intent, not plumbing**: feature services say "notify this person" with rendered messages, never touch Slack app lookups or user ID resolution
- **Communicators wrap existing services**: `SlackChatService` and `MailjetService` stay as-is, communicators handle null-checking and result typing
- **Templates separate rendering from delivery**: message building moves out of notification services into dedicated template classes

### References
- **Clean Code** (Robert Martin) -- don't return null, throw or use special-case objects
- **Parse, Don't Validate** (Alexis King) -- encode outcomes in types so callers can't ignore them
- **Strategy + Resolver patterns** -- encapsulate interchangeable behaviors, resolve at runtime

---

## Full Implementation

### 1. Domain Layer -- Types and Contracts

```
api/src/domain/notification/
  notification-channel.ts
  notification-target.ts
  notification-result.ts
```

#### `notification-channel.ts`
```typescript
export enum NotificationChannel {
  SLACK_DM = 'slack_dm',
  SLACK_CHANNEL = 'slack_channel',
  SLACK_THREAD = 'slack_thread',
  EMAIL = 'email',
}
```

#### `notification-target.ts`
```typescript
import { NotificationChannel } from './notification-channel';

export type NotificationTarget = {
  channel: NotificationChannel;
  /** email address, Slack user ID, channel ID, etc. */
  recipientId: string;
  /** For threads: the parent message timestamp */
  threadTs?: string;
};
```

#### `notification-result.ts`
```typescript
export type NotificationSendResult =
  | { status: 'sent'; channel: string }
  | { status: 'not_configured'; channel: string }
  | { status: 'failed'; channel: string; reason: string };
```

### 2. Infrastructure Layer -- Communicators

```
api/src/infrastructure/services/notification/
  communicator.interface.ts
  slack-dm.communicator.ts
  slack-channel.communicator.ts
  email.communicator.ts
  communication-resolver.service.ts
```

#### `communicator.interface.ts`
```typescript
import { NotificationTarget } from '../../../domain/notification/notification-target';
import { NotificationSendResult } from '../../../domain/notification/notification-result';

export interface Communicator {
  send(
    workspaceId: string,
    target: NotificationTarget,
    message: unknown,
  ): Promise<NotificationSendResult>;
}
```

#### `slack-dm.communicator.ts`
```typescript
import { Injectable } from '@nestjs/common';
import { Communicator } from './communicator.interface';
import { SlackChatService } from '../slack/slack-chat.service';
import { NotificationTarget } from '../../../domain/notification/notification-target';
import { NotificationSendResult } from '../../../domain/notification/notification-result';

@Injectable()
export class SlackDmCommunicator implements Communicator {
  constructor(private readonly slackChatService: SlackChatService) {}

  async send(
    workspaceId: string,
    target: NotificationTarget,
    message: string,
  ): Promise<NotificationSendResult> {
    const result = await this.slackChatService.sendDirectMessage(workspaceId, {
      userId: target.recipientId,
      message,
    });

    if (!result) {
      return { status: 'failed', channel: 'slack_dm', reason: 'sendDirectMessage returned null' };
    }
    return { status: 'sent', channel: 'slack_dm' };
  }
}
```

#### `slack-channel.communicator.ts`
```typescript
import { Injectable } from '@nestjs/common';
import { Communicator } from './communicator.interface';
import { SlackChatService } from '../slack/slack-chat.service';
import { NotificationTarget } from '../../../domain/notification/notification-target';
import { NotificationSendResult } from '../../../domain/notification/notification-result';

@Injectable()
export class SlackChannelCommunicator implements Communicator {
  constructor(private readonly slackChatService: SlackChatService) {}

  async send(
    workspaceId: string,
    target: NotificationTarget,
    message: string,
  ): Promise<NotificationSendResult> {
    const result = await this.slackChatService.sendChannelMessage(workspaceId, {
      channelId: target.recipientId,
      message,
      ...(target.threadTs ? { threadTs: target.threadTs } : {}),
    });

    if (!result) {
      return { status: 'failed', channel: 'slack_channel', reason: 'sendChannelMessage returned null' };
    }
    return { status: 'sent', channel: 'slack_channel' };
  }
}
```

#### `email.communicator.ts`
```typescript
import { Injectable } from '@nestjs/common';
import { Communicator } from './communicator.interface';
import { MailjetService } from '../mailjet/mailjet.service';
import { NotificationTarget } from '../../../domain/notification/notification-target';
import { NotificationSendResult } from '../../../domain/notification/notification-result';

@Injectable()
export class EmailCommunicator implements Communicator {
  constructor(private readonly mailjetService: MailjetService) {}

  async send(
    workspaceId: string,
    target: NotificationTarget,
    message: { subject: string; html: string },
  ): Promise<NotificationSendResult> {
    try {
      await this.mailjetService.sendEmail({
        to: target.recipientId,
        subject: message.subject,
        html: message.html,
      });
      return { status: 'sent', channel: 'email' };
    } catch {
      return { status: 'failed', channel: 'email', reason: 'Email delivery failed' };
    }
  }
}
```

#### `communication-resolver.service.ts`
```typescript
import { Injectable } from '@nestjs/common';
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { Communicator } from './communicator.interface';
import { SlackDmCommunicator } from './slack-dm.communicator';
import { SlackChannelCommunicator } from './slack-channel.communicator';
import { EmailCommunicator } from './email.communicator';

@Injectable()
export class CommunicationResolverService {
  private readonly communicators: Map<NotificationChannel, Communicator>;

  constructor(
    slackDm: SlackDmCommunicator,
    slackChannel: SlackChannelCommunicator,
    email: EmailCommunicator,
  ) {
    this.communicators = new Map([
      [NotificationChannel.SLACK_DM, slackDm],
      [NotificationChannel.SLACK_CHANNEL, slackChannel],
      [NotificationChannel.SLACK_THREAD, slackChannel],
      [NotificationChannel.EMAIL, email],
    ]);
  }

  resolve(channel: NotificationChannel): Communicator {
    const communicator = this.communicators.get(channel);
    if (!communicator) {
      throw new Error(`No communicator registered for channel: ${channel}`);
    }
    return communicator;
  }
}
```

### 3. Infrastructure Layer -- Templates

```
api/src/infrastructure/services/notification/templates/
  notification-template.interface.ts
  answers-ready/
    answers-ready.slack.ts
    answers-ready.email.ts
```

#### `notification-template.interface.ts`
```typescript
export interface SlackTemplate<T> {
  render(data: T): string;
}

export interface EmailTemplate<T> {
  render(data: T): { subject: string; html: string };
}
```

#### `answers-ready/answers-ready.slack.ts`
```typescript
import { SlackTemplate } from '../notification-template.interface';

export type AnswersReadyData = {
  questionnaireName: string;
  source: string | null;
  assignedQuestions: Array<{ question: string }>;
  reviewUrl: string;
};

export class AnswersReadySlackTemplate implements SlackTemplate<AnswersReadyData> {
  render(data: AnswersReadyData): string {
    const sourceText = data.source ? ` from *${this.escape(data.source)}*` : '';
    const questionList = data.assignedQuestions
      .map((q) => `- ${this.escape(q.question)}`)
      .join('\n');

    return [
      `*AI answers are ready for review*`,
      ``,
      `Questionnaire: *${this.escape(data.questionnaireName)}*${sourceText}`,
      `You have *${data.assignedQuestions.length}* question(s) assigned to you:`,
      ``,
      questionList,
      ``,
      `<${data.reviewUrl}|Start reviewing now>`,
    ].join('\n');
  }

  private escape(value: string): string {
    return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
}
```

#### `answers-ready/answers-ready.email.ts`
```typescript
import { EmailTemplate } from '../notification-template.interface';
import { AnswersReadyData } from './answers-ready.slack';

export class AnswersReadyEmailTemplate implements EmailTemplate<AnswersReadyData> {
  render(data: AnswersReadyData): { subject: string; html: string } {
    const safeName = this.escape(data.questionnaireName);
    const sourceText = data.source ? ` from ${this.escape(data.source)}` : '';
    const questionListHtml = data.assignedQuestions
      .map((q) => `<li>${this.escape(q.question)}</li>`)
      .join('');

    return {
      subject: `AI answers ready for review: ${data.questionnaireName}`,
      html: [
        `<p>Hi,</p>`,
        `<p>The AI has finished generating answers for the questionnaire `,
        `<strong>${safeName}</strong>${sourceText}.</p>`,
        `<p>You have <strong>${data.assignedQuestions.length}</strong> `,
        `question(s) assigned to you:</p>`,
        `<ul>${questionListHtml}</ul>`,
        `<p><a href="${data.reviewUrl}">Start reviewing now</a></p>`,
        `<p>-- Ethira</p>`,
      ].join(''),
    };
  }

  private escape(value: string): string {
    return value
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
}
```

### 4. Application Layer -- NotificationService (dual API)

The service exposes two levels of abstraction:

- **`notifyUser()`** -- high-level, channel-agnostic. Caller provides an email address and an **ordered list of channel messages** (priority order). The service resolves each channel (Slack user lookup, app check, etc.) and builds targets automatically. Falls back through the list on failure.
- **`sendWithFallback()`** -- low-level. Caller provides pre-resolved targets. Used when the caller needs full control (e.g., sending to a specific Slack channel ID, custom fallback chains).

The high-level API is **not Slack-specific**. It uses a `UserChannelResolver` interface so that adding Teams (or any future channel) means registering a new resolver -- no changes to `NotificationService` or callers.

```
api/src/application/services/notification/
  notification.service.ts
  user-channel-resolver.interface.ts
  slack-user-channel.resolver.ts
  email-user-channel.resolver.ts
```

#### `user-channel-resolver.interface.ts`

Each channel type knows how to resolve a user email into a target for that channel:

```typescript
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { NotificationTarget } from '../../../domain/notification/notification-target';

export interface UserChannelResolver {
  readonly channel: NotificationChannel;

  /**
   * Resolves an email address into a target for this channel.
   * Returns null if this channel is not available (e.g., Slack not configured, user not found).
   */
  resolve(workspaceId: string, email: string): Promise<NotificationTarget | null>;
}
```

#### `slack-user-channel.resolver.ts`
```typescript
import { Injectable, Logger } from '@nestjs/common';
import { UserChannelResolver } from './user-channel-resolver.interface';
import { SlackApplicationRepository } from '../../../domain/repositories/integration/slack-application.repository';
import { SlackChatService } from '../slack/slack-chat.service';
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { NotificationTarget } from '../../../domain/notification/notification-target';

@Injectable()
export class SlackUserChannelResolver implements UserChannelResolver {
  readonly channel = NotificationChannel.SLACK_DM;
  private readonly logger = new Logger(SlackUserChannelResolver.name);

  constructor(
    private readonly slackApplicationRepository: SlackApplicationRepository,
    private readonly slackChatService: SlackChatService,
  ) {}

  async resolve(workspaceId: string, email: string): Promise<NotificationTarget | null> {
    const slackApp = await this.slackApplicationRepository.findByWorkspaceId(workspaceId);
    if (!slackApp) return null;

    const slackUserId = await this.slackChatService.lookupUserIdByEmail(workspaceId, email);
    if (!slackUserId) {
      this.logger.warn(`No Slack user found for ${email}`);
      return null;
    }

    return { channel: NotificationChannel.SLACK_DM, recipientId: slackUserId };
  }
}
```

#### `email-user-channel.resolver.ts`
```typescript
import { Injectable } from '@nestjs/common';
import { UserChannelResolver } from './user-channel-resolver.interface';
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { NotificationTarget } from '../../../domain/notification/notification-target';

@Injectable()
export class EmailUserChannelResolver implements UserChannelResolver {
  readonly channel = NotificationChannel.EMAIL;

  async resolve(_workspaceId: string, email: string): Promise<NotificationTarget | null> {
    return { channel: NotificationChannel.EMAIL, recipientId: email };
  }
}
```

#### Adding Teams in the future -- just a new resolver:
```typescript
@Injectable()
export class TeamsUserChannelResolver implements UserChannelResolver {
  readonly channel = NotificationChannel.TEAMS_DM;

  async resolve(workspaceId: string, email: string): Promise<NotificationTarget | null> {
    const teamsApp = await this.teamsAppRepository.findByWorkspaceId(workspaceId);
    if (!teamsApp) return null;
    const teamsUserId = await this.teamsService.lookupUserByEmail(workspaceId, email);
    if (!teamsUserId) return null;
    return { channel: NotificationChannel.TEAMS_DM, recipientId: teamsUserId };
  }
}
```

#### `notification.service.ts`
```typescript
import { Injectable, Inject, Logger } from '@nestjs/common';
import { CommunicationResolverService } from '../../../infrastructure/services/notification/communication-resolver.service';
import { UserChannelResolver } from './user-channel-resolver.interface';
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { NotificationTarget } from '../../../domain/notification/notification-target';
import { NotificationSendResult } from '../../../domain/notification/notification-result';

@Injectable()
export class NotificationService {
  private readonly logger = new Logger(NotificationService.name);
  private readonly channelResolvers: Map<NotificationChannel, UserChannelResolver>;

  constructor(
    private readonly communicationResolver: CommunicationResolverService,
    @Inject('USER_CHANNEL_RESOLVERS') resolvers: UserChannelResolver[],
  ) {
    this.channelResolvers = new Map(resolvers.map((r) => [r.channel, r]));
  }

  /**
   * High-level: notify a person by email address.
   * Accepts an ordered list of { channel, message } pairs (priority order).
   * Resolves each channel into a target, then sends with fallback.
   *
   * Channel-agnostic -- adding Teams means registering a new UserChannelResolver,
   * no changes to this method or its callers.
   */
  async notifyUser(
    workspaceId: string,
    email: string,
    channels: Array<{
      channel: NotificationChannel;
      message: unknown;
    }>,
  ): Promise<NotificationSendResult> {
    const attempts: Array<{ target: NotificationTarget; message: unknown }> = [];

    for (const { channel, message } of channels) {
      const resolver = this.channelResolvers.get(channel);
      if (!resolver) {
        this.logger.warn(`No resolver for channel ${channel} -- skipping`);
        continue;
      }

      const target = await resolver.resolve(workspaceId, email);
      if (target) {
        attempts.push({ target, message });
      }
    }

    return this.sendWithFallback(workspaceId, attempts);
  }

  /**
   * Low-level: send to an explicit ordered list of pre-resolved targets.
   * Tries each in order, stops on first success.
   */
  async sendWithFallback(
    workspaceId: string,
    attempts: Array<{
      target: NotificationTarget;
      message: unknown;
    }>,
  ): Promise<NotificationSendResult> {
    if (attempts.length === 0) {
      return { status: 'failed', channel: 'none', reason: 'No notification targets provided' };
    }

    const errors: string[] = [];

    for (const attempt of attempts) {
      const communicator = this.communicationResolver.resolve(attempt.target.channel);

      try {
        const result = await communicator.send(workspaceId, attempt.target, attempt.message);

        if (result.status === 'sent') {
          this.logger.log(
            `Notification delivered via ${result.channel} to ${attempt.target.recipientId}`,
          );
          return result;
        }

        this.logger.warn(
          `Notification not delivered via ${result.channel}: ${result.status}` +
            ('reason' in result ? ` (${result.reason})` : ''),
        );
        errors.push(`${result.channel}: ${result.status}`);
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        this.logger.error(`Notification error via ${attempt.target.channel}: ${message}`);
        errors.push(`${attempt.target.channel}: ${message}`);
      }
    }

    const finalResult: NotificationSendResult = {
      status: 'failed',
      channel: 'all',
      reason: `All channels failed: ${errors.join('; ')}`,
    };
    this.logger.error(finalResult.reason);
    return finalResult;
  }
}
```

### 5. Application Layer -- Feature-Specific Orchestrators

Each feature service focuses on business logic (who to notify, what data to include) and calls the high-level or low-level API as appropriate.

#### `trust-portal-answer-ready-notification.service.ts` (refactored)

Uses `notifyUser()` with an ordered channel list. The caller defines priority (Slack first, email fallback) but never touches Slack apps, user IDs, or targets:

```typescript
@Injectable()
export class TrustPortalAnswerReadyNotificationService {
  private readonly slackTemplate = new AnswersReadySlackTemplate();
  private readonly emailTemplate = new AnswersReadyEmailTemplate();

  constructor(
    private readonly questionRepository: TrustPortalQuestionRepository,
    private readonly questionnaireRepository: TrustPortalReceivedQuestionnaireRepository,
    private readonly notificationService: NotificationService,
    private readonly configService: ConfigService,
  ) {}

  async notifyReviewers(questionnaireId: string, workspaceId: string): Promise<void> {
    const questionnaire = await this.questionnaireRepository.findById(questionnaireId, workspaceId);
    if (!questionnaire) return;

    const questions = await this.questionRepository.findByQuestionnaireIdWithAssignees(
      questionnaireId, workspaceId,
    );
    const assignments = this.groupQuestionsByReviewer(questions);
    if (assignments.length === 0) return;

    const reviewUrl = this.buildReviewUrl(questionnaireId);

    for (const assignment of assignments) {
      const data: AnswersReadyData = {
        questionnaireName: questionnaire.name,
        source: questionnaire.source,
        assignedQuestions: assignment.assignedQuestions,
        reviewUrl,
      };

      // Order = priority. Slack first, email fallback.
      // To add Teams: just add { channel: NotificationChannel.TEAMS_DM, message: teamsTemplate.render(data) }
      await this.notificationService.notifyUser(workspaceId, assignment.reviewer.email, [
        { channel: NotificationChannel.SLACK_DM, message: this.slackTemplate.render(data) },
        { channel: NotificationChannel.EMAIL, message: this.emailTemplate.render(data) },
      ]);
    }
  }

  // ... groupQuestionsByReviewer, buildReviewUrl (unchanged)
}
```

#### `trust-exchange-access-request-slack-notification.service.ts` (refactored)

Uses `sendWithFallback()` -- needs explicit channel targeting (not a person DM):

```typescript
async notifySlackChannel(
  workspaceId: string,
  accessRequest: TrustExchangeAccessRequest,
): Promise<void> {
  const config = await this.trustExchangeRepository.findOneByWorkspaceId(workspaceId);
  if (!config?.accessRequestSlackChannelId) return;

  const blocks = this.buildNotificationBlocks(accessRequest);

  await this.notificationService.sendWithFallback(workspaceId, [
    {
      target: {
        channel: NotificationChannel.SLACK_CHANNEL,
        recipientId: config.accessRequestSlackChannelId,
      },
      message: JSON.stringify(blocks),
    },
  ]);
}
```

### 6. How this maps to existing code

| Current code | What it becomes |
|---|---|
| `SlackChatService` | Stays as-is. Communicators wrap it. |
| `MailjetService` | Stays as-is. `EmailCommunicator` wraps it. |
| `SlackApplicationRepository.findByWorkspaceId` checks in each service | Moves into `SlackUserChannelResolver` |
| `SlackChatService.lookupUserIdByEmail` calls in each service | Moves into `SlackUserChannelResolver` |
| `buildSlackMessage()` in each service | Moves to `SlackTemplate` classes |
| `buildEmailHtml()` in each service | Moves to `EmailTemplate` classes |
| Manual `if (slackApp) { ... } else { ... }` | Replaced by `notifyUser()` or `sendWithFallback()` |
| Unchecked `sendDirectMessage` return | `SlackDmCommunicator` always checks and returns `NotificationSendResult` |

---

## Incremental Refactor Plan

### Phase 0: Fix the bug (this PR -- #844)
**Scope:** 1 file, ~10 lines changed
**File:** `api/src/application/services/trust-portal-slack/trust-portal-answer-ready-notification.service.ts`

Check the `sendDirectMessage` return value and fall back to email when null. Matches the existing `roi-issue-daily-summary` pattern. No new abstractions.

```typescript
const result = await this.slackChatService.sendDirectMessage(workspaceId, {
  userId: slackUserId,
  message: this.buildSlackMessage(params),
});
if (!result) {
  this.logger.warn(`Slack DM delivery failed for ${email} -- falling back to email`);
  await this.sendEmail(email, params);
  return;
}
```

### Phase 1: Introduce domain types + NotificationService
**Scope:** New files only, no existing code changes
**Files to create:**
- `api/src/domain/notification/notification-channel.ts`
- `api/src/domain/notification/notification-target.ts`
- `api/src/domain/notification/notification-result.ts`
- `api/src/infrastructure/services/notification/communicator.interface.ts`
- `api/src/infrastructure/services/notification/slack-dm.communicator.ts`
- `api/src/infrastructure/services/notification/email.communicator.ts`
- `api/src/infrastructure/services/notification/communication-resolver.service.ts`
- `api/src/application/services/notification/user-channel-resolver.interface.ts`
- `api/src/application/services/notification/slack-user-channel.resolver.ts`
- `api/src/application/services/notification/email-user-channel.resolver.ts`
- `api/src/application/services/notification/notification.service.ts` (with both `notifyUser` and `sendWithFallback`)
- `api/src/application/modules/notification.module.ts`

**Tests:** Unit tests for `notifyUser()`, `sendWithFallback()`, each communicator, each channel resolver.

**Risk:** Zero. All new files, nothing existing changes.

### Phase 2: Extract templates, migrate first service
**Scope:** Move message building out of `trust-portal-answer-ready-notification.service.ts`
**Files to create:**
- `api/src/infrastructure/services/notification/templates/notification-template.interface.ts`
- `api/src/infrastructure/services/notification/templates/answers-ready/answers-ready.slack.ts`
- `api/src/infrastructure/services/notification/templates/answers-ready/answers-ready.email.ts`

**Files to modify:**
- `api/src/application/services/trust-portal-slack/trust-portal-answer-ready-notification.service.ts` -- use templates + `notifyUser()`

**Tests:** Existing spec still passes. Add template unit tests.

### Phase 3: Migrate `roi-issue-daily-summary` notification logic
**Scope:** Same pattern as Phase 2, second service
**Files to create:**
- `api/src/infrastructure/services/notification/templates/roi-daily-summary/roi-daily-summary.slack.ts`
- `api/src/infrastructure/services/notification/templates/roi-daily-summary/roi-daily-summary.email.ts`

**Files to modify:**
- `api/src/application/services/roi-validation-issue/roi-issue-daily-summary.service.ts`

### Phase 4: Add `SlackChannelCommunicator`, migrate trust exchange
**Scope:** Adds channel-based sending
**Files to create:**
- `api/src/infrastructure/services/notification/slack-channel.communicator.ts`

**Files to modify:**
- `api/src/application/services/trust-exchange/trust-exchange-access-request-slack-notification.service.ts` -- use `sendWithFallback()` with channel targets

### Phase 5 (optional): Add notification queue
**Scope:** Decouple notification sending from business processors
**Files to create:**
- Add `NOTIFICATION` to `QueueNames` enum in `api/src/infrastructure/queue/queue.module.ts`
- `api/src/application/processors/notification/notification.processor.ts`

**Files to modify:**
- `api/src/application/processors/received-questionnaire-answer-generation/received-questionnaire-answer-generation.processor.ts` -- emit event instead of calling notification service directly

**When:** Only when notification sending causes performance issues in processors, or when you need independent retry/DLQ for notifications.

---

## Verification

### Phase 0 (this PR)
- Run existing tests: `cd api && npx jest trust-portal-answer-ready-notification`
- Add test case: mock `sendDirectMessage` returning `null`, verify `sendEmail` is called

### Phase 1
- Unit tests for each communicator (mock `SlackChatService`, `MailjetService`)
- Unit tests for `NotificationService.notifyUser()` (mock `SlackApplicationRepository`, `SlackChatService`, communicators)
- Unit tests for `NotificationService.sendWithFallback()` (mock communicators returning sent/failed/throwing)
- Test fallback chain: first communicator fails -> second succeeds -> returns sent
- Test all-fail case: all communicators fail -> returns failed with aggregated reasons

### Phase 2-4
- Existing test suites for each migrated service still pass
- Template unit tests (render with various data, verify escaping)
- Manual verification in staging environment

---

## Deliverables

1. **ADR document** -- Save the full ADR to `docs/adr-unified-notification-system.md` in the repo for team reference
2. **Memory file** -- Save to auto-memory for future session context
3. **Apply patches** -- Generate patch files for each phase (Phase 0-4) at `docs/notification-refactor-patches/` so each can be reviewed and applied independently
