---
categories:
  - "[[Projects]]"
project: "[[Ethira]]"
created: 2026-06-23
---
# Phase 4: Add SlackChannelCommunicator, Migrate Trust Exchange

**Scope:** Adds channel-based Slack sending, migrates trust exchange access request notifications.

## Files to create

#### `api/src/infrastructure/services/notification/slack-channel.communicator.ts`
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

## Files to modify

#### `api/src/infrastructure/services/notification/communication-resolver.service.ts`
Add `SlackChannelCommunicator` to the communicators map:
```typescript
[NotificationChannel.SLACK_CHANNEL, slackChannel],
[NotificationChannel.SLACK_THREAD, slackChannel],
```

#### `api/src/application/modules/notification.module.ts`
Register `SlackChannelCommunicator` as a provider.

#### `api/src/application/services/trust-exchange/trust-exchange-access-request-slack-notification.service.ts`
Refactor to use `sendWithFallback()` with explicit channel target:
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
