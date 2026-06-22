# Phase 2: Extract Templates, Migrate Answer-Ready Notification

**Scope:** Move message building into templates, refactor `TrustPortalAnswerReadyNotificationService` to use `NotificationService`.

## Files to create

### Templates

#### `api/src/infrastructure/services/notification/templates/notification-template.interface.ts`
```typescript
export interface SlackTemplate<T> {
  render(data: T): string;
}

export interface EmailTemplate<T> {
  render(data: T): { subject: string; html: string };
}
```

#### `api/src/infrastructure/services/notification/templates/answers-ready/answers-ready.types.ts`
```typescript
export type AnswersReadyData = {
  questionnaireName: string;
  source: string | null;
  assignedQuestions: Array<{ question: string }>;
  reviewUrl: string;
};
```

#### `api/src/infrastructure/services/notification/templates/answers-ready/answers-ready.slack.ts`
```typescript
import { SlackTemplate } from '../notification-template.interface';
import { AnswersReadyData } from './answers-ready.types';

export class AnswersReadySlackTemplate implements SlackTemplate<AnswersReadyData> {
  render(data: AnswersReadyData): string {
    const sourceText = data.source ? ` from *${this.escape(data.source)}*` : '';
    const questionList = data.assignedQuestions
      .map((q) => `• ${this.escape(q.question)}`)
      .join('\n');

    return [
      `✅ *AI answers are ready for review*`,
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

#### `api/src/infrastructure/services/notification/templates/answers-ready/answers-ready.email.ts`
```typescript
import { EmailTemplate } from '../notification-template.interface';
import { AnswersReadyData } from './answers-ready.types';

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
        `<p>— Ethira</p>`,
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

## Files to modify

### `api/src/application/services/trust-portal-slack/trust-portal-answer-ready-notification.service.ts`

Replace the entire service with:

```typescript
import { Injectable, Logger } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { TrustPortalQuestionRepository } from '../../../domain/repositories/trust-portal/trust-portal-question.repository';
import { TrustPortalReceivedQuestionnaireRepository } from '../../../domain/repositories/trust-portal/trust-portal-received-questionnaire.repository';
import { NotificationService } from '../notification/notification.service';
import { NotificationChannel } from '../../../domain/notification/notification-channel';
import { TrustPortalQuestion } from '../../../domain/entities/trust-portal/trust-portal-question.entity';
import { WorkspaceUser } from '../../../domain/entities/workspace/workspace-user.entity';
import { AnswersReadySlackTemplate } from '../../../infrastructure/services/notification/templates/answers-ready/answers-ready.slack';
import { AnswersReadyEmailTemplate } from '../../../infrastructure/services/notification/templates/answers-ready/answers-ready.email';
import { AnswersReadyData } from '../../../infrastructure/services/notification/templates/answers-ready/answers-ready.types';

interface ReviewerAssignment {
  reviewer: WorkspaceUser;
  assignedQuestions: TrustPortalQuestion[];
}

@Injectable()
export class TrustPortalAnswerReadyNotificationService {
  private readonly logger = new Logger(TrustPortalAnswerReadyNotificationService.name);
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
        assignedQuestions: assignment.assignedQuestions.map((q) => ({ question: q.question })),
        reviewUrl,
      };

      await this.notificationService.notifyUser(workspaceId, assignment.reviewer.email, [
        { channel: NotificationChannel.SLACK_DM, message: this.slackTemplate.render(data) },
        { channel: NotificationChannel.EMAIL, message: this.emailTemplate.render(data) },
      ]);
    }
  }

  private groupQuestionsByReviewer(questions: TrustPortalQuestion[]): ReviewerAssignment[] {
    const assignmentMap = new Map<string, ReviewerAssignment>();
    for (const question of questions) {
      if (!question.assigneeWorkspaceUser) continue;
      const reviewer = question.assigneeWorkspaceUser;
      const existing = assignmentMap.get(reviewer.id);
      if (existing) {
        existing.assignedQuestions.push(question);
      } else {
        assignmentMap.set(reviewer.id, { reviewer, assignedQuestions: [question] });
      }
    }
    return Array.from(assignmentMap.values());
  }

  private buildReviewUrl(questionnaireId: string): string {
    const frontendUrl = this.configService.get<string>('frontend.url') || 'http://localhost:3002';
    return `${frontendUrl}/trust-exchange/questionnaire-review/${questionnaireId}`;
  }
}
```

**Key changes:**
- Removed `SlackApplicationRepository`, `SlackChatService`, `MailjetService` dependencies
- Added `NotificationService` dependency
- Removed `sendSlackDm()`, `sendEmail()`, `buildSlackMessage()`, `escapeHtml()`, `escapeSlackMrkdwn()`
- Uses templates for message rendering
- Uses `notifyUser()` with ordered channel list for fallback
