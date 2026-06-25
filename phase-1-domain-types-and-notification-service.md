---
categories:
  - "[[Projects]]"
project: "[[Ethira]]"
created: 2026-06-23
---
# Phase 1: Domain Types + NotificationService

**Scope:** New files only, zero changes to existing code.

## Files to create

### 1. Domain types

#### `api/src/domain/notification/notification-channel.ts`
```typescript
export enum NotificationChannel {
  SLACK_DM = 'slack_dm',
  SLACK_CHANNEL = 'slack_channel',
  SLACK_THREAD = 'slack_thread',
  EMAIL = 'email',
}
```

#### `api/src/domain/notification/notification-target.ts`
```typescript
import { NotificationChannel } from './notification-channel';

export type NotificationTarget = {
  channel: NotificationChannel;
  recipientId: string;
  threadTs?: string;
};
```

#### `api/src/domain/notification/notification-result.ts`
```typescript
export type NotificationSendResult =
  | { status: 'sent'; channel: string }
  | { status: 'not_configured'; channel: string }
  | { status: 'failed'; channel: string; reason: string };
```

### 2. Communicators

#### `api/src/infrastructure/services/notification/communicator.interface.ts`
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

#### `api/src/infrastructure/services/notification/slack-dm.communicator.ts`
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

#### `api/src/infrastructure/services/notification/email.communicator.ts`
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
    _workspaceId: string,
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

#### `api/src/infrastructure/services/notification/communication-resolver.service.ts`
```typescript
import { Injectable } from '@nestjs/common';
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { Communicator } from './communicator.interface';
import { SlackDmCommunicator } from './slack-dm.communicator';
import { EmailCommunicator } from './email.communicator';

@Injectable()
export class CommunicationResolverService {
  private readonly communicators: Map<NotificationChannel, Communicator>;

  constructor(
    slackDm: SlackDmCommunicator,
    email: EmailCommunicator,
  ) {
    this.communicators = new Map([
      [NotificationChannel.SLACK_DM, slackDm],
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

### 3. Channel resolvers

#### `api/src/application/services/notification/user-channel-resolver.interface.ts`
```typescript
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { NotificationTarget } from '../../../domain/notification/notification-target';

export interface UserChannelResolver {
  readonly channel: NotificationChannel;
  resolve(workspaceId: string, email: string): Promise<NotificationTarget | null>;
}
```

#### `api/src/application/services/notification/slack-user-channel.resolver.ts`
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

#### `api/src/application/services/notification/email-user-channel.resolver.ts`
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

### 4. NotificationService (dual API)

#### `api/src/application/services/notification/notification.service.ts`
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

### 5. Module

#### `api/src/application/modules/notification.module.ts`
```typescript
import { Module } from '@nestjs/common';
import { NotificationService } from '../services/notification/notification.service';
import { SlackUserChannelResolver } from '../services/notification/slack-user-channel.resolver';
import { EmailUserChannelResolver } from '../services/notification/email-user-channel.resolver';
import { SlackDmCommunicator } from '../../infrastructure/services/notification/slack-dm.communicator';
import { EmailCommunicator } from '../../infrastructure/services/notification/email.communicator';
import { CommunicationResolverService } from '../../infrastructure/services/notification/communication-resolver.service';

@Module({
  providers: [
    NotificationService,
    SlackDmCommunicator,
    EmailCommunicator,
    CommunicationResolverService,
    SlackUserChannelResolver,
    EmailUserChannelResolver,
    {
      provide: 'USER_CHANNEL_RESOLVERS',
      useFactory: (slack: SlackUserChannelResolver, email: EmailUserChannelResolver) => [slack, email],
      inject: [SlackUserChannelResolver, EmailUserChannelResolver],
    },
  ],
  exports: [NotificationService],
})
export class NotificationModule {}
```

## Tests to write
- Unit tests for `SlackDmCommunicator` (mock `SlackChatService`)
- Unit tests for `EmailCommunicator` (mock `MailjetService`)
- Unit tests for `SlackUserChannelResolver` (mock repo + chat service)
- Unit tests for `NotificationService.notifyUser()` (mock resolvers + communicators)
- Unit tests for `NotificationService.sendWithFallback()` (fallback chain scenarios)
